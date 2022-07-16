# Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму

n = int(input('Введите число, для отображения суммы из последовательности: '))
resultArr = []
sum = 0
for i in range(1, n+1):
    resultArr.append(round((1 + 1/i)**i,2))
    sum = resultArr[i-1]+sum
    # print(sum)

print(resultArr)
print(f'сумма: {round(sum,2)}')
