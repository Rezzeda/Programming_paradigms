numbers = [5, 2, 9, 1, 5, 6]
print(numbers)

# императивный стиль процедуры пузырьковой сортировки чисел в порядке убывания.
def bubble_sort_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

bubble_sort_imperative(numbers)
print(numbers)

# Декларативный стиль
def bubble_sort_declarative(numbers):
    return sorted(numbers, reverse=True)

sorted_numbers = bubble_sort_declarative(numbers)
print(sorted_numbers)
