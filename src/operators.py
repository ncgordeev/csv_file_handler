from abc import ABC, abstractmethod
from typing import Any


class FilterOperator(ABC):
    """Базовый класс для операторов фильтрации"""

    @abstractmethod
    def apply(self, value: Any, target: Any) -> bool:
        """Применить операцию фильтрации."""
        pass


class GreaterThanOperator(FilterOperator):
    """Оператор сравнения больше (>)."""

    def apply(self, value: Any, target: Any) -> bool:
        try:
            return float(value) > float(target)
        except(ValueError, TypeError):
            return str(value) > str(target)


class LessThanOperator(FilterOperator):
    """Оператор сравнения меньше (<)."""

    def apply(self, value: Any, target: Any) -> bool:
        try:
            return float(value) < float(target)
        except(ValueError, TypeError):
            return str(value) < str(target)

class EqualOperator(FilterOperator):
    """Оператор сравнения равно (=)."""

    def apply(self, value: Any, target: Any) -> bool:
        try:
            return float(value) == float(target)
        except(ValueError, TypeError):
            return str(value) == str(target)
