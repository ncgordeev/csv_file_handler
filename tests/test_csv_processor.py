import pytest

from src.csv_processor import CSVProcessor
from src.exceptions import CSVProcessorError, InvalidColumnError


def test_csv_processor_init():
    """Тест инициализации"""
    processor = CSVProcessor("test.csv")
    assert str(processor.filepath) == "test.csv"
    assert processor.data == []
    assert processor.headers == []


def test_load_data(temp_csv_file):
    """Тест загрузки данных"""
    processor = CSVProcessor(temp_csv_file)
    processor.load_data()

    assert len(processor.data) == 4
    assert processor.headers == ["name", "brand", "price", "rating"]
    assert processor.data[0]["name"] == "iPhone 15 Pro"


def test_load_data_file_not_found():
    """Тест несуществующего файла"""
    processor = CSVProcessor("nonexistent.csv")
    with pytest.raises(CSVProcessorError, match="не найден"):
        processor.load_data()


def test_filter_data_equal(temp_csv_file):
    """Тест фильтрации по равенству"""
    processor = CSVProcessor(temp_csv_file)
    processor.load_data()

    filtered = processor.filter_data("brand", "=", "Xiaomi")
    assert len(filtered) == 2
    assert all(row["brand"] == "Xiaomi" for row in filtered)


def test_filter_data_invalid_column(temp_csv_file):
    """Тест несуществующей колонки"""
    processor = CSVProcessor(temp_csv_file)
    processor.load_data()

    with pytest.raises(InvalidColumnError):
        processor.filter_data("invalid", "=", "value")


def test_aggregate_data_avg(temp_numeric_file):
    """Тест агрегации среднего"""
    processor = CSVProcessor(temp_numeric_file)
    processor.load_data()

    result = processor.aggregate_data("quantity", "avg")
    assert result == 20.0  # (10+20+30)/3


def test_aggregate_data_invalid_column(temp_csv_file):
    """Тест агрегации несуществующей колонки"""
    processor = CSVProcessor(temp_csv_file)
    processor.load_data()

    with pytest.raises(InvalidColumnError):
        processor.aggregate_data("invalid", "avg")


def test_aggregate_data_non_numeric(temp_csv_file):
    """Тест агрегации нечисловой колонки"""
    processor = CSVProcessor(temp_csv_file)
    processor.load_data()

    with pytest.raises(CSVProcessorError, match="нечисловые значения"):
        processor.aggregate_data("name", "avg")
