# Файл с общими утилитарными функциями

def is_bracket_valid(expr: str) -> bool:
    '''
    Функция проверяет корректность расположения скобок
    '''
    parity = 0
    for char in expr:
        if char == '(':
            parity += 1
        elif char == ')':
            parity -= 1
        else:
            pass
        if parity < 0:
            return False
    return parity == 0
