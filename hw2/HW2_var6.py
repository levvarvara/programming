#Левченко Варвара, вариант 6
number = int(input("Введите число для посторения таблицы умножения: "))
if number > 0:
    for i in range(1,11):
        print(number, "*", i, "=", number*i)
elif number == 0:
    print("Введен нуль!")
else:
    print("Введено отрицательное число!")
