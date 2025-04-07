import pytest
import os
from app.services.pointcloud_service import PointCloudService

def test_pointcloud_service_ascii(tmp_path):
    content = b"""# .PCD v0.7 - Point Cloud Data file format
VERSION 0.7
FIELDS x y z
SIZE 4 4 4
TYPE F F F
COUNT 1 1 1
WIDTH 3
HEIGHT 1
VIEWPOINT 0 0 0 1 0 0 0
POINTS 3
DATA ascii
1.0 2.0 3.0
4.0 5.0 6.0
7.0 8.0 9.0
"""
    test_file = tmp_path / "test.pcd"
    test_file.write_bytes(content)

    result_json = PointCloudService.get_point_cloud_json(str(test_file))
    assert "[[1.0, 2.0, 3.0]" in result_json
    assert "9.0" in result_json

def test_invalid_file_path():
    result = PointCloudService.get_point_cloud_json("non_existent_file.pcd")
    assert result == "[]"

