import csv
import os
import tempfile

import pytest


@pytest.fixture
def sample_data():
    """Тестовые данные"""
    return [
        {"name": "iPhone 15 Pro", "brand": "Apple", "price": "999", "rating": "4.9"},
        {
            "name": "Galaxy S23 Ultra",
            "brand": "Samsung",
            "price": "1199",
            "rating": "4.8",
        },
        {"name": "Redmi Note 12", "brand": "Xiaomi", "price": "199", "rating": "4.6"},
        {"name": "Poco X5 Pro", "brand": "Xiaomi", "price": "299", "rating": "4.4"},
    ]


@pytest.fixture
def temp_csv_file(sample_data):
    """Временный CSV файл"""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".csv", delete=False, encoding="utf-8"
    ) as f:
        writer = csv.DictWriter(f, fieldnames=sample_data[0].keys())
        writer.writeheader()
        writer.writerows(sample_data)
        temp_file = f.name

    yield temp_file
    os.unlink(temp_file)


@pytest.fixture
def numeric_data():
    """Числовые данные для агрегации"""
    return [
        {"product": "A", "quantity": "10", "cost": "100.5"},
        {"product": "B", "quantity": "20", "cost": "200.0"},
        {"product": "C", "quantity": "30", "cost": "300.0"},
    ]


@pytest.fixture
def temp_numeric_file(numeric_data):
    """Временный CSV файл с числовыми данными"""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".csv", delete=False, encoding="utf-8"
    ) as f:
        writer = csv.DictWriter(f, fieldnames=numeric_data[0].keys())
        writer.writeheader()
        writer.writerows(numeric_data)
        temp_file = f.name

    yield temp_file
    os.unlink(temp_file)
