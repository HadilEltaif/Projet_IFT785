import numpy as np
from app.utils.geometry_utils import compute_bounding_box

def test_compute_bounding_box_returns_dict():
    points = np.random.rand(5, 3)
    box = compute_bounding_box(points)
    assert "min" in box and "max" in box
