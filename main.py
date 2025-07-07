import argparse
import sys

from tabulate import tabulate

from src.csv_processor import CSVProcessor, parse_condition
from src.exceptions import CSVProcessorError


def main():
    """
    Основной скрипт программы.
    """
    parser = argparse.ArgumentParser(
        description="Обработка CSV файлов с фильтрацией и агрегацией данных."
    )
    parser.add_argument("file", help="Путь к CSV файлу")
    parser.add_argument(
        "--where", help="Условие фильтрации (например: price>100 или name=apple)"
    )
    parser.add_argument(
        "--aggregate", help="Условие агрегации (например: price=avg или rating=max)"
    )

    args = parser.parse_args()

    if not args.where and not args.aggregate:
        print("Укажите условие фильтрации (--where) или агрегации (--aggregate)")
        return

    try:
        processor = CSVProcessor(args.file)
        processor.load_data()

        if args.aggregate:
            # Агрегация данных
            column, operation = args.aggregate.split("=", 1)
            result = processor.aggregate_data(column.strip(), operation.strip())

            print(f"\nРезультат агрегации {operation.upper()}({column}): {result}")

        elif args.where:
            # Фильтрация данных
            column, operator, value = parse_condition(args.where)
            filtered_data = processor.filter_data(column, operator, value)

            if filtered_data:
                print(f"\nРезультаты фильтрации ({args.where}):")
                print(tabulate(filtered_data, headers="keys", tablefmt="grid"))
            else:
                print(f"\nНет данных, соответствующих условию: {args.where}")

    except CSVProcessorError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

    except Exception as e:
        print(f"Неожиданная ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
