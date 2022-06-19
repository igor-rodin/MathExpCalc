from telegram import Update
from telegram.ext import CallbackContext
from const import MathOper
import math_controler as mc
from menu import create_menu


def start(update: Update, context: CallbackContext):
    welcome_msg = '''
                       * MathExpCalc \- простой бот 
  для вычисления основных арифметический действий с вещественными и комплексными числами*

          _* Бот позволяет:*_
  \- Обрабатывать произвольные выражения для вещественных чисел
  \- Совершать основные действия с комплексными числами
  \- Поддерживаемые операции: \+, \-, \*, \/
            _* Команды бота *_
  _/start, /help_ \- показывает это сообщение
  _/calc exp_ \- вычисляет выражение _exp_ для вещественных чисел, 
                  пример выражения: _\(2 \+ 5\)\*\(3 \- 6\) \+ 6/\(2 \- 8\)_  
  _/csum a b_ \- вычисляет сумму двух комплексных чисел _a_ и  _b_
  _/csub a b_ \- вычисляет разность двух комплексных чисел _a_ и  _b_
  _/cmul a b_ \- вычисляет произведение двух комплексных чисел _a_ и  _b_
  _/cdiv a b_ \- вычисляет частное двух комплексных чисел _a_ и  _b_  
  *Комплексные числа записываются в формате _\(re \+/\- jim\)_ * 
    _re_ \- вещественная часть числа, _im_ \- мнимая часть числа
    Скобки обязательны когда присутствуют обе части числа, 
    если мнимая или вещественная часть отсутствует, скобки можно опускать
  Примеры команд:
            _'/csum j \(2\-j4\)'_
            _'/cmul \(24 \- j32\) \(12 \+ j45\)'_
            _'/cdiv \(24 \- j32\) \-j22'_
    А так: ~/csum 1 \- j  2 \+j~  \- неправильно 
    '''
    comands = ['/help']
    menu = create_menu(comands)

    update.message.reply_text(
        text=welcome_msg, parse_mode='MarkdownV2', reply_markup=menu)


def calc(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    expr = "".join(context.args)

    if expr.lower().find('j') > -1:
        answer = "Для работы с комплексными числами смотри /help"
    answer = mc.get_answer(expr)

    context.bot.send_message(chat_id, text=answer)


def csum(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    expr = " ".join(context.args)
    answer = mc.get_canswer(expr, MathOper.SUM)

    context.bot.send_message(chat_id, text=answer)


def csub(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    expr = " ".join(context.args)
    answer = mc.get_canswer(expr, MathOper.SUB)

    context.bot.send_message(chat_id, text=answer)


def cmul(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    expr = " ".join(context.args)
    answer = mc.get_canswer(expr, MathOper.MUL)

    context.bot.send_message(chat_id, text=answer)


def cdiv(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    expr = " ".join(context.args)
    answer = mc.get_canswer(expr, MathOper.DIV)

    context.bot.send_message(chat_id, text=answer)
