# 1) Напишите программу, которая на входе получает имя пользователя,
# cохраняет его в переменную user_name и выводит строку  "Hello {user_name}!"
# 2) Напишите программу, которая на входе получает 2 числа, производит с
# ними арифметическую операцию(на ваше усмотрение), и выводит “Результат = {результат}”.


# 3) Напишите программу, чтобы вывести:

#   *********
#  *        *
#  *        *
#   *********

# 1
# user_name = input()
# print(f"Hello {user_name}!")

# 2
# num1 = int(input())
# num2 = int(input())
# print(f"Результат = {num1 + num2}")

# 3
# print('*********\n*       *\n*       *\n*********')

# print('resalt :', 1, 5, ".", sep=":", end="!"*5)
# print("resalt:",  pow(5, 3))  # 125
# print("resalt:",  round(5 / 3))
count = 0
word = 'HELLO PRIVvvvET !'
for i in word:
    if i == "v":
        count += 1
        print("yes")
print("Count", count)














