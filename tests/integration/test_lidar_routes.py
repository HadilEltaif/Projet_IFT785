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

def test_preprocess_route(client):
    response = client.get('/preprocess')
    assert response.status_code == 200
    assert "Prétraitement".encode('utf-8') in response.data

def test_segment_route(client):
    response = client.get('/segment')
    assert response.status_code == 200
    assert "Segmentation".encode('utf-8') in response.data

def test_detect_route(client):
    response = client.get('/detect')
    assert response.status_code == 200
    assert "Détection".encode('utf-8') in response.data
