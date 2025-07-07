import pytest

from src.agrigation import (
    AggregatorFactory,
    AverageAggregator,
    MaxAggregator,
    MinAggregator,
)
from src.exceptions import CSVProcessorError


def test_average_aggregator():
    """Тест агрегатора среднего"""
    agg = AverageAggregator()
    assert agg.calculate([1, 2, 3, 4, 5]) == 3.0
    assert agg.calculate([]) == 0


def test_min_aggregator():
    """Тест агрегатора минимума"""
    agg = MinAggregator()
    assert agg.calculate([1, 2, 3, 4, 5]) == 1
    assert agg.calculate([]) == 0


def test_max_aggregator():
    """Тест агрегатора максимума"""
    agg = MaxAggregator()
    assert agg.calculate([1, 2, 3, 4, 5]) == 5
    assert agg.calculate([]) == 0


def test_aggregator_factory():
    """Тест фабрики агрегаторов"""
    assert isinstance(AggregatorFactory.create_aggregator("avg"), AverageAggregator)
    assert isinstance(AggregatorFactory.create_aggregator("min"), MinAggregator)
    assert isinstance(AggregatorFactory.create_aggregator("max"), MaxAggregator)


def test_aggregator_factory_case_insensitive():
    """Тест регистронезависимости фабрики"""
    assert isinstance(AggregatorFactory.create_aggregator("AVG"), AverageAggregator)
    assert isinstance(AggregatorFactory.create_aggregator("Min"), MinAggregator)


def test_aggregator_factory_invalid():
    """Тест неподдерживаемой операции"""
    with pytest.raises(CSVProcessorError):
        AggregatorFactory.create_aggregator("median")


def test_get_supported_operations():
    """Тест списка поддерживаемых операций"""
    operations = AggregatorFactory.get_supported_operations()
    assert "avg" in operations
    assert "min" in operations
    assert "max" in operations
