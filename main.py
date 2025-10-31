#!/usr/bin/env python3
"""
ASCII-safe UI для calculus_tool:
- Производная (n-го порядка)
- Интеграл (неопределенный или определенный)
- Предел (односторонний/двусторонний)

Работает из корня проекта (добавляем src в sys.path).
"""

import os
import sys
from typing import Optional

# чтобы работало при запуске из корня проекта
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from calculus_tool.core import (
    derivative as drv_text,
    calc_derivative,
    calc_integral,
    calc_limit,
)

def ask(prompt: str, default: Optional[str] = None) -> str:
    s = input(f"{prompt}" + (f" [{default}]" if default is not None else "") + ": ").strip()
    return s if s else (default if default is not None else "")

def ask_float(prompt: str, default: Optional[float] = None) -> Optional[float]:
    s = ask(prompt, str(default) if default is not None else None)
    if s == "" and default is None:
        return None
    try:
        return float(s)
    except ValueError:
        print("Warning: not a number. Try again.")
        return ask_float(prompt, default)

def hr():
    print("-" * 50)

def ui_derivative():
    hr()
    print("PROIZVODNAYA")
    expr = ask("Vyrazhenie", "sin(x)")
    var = ask("Peremennaya", "x")
    order_str = ask("Poryadok proizvodnoi (celoe >= 1)", "1")
    try:
        order = int(order_str)
        if order < 1:
            raise ValueError
    except ValueError:
        print("Warning: order must be integer >= 1. Using 1.")
        order = 1
    try:
        res = calc_derivative(expr, var, order)
        print(f"d^{order}/{var}^{order} {expr} = {res}")
    except Exception as e:
        print(f"Error: {e}")

def ui_integral():
    hr()
    print("INTEGRAL")
    expr = ask("Vyrazhenie", "x")
    var = ask("Peremennaya", "x")
    a = ask_float("Nizhnii predel (Enter = neopr.)", None)
    b = ask_float("Verkhnii predel (Enter = neopr.)", None)
    try:
        res = calc_integral(expr, var, a, b)
        if a is None or b is None:
            print(f"int {expr} d{var} = {res}")
        else:
            print(f"int_[{a};{b}] {expr} d{var} = {res}")
    except Exception as e:
        print(f"Error: {e}")

def ui_limit():
    hr()
    print("PREDEL")
    expr = ask("Vyrazhenie", "sin(x)/x")
    var = ask("Peremennaya", "x")
    at = ask_float(f"K chemu stremitsya {var}", 0.0)
    direction = ask("Napravlenie (+ / - / both)", "+")
    if direction not in {"+", "-", "both"}:
        print("Warning: wrong direction. Using 'both'.")
        direction = "both"
    try:
        res = calc_limit(expr, var, at, direction)
        side = {"both": "", "+": " (sprava)", "-": " (sleva)"}[direction]
        print(f"lim {{ {var}->{at} }} {expr}{side} = {res}")
    except Exception as e:
        print(f"Error: {e}")

def main_loop():
    while True:
        hr()
        print("=== Calculus Tool ===")
        print("1) Proizvodnaya")
        print("2) Integral")
        print("3) Predel")
        print("4) Bystraya proizvodnaya (obolochka zadaniya 9)")
        print("0) Vyhod")
        choice = ask("Vybor", "1")
        if choice == "1":
            ui_derivative()
        elif choice == "2":
            ui_integral()
        elif choice == "3":
            ui_limit()
        elif choice == "4":
            hr()
            print("Fast derivative (safe wrapper)")
            expr = ask("Vyrazhenie", "exp(x**2)")
            var = ask("Peremennaya", "x")
            print(drv_text(expr, var))
        elif choice == "0":
            print("Poka!")
            break
        else:
            print("Warning: wrong menu item.")

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print("\nPoka!")