import io
from unittest.mock import patch

import pytest

from main import main


def test_main_no_arguments(temp_csv_file):
    """Тест запуска без аргументов фильтрации/агрегации"""
    with patch("sys.argv", ["main.py", temp_csv_file]):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            main()
            assert "Укажите условие" in mock_stdout.getvalue()


def test_main_with_filter(temp_csv_file):
    """Тест запуска с фильтрацией"""
    with patch("sys.argv", ["main.py", temp_csv_file, "--where", "brand=Xiaomi"]):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            assert "Результаты фильтрации" in output


def test_main_file_not_found():
    """Тест с несуществующим файлом"""
    with patch("sys.argv", ["main.py", "nonexistent.csv", "--where", "brand=Apple"]):
        with patch("sys.stderr", new_callable=io.StringIO) as mock_stderr:
            with pytest.raises(SystemExit):
                main()
            assert "Ошибка" in mock_stderr.getvalue()


def test_main_invalid_condition(temp_csv_file):
    """Тест с некорректным условием"""
    with patch("sys.argv", ["main.py", temp_csv_file, "--where", "invalid_condition"]):
        with patch("sys.stderr", new_callable=io.StringIO) as mock_stderr:
            with pytest.raises(SystemExit):
                main()
            assert "Ошибка" in mock_stderr.getvalue()


def test_main_empty_filter_result(temp_csv_file):
    """Тест с пустым результатом фильтрации"""
    with patch("sys.argv", ["main.py", temp_csv_file, "--where", "brand=NonExistent"]):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            assert "Нет данных" in output
