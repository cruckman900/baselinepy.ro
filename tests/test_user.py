from app.models import User

def setup_function():
    from app.database import SessionLocal
    db = SessionLocal()
    db.query(User).delete()
    db.commit()
    db.close()

def test_user_crud(client):
    # Create

    response = client.post("/users/", json={
        "username": "riffmaster",
        "email": "riff@example.com",
        "password": "shred123"
    })
    assert response.status_code == 200
    user = response.json()
    user_id = user["id"]

    # Read

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["username"] == "riffmaster"

    # Update

    response = client.patch(f"/users/{user_id}", json={"username": "updateduser"})
    assert response.status_code == 200
    assert response.json()["username"] == "updateduser"

    # List
    response = client.get("/users/")
    assert response.status_code == 200
    assert any(u["id"] == user_id for u in response.json())

    # Delete
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 204

def test_login_user(client):
    # Create user
    client.post("/users/", json={
        "username": "loginuser",
        "email": "login@example.com",
        "password": "securepass"
    })

    # Login
    response = client.post("/users/login", json={
        "email": "login@example.com",
        "password": "securepass"
    })
    assert response.status_code == 200
    assert "user_id" in response.json()
