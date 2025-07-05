from abc import ABC, abstractmethod
from typing import List, Union


class AggregationFunction(ABC):
    """Базовый класс для функции агрегации."""

    @abstractmethod
    def calculate(self, values: List[Union[int, float]]) -> Union[int, float]:
        """Метод расчета результатов функций агрегации."""
        pass


class AvgFunction(AggregationFunction):
    """Среднее значение."""

    def calculate(self, values: List[Union[int, float]]) -> Union[int, float]:
        if not values:
            return 0
        return sum(values) / len(values)


class MinFunction(AggregationFunction):
    """Минимальное значение."""

    def calculate(self, values: List[Union[int, float]]) -> Union[int, float]:
        if not values:
            return 0
        return min(values)


class MaxFunction(AggregationFunction):
    """Максимальное значение."""

    def calculate(self, values: List[Union[int, float]]) -> Union[int, float]:
        if not values:
            return 0
        return max(values)
