from app.services.file_service import FileService
from app.services.preprocessing_service import PreprocessingService
from app.services.pointcloud_service import PointCloudService
import json

class Command:
    def execute(self):
        raise NotImplementedError("execute() must be implemented in subclasses")


class UploadCommand(Command):
    def __init__(self, file):
        self.file = file

    def execute(self):
        return FileService.process_uploaded_file(self.file)


class PreprocessCommand(Command):
    def __init__(self, file_path, step):
        self.file_path = file_path
        self.step = step

    def execute(self):
        return PreprocessingService.apply_step_and_save(self.file_path, self.step)


class VisualizeCommand(Command):
    def __init__(self, file_path):
        self.file_path = file_path

    def execute(self):
        data_json = PointCloudService.get_point_cloud_json(self.file_path)
        return json.loads(data_json)
