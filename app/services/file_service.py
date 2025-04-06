import os
from werkzeug.utils import secure_filename
from app.factories.loader_factory import LoaderFactory

ALLOWED_EXTENSIONS = {"pcd", "ply", "bin"}

class FileService:
    upload_folder = "uploads/"

    @staticmethod
    def allowed_file(filename):
        return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

    @staticmethod
    def save_file(file):
        filename = secure_filename(file.filename)
        path = os.path.join(FileService.upload_folder, filename)
        os.makedirs(FileService.upload_folder, exist_ok=True)
        file.save(path)
        return path

    @staticmethod
    def process_uploaded_file(file):
        if not FileService.allowed_file(file.filename):
            raise ValueError("Format de fichier non supporté.")

        filepath = FileService.save_file(file)

        loader = LoaderFactory.get_loader(filepath)
        data = loader.load(filepath)

        return data
