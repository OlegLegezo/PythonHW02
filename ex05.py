# Реализовать алгоритм перемешивания списка.

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


Arr1 = []
listMinusPlusN(Arr1)

Arr2 = Arr1.copy()
x = len(Arr1)-1
# print(x)

for i in Arr1:
    Arr2[x] = Arr1[i]
    x = x-1

print('математически перемешанный список:')
print(Arr2)

# list.reverse() можно еще использовать реверс
