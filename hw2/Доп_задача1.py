summa = 0
count = 0
maxim = 0

number=input("Введите число: ")

if number != " ":
    minim = int(number)

    while number != " ":
        number = int(number)
        summa += number
        if number > maxim:
            maxim = number
        if number < minim:
            minim = number
        number = input("Введите число: ")
        count += 1

    print("Среднее арифметическое равно ", "%.2f" % (summa / count))
    print("Max: ", maxim)
    print("Min: ", minim)
else:
    print("Введен пробел!")
