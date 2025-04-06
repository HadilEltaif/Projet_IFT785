from app.interfaces.loader_interface import ILoader
import open3d as o3d
import numpy as np

class PCDLoader(ILoader):
    def load(self, filepath):
        pcd = o3d.io.read_point_cloud(filepath)
        return np.asarray(pcd.points)
