# #todo: Модифицировать программу таким образом чтобы она выводила
# # приветствие "Hello", которое только что записали в файл text.txt

# f = open("text.txt", "w+t")
# f.write("Hello\n")
# # Ваше решение.

# f.close()

f = open("text.txt", "w+t")
f.write("Hello\n")

f.seek(0)

print(f.read().strip())

f.close()
