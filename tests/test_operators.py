import pytest

from src.exceptions import CSVProcessorError
from src.operators import (
    EqualOperator,
    GreaterThanOperator,
    LessThanOperator,
    OperatorFactory,
)


def test_equal_operator():
    """Тест оператора равенства"""
    op = EqualOperator()
    assert op.apply("100", "100") is True
    assert op.apply("apple", "APPLE") is True
    assert op.apply("100", "200") is False


def test_greater_than_operator():
    """Тест оператора больше"""
    op = GreaterThanOperator()
    assert op.apply("200", "100") is True
    assert op.apply("100", "200") is False
    assert op.apply("b", "a") is True  # строки


def test_less_than_operator():
    """Тест оператора меньше"""
    op = LessThanOperator()
    assert op.apply("100", "200") is True
    assert op.apply("200", "100") is False
    assert op.apply("a", "b") is True  # строки


def test_operator_factory():
    """Тест фабрики операторов"""
    assert isinstance(OperatorFactory.create_operator("="), EqualOperator)
    assert isinstance(OperatorFactory.create_operator(">"), GreaterThanOperator)
    assert isinstance(OperatorFactory.create_operator("<"), LessThanOperator)


def test_operator_factory_invalid():
    """Тест неподдерживаемого оператора"""
    with pytest.raises(CSVProcessorError):
        OperatorFactory.create_operator("!=")


def test_get_supported_operators():
    """Тест списка поддерживаемых операторов"""
    operators = OperatorFactory.get_supported_operators()
    assert "=" in operators
    assert ">" in operators
    assert "<" in operators
