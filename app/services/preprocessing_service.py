import os
import open3d as o3d
import json
import numpy as np
from app.services.pointcloud_service import PointCloudService
from app.strategies.preprocessing_strategy import PreprocessingStrategy
from app.decorators.strategy_logger import StrategyLoggerDecorator
from app.strategies.remove_top_bottom import RemoveTopBottomStrategy
from app.strategies.remove_side_points import RemoveSidePointsStrategy
from app.strategies.remove_outliers import RemoveOutliersStrategy
from app.strategies.remove_floor import RemoveFloorStrategy
from app.strategies.downsampler import DownsamplerStrategy

class PreprocessingService:
    strategies = {
        "remove_top_bottom": StrategyLoggerDecorator(RemoveTopBottomStrategy()),
        "remove_side_points": StrategyLoggerDecorator(RemoveSidePointsStrategy()),
        "remove_outliers": StrategyLoggerDecorator(RemoveOutliersStrategy()),
        "remove_floor": StrategyLoggerDecorator(RemoveFloorStrategy()),
        "downsample": StrategyLoggerDecorator(DownsamplerStrategy()),
    }
    @staticmethod
    def load_point_cloud(file_path):
        return PointCloudService.load_point_cloud(file_path)

    @staticmethod
    def apply_strategy(pcd, strategy_name):
        strategy = PreprocessingService.strategies.get(strategy_name)
        if not strategy:
            raise ValueError(f"Unknown preprocessing step: {strategy_name}")
        return strategy.apply(pcd)

    @staticmethod
    def apply_step_and_save(file_path, strategy_name):
        # Load
        pcd = PreprocessingService.load_point_cloud(file_path)

        # Apply
        processed_pcd = PreprocessingService.apply_strategy(pcd, strategy_name)

        # Save
        processed_dir = os.path.join("uploads", "processed")
        os.makedirs(processed_dir, exist_ok=True)
        filename = os.path.basename(file_path)
        new_path = os.path.join(processed_dir, f"{strategy_name}_{filename}")
        o3d.io.write_point_cloud(new_path, processed_pcd)

        # Convert to JSON
        json_data = PointCloudService.pcd_to_json(processed_pcd)
        return json_data, new_path
