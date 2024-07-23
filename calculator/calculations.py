#  calc functions

"""
Takes two numbers and an operator then returns a float value result.
Args:
    a, b 
"""

def add(a:float|int, b:float|int) -> float:
    """
    Compute and return the sum of two numbers.
    
    Args:
    a : the first operand
    b : the second operand
    
    Returns:
    The sum of the two inputs. 

    Examples:
    >>> add(4, 2)
    6.0
    >>> add(4.0, 2.0)
    6.0
    """
    
    return float(a+b) 

def subtract(a:float|int, b:float|int) -> float:
    """
    Compute and return the difference of two numbers.
    
    Args:
    a : the first operand
    b : the second operand
    
    Returns:
    The difference between the first and second input. 
    
    Examples: 
    >>> subtract(4, 2)
    2.0
    >>> subtract(4.0, 2.0)
    2.0
    """
    return float(a-b) 

def multiply(a:float|int, b:float|int) -> float:
    """
    Compute and return the product of two numbers.
    
    Args:
    a : the first operand
    b : the second operand
    
    Returns:
    The product of the two inputs. 

    Examples: 
    >>> multiply(4, 2)
    8.0
    >>> multiply(4.0, 2.0)
    8.0
    """
    return float(a*b) 

def divide(a:float|int, b:float|int) -> float:
    """
    Compute and return the quotient of two numbers.
    
    Args:
    a : the first operand (numerator)
    b : the second operand (divisor)
    
    Returns:
    The sum of the two inputs. 
    
    Raises:
    ZeroDivisionError: Division by zero is not allowed!
    
    Examples:
    >>> divide(4, 2)
    2.0
    >>> divide(4.0, 2.0)
    2.0
    # >>> divide(4, 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero
    """
    
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed!")
    return float(a/b) 