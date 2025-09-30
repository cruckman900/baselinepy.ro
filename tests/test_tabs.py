import fileinput
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def example_tab():
    os.makedirs("tabs", exist_ok=True)
    path = "tabs/example.ftab"
    with open(path, "wb") as f:
        f.write(b"X 1 2 0 3")
    yield path
    os.remove(path)

def test_upload_valid_file():
    test_file_content = b"X 1 2 0 3"
    response = client.post(
        "/upload/",
        files={"file": ("test.ftab", test_file_content, "text/plain")}
    )
    assert response.status_code == 200
    assert response.json()["filename"] == "test.ftab"

def test_upload_empty_file():
    response = client.post(
        "/upload/",
        files={"file": ("empty.ftab", b"", "text/plain")}
    )
    assert response.status_code == 400
    assert "Empty file" in response.json()["detail"]

def test_upload_wrong_extension():
    response = client.post(
        "/upload/",
        files={"file": ("not_a_tab.txt", b"X 1 2 0 3", "text/plain")}
    )
    assert response.status_code == 400
    assert "Invalid file type" in response.json()["detail"]

def test_download_existing_tab():
    # Assign: create the file
    os.makedirs("tabs", exist_ok=True)
    with open("tabs/example.ftab", "wb") as f:
        f.write(b"X 21 2 0 3")

    # Test: download it
    response = client.get("/download/test")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/plain")
    assert response.content == b"X 1 2 0 3"

    # Cleanup (optional)
    os.remove("tabs/example.ftab")

def test_download_missing_tab():
    response = client.get("/download/ghost")
    assert response.status_code == 404
    assert "Tab file not found" in response.json()["detail"]

def test_upload_large_file():
    large_content = b"X 1 2 0 3\n" * 10000  # ~50KB
    response = client.post(
        "/upload/",
        files={"file": ("big.ftab", large_content, "text/plain")}
    )
    assert response.status_code == 200
    assert response.json()["filename"] == "big.ftab"
