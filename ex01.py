# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

a = float(input('введите число a:'))
n = int(input('введите число знаков после запятой:'))
aPart1 = int(a)
# print("aPart1:", aPart1)
aPart2 = float(round((a-aPart1), n))
# aPart2 = 0.12321
# print("aPart2:", aPart2)

sum = int(0)
while aPart1 != 0:
    sum = int(aPart1 % 10+sum)
    aPart1 = aPart1/10
# print(f"Сумма до точки:", sum)

n = n-1
while aPart2 != 0:
    sum = int(aPart2*10+sum)
    # print(f"Сумма {n}:", sum)
    aPart2 = round(aPart2*10, n)
    # print(f"aPart2 {n}:", sum)
    aPart2 = round(aPart2-int(aPart2), n)
    # print(f"aPart2 {n}:", sum)
    n = n-1


print("Сумма цифр вещественного числа:", sum)
