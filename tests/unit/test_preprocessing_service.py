
import os
import pytest
from unittest.mock import patch, MagicMock
from app.services.preprocessing_service import PreprocessingService

@pytest.fixture
def dummy_point_cloud():
    mock_pcd = MagicMock()
    return mock_pcd

def test_apply_strategy_valid(dummy_point_cloud):
    strategy_name = "remove_floor"
    with patch.object(PreprocessingService.strategies[strategy_name], 'apply', return_value="processed_pcd") as mock_apply:
        result = PreprocessingService.apply_strategy(dummy_point_cloud, strategy_name)
        assert result == "processed_pcd"
        mock_apply.assert_called_once_with(dummy_point_cloud)

def test_apply_strategy_invalid(dummy_point_cloud):
    with pytest.raises(ValueError) as excinfo:
        PreprocessingService.apply_strategy(dummy_point_cloud, "invalid_strategy")
    assert "Unknown preprocessing step" in str(excinfo.value)

import os
from unittest.mock import patch

@patch("app.services.preprocessing_service.os.makedirs")
@patch("app.services.preprocessing_service.os.path.basename", return_value="file.pcd")
@patch("app.services.preprocessing_service.o3d.io.write_point_cloud")
@patch("app.services.preprocessing_service.PreprocessingService.apply_strategy")
@patch("app.services.preprocessing_service.PreprocessingService.load_point_cloud")
@patch("app.services.preprocessing_service.PointCloudService.pcd_to_json", return_value={"mock": "json"})
def test_apply_step_and_save(mock_json, mock_load, mock_apply, mock_write, mock_basename, mock_makedirs):
    mock_load.return_value = "loaded_pcd"
    mock_apply.return_value = "processed_pcd"
    
    json_result, new_path = PreprocessingService.apply_step_and_save("path/to/file.pcd", "remove_floor")

    mock_load.assert_called_once_with("path/to/file.pcd")
    mock_apply.assert_called_once_with("loaded_pcd", "remove_floor")
    mock_write.assert_called_once()
    mock_json.assert_called_once_with("processed_pcd")

    assert isinstance(json_result, dict)

    
    expected_path = os.path.join("uploads", "processed", "remove_floor_file.pcd")
    assert new_path.endswith(expected_path)
