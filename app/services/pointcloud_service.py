import struct
import json
import open3d as o3d
import numpy as np
import os
class PointCloudService:
    @staticmethod
    def get_point_cloud_data(filepath):
        if filepath.endswith(('.pcd', '.ply', '.bin')):
            return PointCloudService._parse_with_open3d(filepath)
        else:
            raise ValueError("Unsupported file format")

    @staticmethod
    def _parse_with_open3d(filepath):
        pcd = o3d.io.read_point_cloud(filepath)
        points = [[float(p[0]), float(p[1]), float(p[2])] for p in pcd.points]
        return points

    @staticmethod
    def get_point_cloud_json(filepath):
        points = PointCloudService.get_point_cloud_data(filepath)
        return json.dumps(points)
    @staticmethod
    def load_point_cloud(filepath):
        return o3d.io.read_point_cloud(filepath)
    
    
    @staticmethod
    def pcd_to_json(pcd):
        """Convertit un nuage de points Open3D en JSON pour affichage Web"""
        points = np.asarray(pcd.points).tolist()
        return json.dumps({"points": points})
