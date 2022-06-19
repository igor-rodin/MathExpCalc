from collections import namedtuple

ComplexNumber = namedtuple('ComplexNumber', 're img')

# Операции с комплексными числамиб: +, -, *, /


def sum(a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
    return ComplexNumber(a.re + b.re, a.img + b.img)


def sub(a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
    return ComplexNumber(a.re - b.re, a.img - b.img)


def mul(a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
    return ComplexNumber(a.re*b.re - a.img*b.img, a.re * b.img + b.re * a.img)


def div(a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
    re = (a.re*b.re + a.img*b.img)/(b.re**2 + b.img**2)
    im = (b.re * a.img - a.re * b.img)/(b.re**2 + b.img**2)
    return ComplexNumber(re, im)

# Представление комплексного числа в виде строки


def comp_tostring(number: ComplexNumber) -> str:
    re = number.re
    im = number.img
    if re == 0 and im == 0:
        res = 0
    elif re == 0 and im in (-1, 1):
        res = "j" if im == 1 else "-j"
    elif re == 0:
        res = f"j{im}" if im > 0 else f"-j{abs(im)}"
    elif im == 0:
        res = f"{re}"
    elif im in (-1, 1):
        res = f"{re} + j" if im > 0 else f"{re} - j"
    else:
        res = f"{re} + j{im}" if im > 0 else f"{re} - j{abs(im)}"
    return res
