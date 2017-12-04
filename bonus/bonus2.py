cels = int(input("Введите температуру в градусах Цельсия: "))
if cels != "":
    far = cels*9/5+32
    celv = 273.15 + cels
    print("По Кельвину: ",celv,"   По Фаренгейту: ",far)
else:
    print("ПУСТАЯ СТРОКА")
