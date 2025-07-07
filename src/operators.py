from abc import ABC, abstractmethod
from typing import Any

from src.exceptions import CSVProcessorError


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
        except (ValueError, TypeError):
            return str(value) > str(target)


class LessThanOperator(FilterOperator):
    """Оператор сравнения меньше (<)."""

    def apply(self, value: Any, target: Any) -> bool:
        try:
            return float(value) < float(target)
        except (ValueError, TypeError):
            return str(value) < str(target)


class EqualOperator(FilterOperator):
    """Оператор сравнения равно (=)."""

    def apply(self, value: Any, target: Any) -> bool:
        try:
            return float(value) == float(target)
        except (ValueError, TypeError):
            return str(value) == str(target)


class OperatorFactory:
    """Фабрика операторов"""

    _operators = {
        "=": EqualOperator,
        ">": GreaterThanOperator,
        "<": LessThanOperator,
    }

    @classmethod
    def create_operator(cls, operator: str) -> FilterOperator:
        """Создание оператора по строковому представлению"""
        if operator not in cls._operators:
            raise CSVProcessorError(f"Неподдерживаемый оператор: {operator}")

        return cls._operators[operator]()

    @classmethod
    def get_supported_operators(cls) -> list[str]:
        """Получение списка поддерживаемых операторов"""
        return list(cls._operators.keys())
