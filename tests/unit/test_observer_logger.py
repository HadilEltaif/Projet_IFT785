
from app.observers.observer import PreprocessingNotifier, LoggerObserver
from unittest.mock import MagicMock

def test_logger_observer_receives_notification(capsys):
    # Arrange
    observer = LoggerObserver()
    notifier = PreprocessingNotifier()
    notifier.attach(observer)

    # Act
    notifier.notify("Test: Étape appliquée")

    # Assert (capture la sortie console)
    captured = capsys.readouterr()
    assert "Test: Étape appliquée" in captured.out
