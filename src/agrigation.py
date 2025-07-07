from abc import ABC, abstractmethod
from typing import List, Union

from src.exceptions import CSVProcessorError


class Aggregator(ABC):
    """Базовый класс для функции агрегации."""

    @abstractmethod
    def calculate(self, values: List[Union[int, float]]) -> Union[int, float]:
        """Метод расчета результатов функций агрегации."""
        pass


class AverageAggregator(Aggregator):
    """Среднее значение."""

    def calculate(self, values: List[Union[int, float]]) -> Union[int, float]:
        if not values:
            return 0
        return sum(values) / len(values)


class MinAggregator(Aggregator):
    """Минимальное значение."""

    def calculate(self, values: List[Union[int, float]]) -> Union[int, float]:
        if not values:
            return 0
        return min(values)


class MaxAggregator(Aggregator):
    """Максимальное значение."""

    def calculate(self, values: List[Union[int, float]]) -> Union[int, float]:
        if not values:
            return 0
        return max(values)


class AggregatorFactory:
    """Фабрика агрегаторов"""

    _aggregators = {
        "avg": AverageAggregator,
        "min": MinAggregator,
        "max": MaxAggregator,
    }

    @classmethod
    def create_aggregator(cls, operation: str) -> Aggregator:
        """Создание агрегатора по строковому представлению"""
        operation = operation.lower()
        if operation not in cls._aggregators:
            raise CSVProcessorError(f"Неподдерживаемая операция агрегации: {operation}")

        return cls._aggregators[operation]()

    @classmethod
    def get_supported_operations(cls) -> list[str]:
        """Получение списка поддерживаемых операций"""
        return list(cls._aggregators.keys())
