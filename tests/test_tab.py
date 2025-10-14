def test_create_tab(client):
    response = client.post("/tabs/", json={
        "public_id": "abc123",
        "title": "lineardescent",
        "filename": "riff.gp5",
        "instrument": "guitar",
        "genre": "metal"
    })
    assert response.status_code == 200
    assert response.json()["filename"] == "riff.gp5"
