
import pytest
from unittest.mock import MagicMock
from app.strategies.preprocessing_strategy import PreprocessingPipeline, PreprocessingStrategy

class DummyStrategy(PreprocessingStrategy):
    def apply(self, pcd):
        return [[x + 1 for x in point] for point in pcd]

def test_preprocessing_pipeline_applies_all_strategies():
    # Arrange
    pcd_input = [[1, 2, 3], [4, 5, 6]]
    strategies = [DummyStrategy(), DummyStrategy()]
    pipeline = PreprocessingPipeline(strategies)

    # Act
    result = pipeline.run(pcd_input)

    # Assert
    assert result == [[3, 4, 5], [6, 7, 8]]

def test_strategy_interface_raises_if_not_implemented():
    with pytest.raises(NotImplementedError):
        PreprocessingStrategy().apply([[0, 0, 0]])
