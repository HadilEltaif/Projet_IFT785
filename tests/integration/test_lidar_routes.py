import os
import json
import pytest
from flask import url_for
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["UPLOAD_FOLDER"] = "uploads"
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"LiDAR" in response.data

def test_about_route(client):
    response = client.get('/about')
    assert response.status_code == 200

def test_contact_route(client):
    response = client.get('/contact')
    assert response.status_code == 200
    
# Test d’un fichier inexistant pour /api/points/<filename>
def test_get_points_not_found(client):
    response = client.get("/api/points/fichier_inexistant.pcd")
    assert response.status_code == 500 or response.status_code == 404
    assert b"error" in response.data

# Test /preprocess avec redirection suivie
def test_preprocess_route(client):
    response = client.get("/preprocess", follow_redirects=True)
    assert response.status_code == 200
    assert b"preprocess" in response.data or b"html" in response.data
    
def test_visualize_no_file(client):
    response = client.get("/visualize/")
    assert response.status_code == 200
    assert b"visualize" in response.data or b"html" in response.data

def test_preprocess_step_and_return_json_file_not_found(client):
    response = client.get("/preprocess_step_and_return_json/remove_floor/fichier_inexistant.pcd")
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data

def test_download_file_not_found(client):
    response = client.get("/download/fichier_inexistant.pcd")
    assert response.status_code == 404

def test_download_existing_file(client, tmp_path):
    from app.controllers import lidar_controller

    processed_dir = tmp_path / "processed"
    processed_dir.mkdir()
    (processed_dir / "result.pcd").write_text("dummy data")
    lidar_controller.PROCESSED_FOLDER = str(processed_dir)

    response = client.get("/download/result.pcd")
    assert response.status_code == 200


def test_uploaded_file_redirects(client, tmp_path):
    # Simuler un fichier temporaire dans processed/
    processed_dir = tmp_path / "processed"
    processed_dir.mkdir()
    (processed_dir / "mock.pcd").write_text("data")

    # Simuler l’environnement attendu
    from app.controllers import lidar_controller
    lidar_controller.UPLOAD_FOLDER = str(tmp_path)

    response = client.get("/uploads/mock.pcd")
    assert response.status_code == 200