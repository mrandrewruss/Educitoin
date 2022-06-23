# Задача 1. Тайны археологии
# Ирина работает археологом и недавно приехала с интересных раскопок.
# Там нашли древнюю глиняную табличку, на которой еле-еле видны числа 
# 114 12 14 10605 4907 450. 
# Ирина предположила, что это такой шифр и хочет использовать программу,
# которую использовали для расшифровки целой книги из таких чисел.
# Напишите программу,
# которая проверяет каждое число и выводит к каждому соответствующее сообщение.
# Число подходит, если оно чётное и не делится на 3.
for number in 114, 12, 14, 10605, 4907, 450:
  if (number % 2 == 0) and (number % 3 != 0):
    print(number, '- Число подходит')
  else:
    print(number, '- Число не подходит')

# =========================================================
# Задача 2. Должники
# Должники и законопослушные граждане хранятся в одной базе банка.
# Из этой базы нам выделяются по 10 человек, у каждого из которых есть свой номер.
# Правда, иногда база глючит и выдаёт нам отрицательный номер.
# А ещё по статистике, которую собрал наш МирПрогБанк, 
# каждый второй, кто в этом году брал кредит, не выплатил его вовремя.
# Пользователь вводит 10 чисел.
# Напишите программу,
# которая определяет, сколько из них являются одновременно четными и положительными.
summ = 0
for number in range(1,11):
  number = int(input('Введите число: '))
  if (number % 2 == 0) and (number > 0):
    #print(number, '- Число чётное и положительное')
    summ += 1
print(summ, '- чисел чётных и положительных')

# =========================================================
# Задача 3. Посчитай чужую зарплату...
# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.
# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев 
# и выводит на экран среднюю зарплату за год.
salary_per_year = 0
for month in range(1,13):
  monthly_salary = int(input(f'Введите з/п за {month} месяц - '))
  salary_per_year += monthly_salary
print('З/п за год =', salary_per_year)
print('Средняя з/п =', salary_per_year / 12)

# =========================================================
# Задача 4. С заботой о природе
contravention = 0
for sector in range(30,36):
  people = int(input(f'Людей в {sector}-м секторе: '))
  if people > 10:
    print('Нарушение! Слишком много людей в секторе!')
    contravention += 1
  else:
    print('Всё спокойно.')
print(contravention)

# =========================================================
# Задача 5. Факториал
# Мы всё ближе и ближе подбираемся к серьёзной математике.
# Одна из классических задач - задача на нахождение факториала числа.
# И в будущем мы с ней ещё встретимся.
# 
# Дано натуральное число N. Напишите программу, которая находит N! (N факториал)
# 
# Запись N! означает следующее:
# 
# N! = 1 * 2 * 3 * 4 * 5 * … * N
# 
# Пример:
# 
# Введите число: 5
# Факториал числа 5 равен 120
n = int(input('Ввелите число: '))
factorial = 1
for i in range(1, n+1):
  factorial *= i
  #print(factorial)
print(f'Факториал числа {n} равен {factorial}')

# =========================================================
# Задача 6. Успеваемость в классе
# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. 
# 
# Напишите программу, 
# которая получает список оценок - N чисел - и выводит на экран сообщение о том, 
# кого сегодня больше: отличников, хорошистов или троечников.
students = int(input('How many students: '))
five = 0
four = 0 
three = 0
for i in range(1, students+1):
  mark = int(input('What mark for '+str(i)+' student: '))
  if mark == 5:
    five += 1
  elif mark == 4:
    four += 1
  elif mark == 3:
    three += 1
print('fives -', five)
print('fours -', four)
print('threes -', three)

# =========================================================
# Задача 7. Отрезок
# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль 
# среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.
num_a = int(input('введите число a: '))
num_b = int(input('введите число b: '))
average = 0
count = 0
for step in range(num_a, num_b+1):
  if step % 3 == 0:
    average = average + step
    count += 1
    print(step)
print('среднее арифметическое равно: ', average / count)

# =========================================================
# Задача 8. Замечательные числа
# Напишите программу,
# которая находит и выводит все двузначные числа,
# которые равны утроенному произведению своих цифр.
# К таким относятся, например, 15 и 24.
for number in range(9, 99):
  last_number = number % 10
  first_number = number // 10
  #print(first_number, last_number)
  finding =  last_number * first_number * 3
  if finding == number:
    print(finding)

# =========================================================
# Задача 9. ...Теперь можно посчитать и свою
# Пока бухгалтер считала среднюю зарплату сотрудников,
# ей стало интересно, а не зря ли она работает столько времени на одном месте?
# Ей захотелось узнать, увеличивается ли её зарплата с каждым месяцем или нет.
# Пользователь вводит 10 чисел.
# Напишите программу, которая проверяет, упорядочены ли они по возрастанию.
previous_salary = 0
for month in range(1, 11):
  print('Месяц', month)
  salary = int(input('Введите размер зарплаты: '))
  if salary > previous_salary:
    res = 'Зарплата растёт!'
  else:
    res = 'Зарплаты упорядочены не по-возвратанию'
    break
  previous_salary = salary
print(res)

# =========================================================
# Задача 10. Пропавшая карточка
#Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
# 
# Вводится число N,
# далее еще N − 1 чисел: 
# номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.

N = int(input('Введите число: '))
first_summ = 0
second_summ = 0
for i in range (1, N + 1):
    first_summ += i
for x in range (N - 1):
    x = int(input('Введите число: '))
    second_summ += x
print(first_summ - second_summ)