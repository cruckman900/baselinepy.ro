import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_model import User, PasswordResetToken
from app.schemas.user_schema import UserCreate , UserRead , UserUpdate , UserLogin
from uuid import uuid4 , UUID
from datetime import datetime, timezone
import bcrypt
from pydantic import BaseModel, EmailStr
from jinja2 import Environment, FileSystemLoader
import smtplib
from email.mime.text import MIMEText
from app.config import settings

router = APIRouter(prefix="/users", tags=["Users"])

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordRequest(BaseModel):
    new_password: str

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode(), hashed.encode())

def generate_reset_token(user_id: UUID) -> str:
    return str(uuid4())

def send_reset_email(to_email: str, token: str):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("reset_email.html")
    reset_url = f"https://nextriff.netlify.app/reset-password/{token}"
    html_content = template.render(reset_url=reset_url)

    msg = MIMEText(html_content, "html")
    msg["Subject"] = "Reset Your Password"
    msg["From"] = "no-reply@cruckman.com"
    msg["To"] = to_email

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg)

def verify_reset_token(token: str, db: Session) -> int:
    record = db.query(PasswordResetToken).filter_by(token=token).first()
    if not record or record.expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Invalid or expired token")
    return record.user_id

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter_by(email=user.email).first()
    if existing:
        raise HTTPException(status_code=400 , detail="Email already registered")
    db_user = User(
        id=uuid4(),
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password), # use bcrypt later
        created_at=datetime.now(timezone.utc)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: UUID, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=list[UserRead])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.patch("/{user_id}", response_model=UserRead)
def update_user(user_id: UUID, update: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if update.username:
        user.username = update.username
    if update.password:
        user.hashed_password = hash_password(update.password)
    db.commit()
    db.refresh(user)
    return user

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: UUID, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()

@router.post("/login")
def login_user(payload: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "user_id": str(user.id)}

@router.post("/forgot-password")
def forgot_password(payload: ForgotPasswordRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Email not found")
    token = generate_reset_token(user.id)   # UUID or JWT
    send_reset_email(user.email, token)     # Email with reset link
    return {"message", "Reset link sent"}

@router.post("/reset-password/{token}")
def reset_password(token: str, payload: ResetPasswordRequest, db: Session = Depends(get_db)):
    user_id = verify_reset_token(token)
    user = db.query(User).get(user_id)
    user.hashed_password = hash_password(payload.new_password)
    db.commit()
    return {"message": "Password reset successful"}
