from telegram.replykeyboardmarkup import ReplyKeyboardMarkup


def create_menu(comands: list) -> ReplyKeyboardMarkup:
    menu_layot = [comands]

    return ReplyKeyboardMarkup(menu_layot, resize_keyboard=True)
