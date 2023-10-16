# Написать программу на любом языке в любой парадигме для бинарного поиска.
# На вход подаётся целочисленный массив и число.
# На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Найден искомый элемент, возвращаем индекс
        elif arr[mid] < target:
            left = mid + 1  # Искомый элемент справа от середины
        else:
            right = mid - 1  # Искомый элемент слева от середины

    return -1  # Если элемент не найден

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10

result = binary_search(arr, target)

if result != -1:
    print(f"Элемент {target} найден по индексу {result}.")
else:
    print(f"Элемент {target} не найден в массиве.")
