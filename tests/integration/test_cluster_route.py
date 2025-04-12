import os
import json
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_cluster_route_with_valid_file(client):
    # Assurez-vous que le fichier de test existe
    test_file = "remove_floor_sample.pcd"
    path_processed = os.path.join("uploads", "processed", test_file)
    if not os.path.exists(path_processed):
        pytest.skip("Fichier de test requis non trouvé dans uploads/processed.")

    response = client.get(f"/cluster/{test_file}")
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
    assert response.status_code == 404 or response.status_code == 500
    data = response.get_json()
    assert "error" in data
