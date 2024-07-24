#  calc functions

"""
Provides simple math calculations on two input variables (as either float or int).

The module conatins the following functions: 

    - `add(a,b)` -- returns the sum of two numbers. 
    - `subtract(a,b)` -- returns the difference of two numbers. 
    - `multiply(a,b)` -- returns the product of two numbers. 
    - `divide(a,b)` -- returns the quotent of two numbers. 

Examples:
    >>> from calculator import calculations
    >>> calculations.add(4,2)
    6.0
    >>> calculations.multiply(2.0, 4.0)
    8.0
    >>> from calculator.calculations import divide
    >>> divide(4.0, 2)
    2.0

"""

def add(a:float|int, b:float|int) -> float:
    """
    Computes and returns the sum of two numbers.
    
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
        The quotent of the two inputs. 
    
    Raises:
        ZeroDivisionError: An error occurs when trying to divide by zero. 
    
    Examples:
        >>> divide(4, 2)
        2.0
        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero
    """

    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a/b) 