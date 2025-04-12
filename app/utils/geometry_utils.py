# app/utils/geometry_utils.py

import numpy as np

def compute_bounding_box(cluster: np.ndarray):
    min_bounds = cluster.min(axis=0)
    max_bounds = cluster.max(axis=0)
    return {
        "min": min_bounds.tolist(),
        "max": max_bounds.tolist()
    }
