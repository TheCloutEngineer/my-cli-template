"""
Calculator module for my-cli-template.
"""


def add(a: float, b: float) -> float:
    """
    Return the sum of two numbers.
    :param a:
    :param b:
    :return: Float
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Return the difference of two numbers.
    :param a:
    :param b:
    :return: Float
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Return the product of two numbers.
    :param a:
    :param b:
    :return: Float
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Return the quotient of two numbers.
    :param a:
    :param b:
    :return: Float
    :raises ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a: float, b: float) -> float:
    """
    Return a raised to the power of b.
    :param a:
    :param b:
    :return: Float
    """
    return a ** b
