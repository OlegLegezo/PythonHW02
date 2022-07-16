# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


str1=str(input('введите число a:'))
# print(str1)
sum=0
for elem in str1:
    if elem.isdigit():
        sum = int(elem)+sum
        # print(elem)
print("Cумма цифр вещественного числа=" ,sum)

# print("Сумма цифр вещественного числа:", sum)
