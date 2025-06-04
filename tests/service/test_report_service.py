import pytest
from unittest.mock import MagicMock
from services.report_service import ReportService

def test_export_without_strategy_raises():
    service = ReportService()
    with pytest.raises(Exception):
        service.export([], "out.csv")

def test_export_with_strategy():
    service = ReportService()
    mock_strategy = MagicMock()
    service.set_strategy(mock_strategy)
    service.export([{"x": 1}], "out.csv")
    mock_strategy.export.assert_called_once()
