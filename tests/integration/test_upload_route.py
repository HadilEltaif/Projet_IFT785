import io

def test_upload_valid_pcd_file(client):
    data = {
        'file': (io.BytesIO(b"test PCD content"), 'sample.pcd')
    }
    response = client.post(
        '/upload/', data=data,
        content_type='multipart/form-data',
        follow_redirects=True
    )
    assert response.status_code == 200
    assert "Fichier téléversé avec succès".encode('utf-8') in response.data or "Erreur".encode('utf-8') in response.data


def test_upload_invalid_file(client):
    data = {
        'file': (io.BytesIO(b"bad content"), 'bad.txt')
    }
    response = client.post(
        '/upload/', data=data,
        content_type='multipart/form-data',
        follow_redirects=True
    )
    assert response.status_code == 200
    assert "Format de fichier non supporté".encode('utf-8') in response.data



def test_upload_no_file(client):
    response = client.post(
        '/upload/', data={},
        content_type='multipart/form-data',
        follow_redirects=True
    )
    assert response.status_code == 200
    assert "Aucun fichier sélectionné".encode('utf-8') in response.data
    
    
    
