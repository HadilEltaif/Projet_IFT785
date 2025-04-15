import os
import pytest
from app import create_app

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "uploads")
PROCESSED_FOLDER = os.path.join(UPLOAD_FOLDER, "processed")
TEST_FILE_NAME = "remove_floor_1464001237.774877000.pcd"  # assure-toi qu'il existe

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_cluster_route_with_valid_file(client):
    #  Vérifie que le fichier de test est bien présent
    file_path = None
    for folder in [PROCESSED_FOLDER, UPLOAD_FOLDER]:
        path = os.path.join(folder, TEST_FILE_NAME)
        if os.path.exists(path):
            file_path = path
            break

    if not file_path:
        pytest.skip(f"Le fichier de test '{TEST_FILE_NAME}' est manquant dans uploads/ ou uploads/processed.")

    # Appelle la route /cluster/<filename>
    response = client.get(f"/cluster/{TEST_FILE_NAME}")
    assert response.status_code == 200

    data = response.get_json()
    assert "clusters" in data
    assert isinstance(data["clusters"], list)

    if data["clusters"]:
        cluster = data["clusters"][0]
        assert "points" in cluster
        assert "bbox" in cluster
        assert "min" in cluster["bbox"]
        assert "max" in cluster["bbox"]

def test_cluster_route_with_invalid_file(client):
    response = client.get("/cluster/fichier_inexistant.pcd")
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data
