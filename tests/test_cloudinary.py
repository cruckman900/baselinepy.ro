
# perfect scenario tests

def test_upload_valid_file(client):
    test_file_content = b"X 1 2 0 3"
    response = client.post(
        "/upload-file/",
        files={"file": ("test.ftab", test_file_content, "text/plain")}
    )
    assert response.status_code == 200
    data = response.json()
    public_id = data["public_id"]
    assert "cloudinary_url" in data
    assert data["cloudinary_url"].startswith("https://res.cloudinary.com/")

def test_download_existing_tab(client):
    response = client.get("/download/test.ftab")
    assert response.status_code == 200
    data = response.json()
    assert "cloudinary_url" in data
    assert data["cloudinary_url"].startswith("https://res.cloudinary.com/")

# edge case tests - upload

def test_upload_unsupported_mime_types(client):
    test_file_content = b"<html><body>Not a tab</body></html>"
    response = client.post(
        "/upload-file/",
        files={"file": ("bad.html", test_file_content, "text/html")}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Unsupported file type"

def test_upload_empty_file(client):
    response = client.post(
        "/upload-file/",
        files={"file": ("empty.ftab", b"", "text/plain")}
    )
    assert response.status_code == 400
    assert "Empty file" in response.json()["detail"]

def test_upload_missing_file(client):
    response = client.post("/upload")
    assert response.status_code == 422 # FAstAPI validation error

def test_upload_large_file(client):
    large_content = b"X " * 10_000_000 # ~20MB
    response = client.post(
        "/upload-file/",
        files={"file": ("big.ftab", large_content, "text/plain")}
    )
    assert response.status_code in [413, 400] # Depending on server config

# edge case tests - download

def test_download_nonexistent_tab(client):
    response = client.get("/downlaod/this-id-does-not-exist")
    assert response.status_code == 404

def test_download_malformed_id(client):
    response = client.get("/download/!@#$%^&*()")
    assert response.status_code in [400, 404]
