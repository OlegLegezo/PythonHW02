# Задать список из N элементов, заполненных числами из промежутка [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции вводит пользователь через пробел

# функция для создания и печати списка
def listMinusPlusN(resultArr=[]):
    n = int(input(
        'Введите положительное число N, для отображения всего промежутка -N до N: '))
    # resultArr = []
    startValue = -n
    for i in range(-n, n+1):
        resultArr.append(startValue)
        startValue += 1
        # print(sum)
    print(resultArr)
    return(resultArr)


Arr = []
listMinusPlusN(Arr)

print('введите позиции через пробел')
m = list(map(int, input().split()))
# print(m)
# m=[0,1]

mul1 = 1
for i in m:
    mul1 = Arr[i]*mul1
    # print(mul1)

print(f'произведение элементов с перечисленных позиций: {mul1}')
