import csv
from pathlib import Path
from typing import Any, Dict, List

from src.agrigation import AggregatorFactory
from src.exceptions import (
    CSVProcessorError,
    DataProcessingError,
    InvalidColumnError,
    InvalidOperatorError,
)
from src.operators import OperatorFactory


class CSVProcessor:
    """
    Основной класс для обработки CSV файлов.
    """

    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.data: List[Dict[str, Any]] = []
        self.headers: List[str] = []

    def load_data(self) -> None:
        """
        Загрузка данных из CSV файла.
        """
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.headers = reader.fieldnames or []
                self.data = list(reader)
        except FileNotFoundError:
            raise CSVProcessorError(f"Файл {self.filepath} не найден")
        except Exception as e:
            raise CSVProcessorError(f"Ошибка при чтении файла: {e}")

    def filter_data(
        self, column: str, operator: str, value: str
    ) -> List[Dict[str, Any]]:
        """
        Фильтрация данных по условию.
        """
        if column not in self.headers:
            raise InvalidColumnError(f"Колонка '{column}' не найдена в файле")

        filter_operator = OperatorFactory.create_operator(operator)
        filtered_data = []

        for row in self.data:
            try:
                if filter_operator.apply(row[column], value):
                    filtered_data.append(row)
            except Exception as e:
                raise DataProcessingError(f"Ошибка при фильтрации: {e}")

        return filtered_data

    def aggregate_data(self, column: str, operation: str) -> float:
        """
        Агрегация данных по колонке.
        """
        if column not in self.headers:
            raise InvalidColumnError(f"Колонка '{column}' не найдена в файле")

        aggregator = AggregatorFactory.create_aggregator(operation)

        try:
            values = [float(row[column]) for row in self.data if row[column]]
            if not values:
                raise CSVProcessorError(f"Нет числовых значений в колонке '{column}'")

            return aggregator.calculate(values)
        except ValueError:
            raise CSVProcessorError(f"Колонка '{column}' содержит нечисловые значения")
        except Exception as e:
            raise DataProcessingError(f"Ошибка при агрегации: {e}")


def parse_condition(condition: str) -> tuple[str, str, str]:
    """Парсинг условия вида 'column=value' или 'column>value' и т.д."""
    operators = [">", "<", "="]

    for op in operators:
        if op in condition:
            parts = condition.split(op, 1)
            if len(parts) == 2:
                return parts[0].strip(), op, parts[1].strip()

    raise InvalidOperatorError(f"Неверный формат условия: {condition}")
