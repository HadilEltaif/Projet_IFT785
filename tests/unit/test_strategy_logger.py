import numpy as np
import open3d as o3d
from app.decorators.strategy_logger import StrategyLoggerDecorator
from app.strategies.remove_outliers import RemoveOutliersStrategy

def test_strategy_logger_executes_and_logs(capfd):
    points = np.random.rand(100, 3)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)

    strategy = StrategyLoggerDecorator(RemoveOutliersStrategy())
    result = strategy.apply(pcd)

    out, _ = capfd.readouterr()
    assert "[LOG] Début de" in out
    assert "RemoveOutliersStrategy" in out
    assert "[LOG] Fin de" in out
    assert isinstance(result, o3d.geometry.PointCloud)
