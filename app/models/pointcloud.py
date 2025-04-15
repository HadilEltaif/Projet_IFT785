
import numpy as np

class PointCloud:
    def __init__(self, points: np.ndarray):
        self.points = points  # shape: (N, 3) ou (N, 4) avec intensité

    @classmethod
    def from_array(cls, array: np.ndarray):
        return cls(array)

    def to_array(self) -> np.ndarray:
        return self.points

    def __len__(self):
        return len(self.points)

    def __str__(self):
        return f"PointCloud with {len(self.points)} points"
