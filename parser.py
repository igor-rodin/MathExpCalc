# Модуль отвечает за разбор выражений из комплексных чисел

def parse_number(expr: str) -> tuple:
    is_int = True
    is_img = False
    sign = 1
    pos = 0
    num_idx = pos
    if expr[pos] == '-':
        pos += 1
        num_idx = pos
        sign = -1

    if expr[pos] == 'j':
        is_img = True
        pos += 1
        num_idx = pos
        if pos == len(expr):
            return (0, sign)

    while pos < len(expr) and expr[pos].isdigit():
        pos += 1
    if pos < len(expr) and expr[pos] == ".":
        is_int = False
        pos += 1
    while pos < len(expr) and expr[pos].isdigit():
        pos += 1

    complex_part = sign * int(expr[num_idx:pos]) if is_int else float(
        expr[num_idx:pos])

    return (0, complex_part) if is_img else (complex_part, 0)


def parse_2number(expr: str) -> tuple:
    expr_l = expr.split('j')
    if len(expr_l) == 1:
        re = int(expr_l[0]) if expr_l[0].find('.') == -1 else float(expr_l[0])
        return (re, 0)
    if len(expr_l[1]) == 0:
        img = 1
    else:
        img = int(expr_l[1]) if expr_l[1].find('.') == -1 else float(expr_l[1])
    if len(expr_l[0]) > 0 and expr_l[0][-1] == '-':
        img *= -1
    if len(expr_l[0]) < 2:
        re = 0
    else:
        re = int(expr_l[0][0:-1]) if expr_l[0].find('.') == - \
            1 else float(expr_l[0][0:-1])

    return (re, img)


def parse(expr: str) -> tuple:
    '''
    Функция распарсивает строку expr на левую и правую части.
    expr имеет вид: "(re_l + jimg_l) (re_r + jimg_r) | re_l (re_r + jimg_r) | jimg_l (re_r + jimg_r) 
                    | (re_l + jimg_l) re_r | (re_l + jimg_l) jimg_r | re_l/jimg_l re_r/jimg_r"
    re_l(r) и img_l(r) - вещественная и мнимая части комплексного числа.
    Возвращаемое выражение - ((re_l, im_l),(re_r, img_r)) 
    '''
    expr = expr.lower().strip()
    bracket_count = expr.count('(')
    if bracket_count == 0:
        expr_list = expr.split()
        if len(expr_list[0]) > 1 or len(expr_list[1]) > 1:
            raise SyntaxError("Некоректное выражение, пропущены скобки")
        left_part = parse_number(expr_list[0])
        right_part = parse_number(expr_list[1])
    elif bracket_count == 1:
        brack_pos = expr.find('(')
        expr = expr.split()
        if brack_pos == 0:
            right_part = parse_number(expr[-1])
            l_expr = "".join(expr[:-1])
            left_part = parse_2number(l_expr[1:-1])
        else:
            left_part = parse_number(expr[0])
            r_expr = "".join(expr[1:])
            right_part = parse_2number(r_expr[1:-1])
    elif bracket_count == 2:
        expr = "".join(expr.split())
        expr = expr.split(')(')
        left_part = parse_2number(expr[0][1:])
        right_part = parse_2number(expr[1][:-1])

    return (left_part, right_part)
