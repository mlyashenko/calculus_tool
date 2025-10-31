import argparse
from .core import calc_limit, calc_derivative, calc_integral

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="calculus_tool",
        description="CLI для пределов, производных и интегралов",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    p_lim = sub.add_parser("limit", help="предел выражения")
    p_lim.add_argument("--expr", required=True, help="напр. 'sin(x)/x'")
    p_lim.add_argument("--var", default="x", help="переменная")
    p_lim.add_argument("--at", type=float, default=0.0, help="к чему стремится")
    p_lim.add_argument("--direction", choices=["+", "-", "both"], default="+",
                       help="направление предела")

    p_der = sub.add_parser("derivative", help="производная")
    p_der.add_argument("--expr", required=True, help="напр. 'x**3' или 'sin(x)'")
    p_der.add_argument("--var", default="x")
    p_der.add_argument("--order", type=int, default=1, help="порядок производной")

    p_int = sub.add_parser("integral", help="интеграл")
    p_int.add_argument("--expr", required=True, help="напр. 'sin(x)' или 'x'")
    p_int.add_argument("--var", default="x")
    p_int.add_argument("--a", type=float, default=None, help="нижний предел")
    p_int.add_argument("--b", type=float, default=None, help="верхний предел")

    sub.add_parser("demo", help="показать примеры вычислений")
    return p

def main(argv=None) -> int:
    p = build_parser()
    args = p.parse_args(argv)

    if args.cmd == "limit":
        print(calc_limit(args.expr, var=args.var, at=args.at, direction=args.direction)); return 0
    if args.cmd == "derivative":
        print(calc_derivative(args.expr, var=args.var, order=args.order)); return 0
    if args.cmd == "integral":
        print(calc_integral(args.expr, var=args.var, a=args.a, b=args.b)); return 0
    if args.cmd == "demo":
        print("limit sin(x)/x, x->0:");  print(calc_limit("sin(x)/x", at=0))
        print("\nderivative x**3, order 2:"); print(calc_derivative("x**3", order=2))
        print("\nintegral x from 0 to 1:");  print(calc_integral("x", a=0, b=1))
        return 0
    p.print_help(); return 1