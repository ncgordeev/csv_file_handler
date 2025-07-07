# CSV File Handler

Обработчик CSV-файлов с возможностью фильтрации и агрегации данных.

## Запуск проекта

1. Установите зависимости:
```bash
poetry install
```

2. Запустите скрипт используя команды:
```bash
python main.py example.csv --where "brand=Xiaomi"
python main.py example.csv --aggregate "price=avg"
```

## Опциональные возможности скрипта:

```
options:
  --where WHERE                       Условие фильтрации (например: price>100)
  --aggregate AGGREGATE               Условие агрегации (например: price=avg)
```

## Архитектура

Скрипт использует модульную архитектуру с разделением ответственности:

**`CSVProcessor`** - основной класс, который загружает CSV файл в список словарей через стандартную библиотеку `csv.DictReader`. 
Все последующие операции происходят с этим списком.

**Фильтрация** реализована через паттерн Strategy с классами операторов (`EqualOperator`, `GreaterThanOperator`, `LessThanOperator`), 
которые создаются через фабрику `OperatorFactory`. 
Функция `parse_condition()` разбирает строку условия на компоненты.

**Агрегация** использует аналогичный подход с агрегаторами (`AverageAggregator`, `MinAggregator`, `MaxAggregator`) и фабрикой `AggregatorFactory`.

Поддерживаемые операции:
- Фильтрация: `=`, `>`, `<` (регистронезависимо для текста)
- Агрегация: `avg`, `min`, `max`

## Примеры использования

```bash
# Фильтрация телефонов Xiaomi
python main.py example.csv --where "brand=Xiaomi"

# Телефоны дороже $500
python main.py example.csv --where "price>500"

# Средняя цена всех телефонов
python main.py example.csv --aggregate "price=avg"
```

## Тестирование

```bash
pytest --cov=src --cov-report=term-missing
```

```
Name                   Stmts   Miss  Cover
------------------------------------------
src/__init__.py            0      0   100%
src/agrigation.py         30      0   100%
src/csv_processor.py      54      7    87%
src/exceptions.py         12      0   100%
src/operators.py          32      0   100%
------------------------------------------
TOTAL                    128      7    95%

```

# Контакты

[![Telegram](https://img.shields.io/badge/Telegram-blue?logo=telegram&logoColor=white&style=flat)](https://t.me/equals7)