# E -> T1 + E | T1 - E | T1
# T1 -> T2 *T1 | T2 / T1 | T2
# T2 -> -T3
# T3 ->  Num | (E)
# Num -> digit | empty
from mathcalc import mathcommon

cur_idx = 0


def skip_whitespaces(expr: str):
    '''
    Функция пропускает пробельные символы в разбираемом выражении
    '''
    global cur_idx
    while cur_idx < len(expr) and expr[cur_idx].isspace():
        cur_idx += 1


def get_number(expr: str):
    '''
    Функция распарсивает число в арифметическом выражении
    Результат float при наличии десятичной точки или int 
    '''
    global cur_idx
    is_int = True
    num_idx = cur_idx

    while cur_idx < len(expr) and expr[cur_idx].isdigit():
        cur_idx += 1
    if cur_idx < len(expr) and expr[cur_idx] == ".":
        is_int = False
        cur_idx += 1
    while cur_idx < len(expr) and expr[cur_idx].isdigit():
        cur_idx += 1

    return int(expr[num_idx:cur_idx]) if is_int else float(expr[num_idx:cur_idx])


def get_term_3(expr: str):
    '''
    Функция определяет наличие скобочных выражений
    '''
    global cur_idx
    skip_whitespaces(expr)

    if cur_idx > len(expr) - 1:
        return

    if expr[cur_idx] == "(":
        cur_idx += 1
        exp = get_expr(expr)
        skip_whitespaces(expr)
        if expr[cur_idx] == ")":
            cur_idx += 1
            return exp
        else:
            print("Не парные скобки")
            return

    return get_number(expr)


def get_term_2(expr: str):
    '''
    Функция определяет наличие унарного минуса
    '''
    global cur_idx
    skip_whitespaces(expr)

    if expr[cur_idx] == "-":
        cur_idx += 1
        return -get_term_3(expr)
    return get_term_3(expr)


def get_term_1(expr: str):
    '''
    Функция распарсивает операции '*', '/'
    '''
    global cur_idx
    skip_whitespaces(expr)

    term_2 = get_term_2(expr)
    if cur_idx > len(expr) - 1:
        return term_2

    skip_whitespaces(expr)
    if expr[cur_idx] == "*":
        cur_idx += 1
        return term_2 * get_term_1(expr)
    elif expr[cur_idx] == "/":
        cur_idx += 1
        return term_2 / get_term_1(expr)

    return term_2


def get_expr(expr: str):
    '''
    Функция распарсивает операции '+', '-'
    '''
    global cur_idx
    skip_whitespaces(expr)

    term_1 = get_term_1(expr)
    if cur_idx > len(expr) - 1:
        return term_1

    skip_whitespaces(expr)

    if expr[cur_idx] == "+":
        cur_idx += 1
        return term_1 + get_expr(expr)
    elif expr[cur_idx] == "-":
        cur_idx += 1
        return term_1 - get_expr(expr)

    return term_1


def evaluate(expr: str):
    '''
    Основная функция для парсинга арифметического выражения
    '''
    global cur_idx
    if expr is None or len(expr) == 0:
        raise SyntaxError("Пустое выражение")
    else:
        if mathcommon.is_bracket_valid(expr):
            answer = get_expr(expr)
            cur_idx = 0
            return answer
        else:
            raise SyntaxError("Не соответствие закрытых и открытых скобок")
