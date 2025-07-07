class CSVProcessorError(Exception):
    """Базовое исключение для CSV-процессора"""

    pass


class FileNotFoundError(CSVProcessorError):
    """Исключение для случая, когда файл не найден"""

    pass


class InvalidColumnError(CSVProcessorError):
    """Исключение для случая, когда указана несуществующая колонка"""

    pass


class InvalidOperatorError(CSVProcessorError):
    """Исключение для случая, когда указан неподдерживаемый оператор"""

    pass


class InvalidAggregationError(CSVProcessorError):
    """Исключение для случая, когда указана неподдерживаемая операция агрегации"""

    pass


class DataProcessingError(CSVProcessorError):
    """Исключение для ошибок обработки данных"""

    pass
