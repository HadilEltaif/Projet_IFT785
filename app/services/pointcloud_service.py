import json
import numpy as np
from app.factories.loader_factory import LoaderFactory
from app.services.file_service import FileService

class PointCloudService:

    @staticmethod
    def get_point_cloud_json(filepath):
        extension = filepath.rsplit(".", 1)[-1].lower()
        loader = LoaderFactory.get_loader(extension)
        pcd = loader.load(filepath)

        points = np.asarray(pcd.points)
        point_list = [{"x": float(p[0]), "y": float(p[1]), "z": float(p[2])} for p in points]
        return json.dumps(point_list)

