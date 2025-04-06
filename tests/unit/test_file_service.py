import os
import pytest
from app.services.file_service import FileService
from app.factories.loader_factory import LoaderFactory
from app.interfaces.loader_interface import ILoader

import pytest
from app.interfaces.loader_interface import ILoader

def test_loader_interface_not_implemented():
    # On crée une classe sans implémenter 'load'
    class DummyLoader(ILoader):
        pass

    # On vérifie que Python refuse de créer un objet
    with pytest.raises(TypeError):
        DummyLoader()


def test_loader_factory_invalid_extension():
    with pytest.raises(ValueError, match="Format non supporté"):
        LoaderFactory.get_loader("xyz")

def test_allowed_file_valid():
    assert FileService.allowed_file("sample.pcd") is True
    assert FileService.allowed_file("sample.ply") is True
    assert FileService.allowed_file("sample.bin") is True

def test_allowed_file_invalid():
    assert FileService.allowed_file("sample.txt") is False
    assert FileService.allowed_file("sample") is False
    assert FileService.allowed_file("") is False

def test_save_file(tmp_path):
    class FakeFile:
        filename = "test.pcd"
        def save(self, path):
            with open(path, 'w') as f:
                f.write("test content")

    file = FakeFile()
    FileService.upload_folder = tmp_path.as_posix()
    saved_path = FileService.save_file(file)

    assert os.path.exists(saved_path)
    with open(saved_path, "r") as f:
        assert f.read() == "test content"
