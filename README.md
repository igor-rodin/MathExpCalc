# MathExpCalc - простой телеграмм бот для вычисления основных арифметический действий с вещественными и комплексными числами

### Бот позволяет:

1. Обрабатывать произвольные выражения для вещественных чисел
2. Совершать основные действия с комплексными числами
3. Поддерживаемые операции: +, -, *, /

### Команды бота

1. ``` /start, /help ``` - показывает иформацию об используемых командах
2. ```/calc exp``` - вычисляет выражение _exp_ для вещественных чисел, пример выражения - ``` (2 + 4.2)*(1.5 - 3.6) + 6./(2. - 8.) ```  
3. ```/csum a b ``` - вычисляет сумму двух комплексных чисел ```a``` и  ```b```
4. ```/csub a b ``` - вычисляет разность двух комплексных чисел ```a``` и  ```b```
5. ```/cmul a b ``` - вычисляет произведение двух комплексных чисел ```a``` и  ```b```
6. ```/cdiv a b ``` - вычисляет частное двух комплексных чисел ```a``` и  ```b```
7. Комплексные числа записываются в формате ```(re +/- jim)```, _re_ - вещественная часть числа, _im_ - мнимая часть числа. Скобки обязательны когда присутствуют обе части числа, если мнимая или вещественная часть отсутствует, скобки можно опускать.  Примеры команд: ```'/сsum j (2-j4)'```, ```'/сmul (2.4 - j3.2) (1.2 + j4.5)'```, ```'/сdiv (2.4 - j3.2) -j2.2'```. 
  Так: ~~/сsum 1 - j  2 +j3~~  - неправильно

Модули программы:
* _main_ - Главный модуль программы. Стартовая точка запуска бота
* _calc_bot_ - Модуль, в котором происходит создание бота и инициалиация обработчиков команд
* _cmd\_handlers_ - Модуль, в котором содержатся обработчики команд бота
* _menu_ - Модуль c настройками меню команд 
* _math\_controller_ - Модуль, отвечающий за взаимодействие бота с математикой.
* _parser_ - Модуль, отвечающий за парсер вычисляемых выражений, поступающих от пользователя
* __const_ - Модуль с  глобальными константами
* __math\_calc_ - Модуль, отвечающий за математику. Состоит из трех подмодулей
  * _fmath_ - содержит операции с вещественными числами
  * _сmath_ - содержит операции с комплексными числами
  * _mathcommon_ - содержит функции, общие для _fmath_ и _cmath_
  