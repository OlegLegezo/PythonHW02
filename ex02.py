# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

# функции с мал букв! значения по умолчанию
def func1(a=4):
    # def func1(a: int, b: int) -> list(тайп хинтинг):
    my_list = [1]
    b = 2
    while len(my_list) < a:
        my_list.append(my_list[-1]*b)
        # .append позволяет добавлять элемент в конце списка, который уже существует
        b += 1
    print(my_list)
    return my_list


n = int(input('введите число N:'))
func1(n)
