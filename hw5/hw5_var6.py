numbers = []
i=0
while i < 7:
    numbers.append(int(input()))
    i+=1

with open("text.txt", "w", encoding="utf-8") as f:
    for n in numbers:
        if n>=0:
            for m in range(n):
                f.write("X")
            f.write("\n")
        else:
            f.write("\n")

with open("text.txt", encoding="utf-8") as f:
    text=f.read()

#print(text)
