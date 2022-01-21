# tochnocursovaya
Использование REPL
PyCharm поддерживает консоль Python в которой можно писать код:
![image](https://user-images.githubusercontent.com/90445300/149093026-368a4f68-d5f7-4d34-838e-5835b2045a67.png)
это был пройден первый модуль второй урок

Использование оператора Python
Python поддерживает интерактивную консоль, в которой можно вводить команды и немедленно видеть результат.
![image](https://user-images.githubusercontent.com/90445300/149491778-6d0de152-72b3-44d1-b565-9841018417e1.png)

Объявление и вывод переменных
Пока запущена программа REPL, создадим переменные.
![image](https://user-images.githubusercontent.com/90445300/149492386-323d2d2b-836d-4ef0-bced-aef1d8a41c77.png)
это был пройден первый модуль четвёртый урок

Чтение данных, вводимых с клавиатуры
Для чтения данных, вводимых с клавиатуры, в Python имеется функция input(). Функция input() считывает клавиши, вводимые пользователем на клавиатуре, и возвращает их в виде строки.
![image](https://user-images.githubusercontent.com/90445300/149907732-0597cde9-1507-4e01-8aea-614229fbe4d6.png)
Строка, передаваемая в качестве аргумента функции input, представляет собой запрос, выводимый пользователю.
Функцию input можно также вызвать без параметра:
![image](https://user-images.githubusercontent.com/90445300/149908080-e147e733-fecf-463c-969d-af501b03a6f3.png)
Эта программа выполняется почти так же, как первая. Разница в том, что функция print (по умолчанию) добавляет в выходные данные символ новой строки.

Считывание вводимых чисел
Функция input всегда возвращает вводимые значения как строки (текст). Это разумно, так как пользователь может ввести любой набор символов. Даже если введенное значение является числом, оно возвращается из функции input как строка.
![image](https://user-images.githubusercontent.com/90445300/149909223-e7c22960-7313-485d-ad06-afed0d8e2ff4.png)
Если выполнить этот код и ввести значение "7", на экране отобразится <class 'str'>, несмотря на то, что введено числовое значение. Чтобы преобразовать значение в целочисленную переменную, можно воспользоваться функцией int():
![image](https://user-images.githubusercontent.com/90445300/149909495-9dbdeb03-8aab-4a77-994b-510e976b8a30.png)
Этот код выводит <class 'int'> для значения 7. Если в значении может быть дробная часть, можно использовать функцию float аналогичным образом.

Преобразование чисел в строки
Можно делать и наоборот. Метод str() принимает целое число или число с плавающей запятой и преобразует его в строку.
![image](https://user-images.githubusercontent.com/90445300/149909843-c78e4f35-cbd9-48b8-967e-0f1208d325fb.png)
Это был пройден первый модуль 5 урок

Упражнение. Создание калькулятора
В этом упражнении мы используем полученные в модуле знания для создания калькулятора
запускаем программу REPL, введя python
![image](https://user-images.githubusercontent.com/90445300/149912474-0252e695-91b7-473f-83da-facd9988d0a1.png)
создадим операцию сложения
![image](https://user-images.githubusercontent.com/90445300/149915816-b274a2aa-46b4-411f-8e9e-b152b19fa3ac.png)
Символы ;\ в конце первых двух инструкций информируют о наличии множества строк кода и позволяют вводить их все построчно.
программа предлагает нам ввести слагаемые, вводим слагаемые 2 и 3, нажимаем Enter, программа выдаёт нам результат 5
![image](https://user-images.githubusercontent.com/90445300/149916654-9c8c690f-3d34-4097-bdc3-4db959d479be.png)
мы создали программу-калькулятор

Итоги
мы создали и запустили свою первую программу на Python


Объектно-ориентированное программирование на языке Python
Добавление и инициализация атрибутов в классе
посмотрим пример настройки атрибутов в конструкторе:
В предыдущем примере описывается класс Elevator с двумя переменными, make и floor. Важно понять, что __init__() вызывается неявно. Вы не вызываете метод __init__() по имени. Он вызывается при создании объекта в следующей строке кода
![image](https://user-images.githubusercontent.com/90445300/150093829-ef0ec73c-f0a2-41c0-9fcf-32e859e868be.png)

Неправильное использование self
Чтобы понять, как работает ключевое слово self, рассмотрим следующий код, в котором два атрибута, color и make, назначаются в конструкторе __init__():
![image](https://user-images.githubusercontent.com/90445300/150491508-d6f27f67-0c04-4d57-b580-c4c517207e84.png)
это был пройден 2 модуль 3 урок


Упражнение. Моделирование и создание игры
Создание классов и состояния
Создаём файл rock-paper-scissor.py и открываем редактор
Присваиваем ему следующее содержимое и сохраняем файл
![image](https://user-images.githubusercontent.com/90445300/150504878-85ea2c0a-2154-4b9f-8e99-cdbb27e0a6ef.png)
У нас есть необходимые классы, созданные для игры. Теперь необходимо подумать о том, какие данные у нас есть и в какой класс их нужно разместить.
![image](https://user-images.githubusercontent.com/90445300/150505289-4fa9e34e-9566-457b-9b23-79a076dfc21d.png)
Классу Participant были присвоены атрибуты points и choice, как указано в первой и третьей строке таблицы.
Для Game присвоены поля endGame, как указано в четвертой строке. Кроме того, у класса Game есть два участника: participant и secondParticipant.
