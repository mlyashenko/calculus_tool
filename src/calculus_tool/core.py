from typing import Optional
import sympy as sp

def _sympify(expr: str):
    try:
        return sp.sympify(expr)
    except Exception as e:
        raise ValueError(f"Не удалось распарсить выражение: {expr}. Ошибка: {e}")

def calc_limit(expr: str, var: str = "x", at: Optional[float] = None, direction: str = "+") -> sp.Expr:
    """Вычисляет предел выражения expr при var -> at.
    direction: "+"/"-"/"both" (двусторонний). Если at=None — формальный объект предела.
    """
    x = sp.Symbol(var)
    f = _sympify(expr)
    if at is None:
        return sp.Limit(f, x)
    dir_map = {"+": "+", "-": "-", "both": None}
    return sp.limit(f, x, at, dir=dir_map.get(direction, "+"))

def calc_derivative(expr: str, var: str = "x", order: int = 1) -> sp.Expr:
    """Производная n-го порядка expr по var."""
    if order < 1:
        raise ValueError("order должен быть >= 1")
    x = sp.Symbol(var)
    f = _sympify(expr)
    return sp.diff(f, x, order)

def calc_integral(expr: str, var: str = "x", a: Optional[float] = None, b: Optional[float] = None) -> sp.Expr:
    """Неопределённый (если a,b не заданы) или определённый интеграл."""
    x = sp.Symbol(var)
    f = _sympify(expr)
    if a is None or b is None:
        return sp.integrate(f, x)
    return sp.integrate(f, (x, a, b))

# Для задания 9: текстовая оболочка с try/except
def derivative(expression: str, variable: str) -> str:
    """Calculate the derivative of a mathematical expression with respect to a given variable.
    Returns string representation or error message.
    """
    try:
        x = sp.Symbol(variable)
        f = sp.sympify(expression)
        d = sp.diff(f, x)
        return str(d)
    except Exception as e:
        return f"Error: {e}"