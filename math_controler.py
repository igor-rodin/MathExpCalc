from const import MathOper
from mathcalc.cmath import (ComplexNumber, sum, sub, div, mul, comp_tostring)
from mathcalc.fmath import evaluate
from parser import parse


def get_answer(expr: str) -> str:
    try:
        return str(evaluate(expr))
    except SyntaxError as err:
        return err.msg


def get_canswer(expr: str, math_oper: MathOper) -> str:

    try:
        left, right = parse(expr)
    except SyntaxError as err:
        return err.msg

    if math_oper == MathOper.SUM:
        res = sum(ComplexNumber(left[0], left[1]),
                  ComplexNumber(right[0], right[1]))
    elif math_oper == MathOper.SUB:
        res = sub(ComplexNumber(left[0], left[1]),
                  ComplexNumber(right[0], right[1]))
    elif math_oper == MathOper.MUL:
        res = mul(ComplexNumber(left[0], left[1]),
                  ComplexNumber(right[0], right[1]))
    elif math_oper == MathOper.DIV:
        res = div(ComplexNumber(left[0], left[1]),
                  ComplexNumber(right[0], right[1]))
    return comp_tostring(res)
