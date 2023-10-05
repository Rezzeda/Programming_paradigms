# На вход подается число n.
# Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.

def generate_multiplication_table(n):
    table = []
    for i in range(1, n + 1):
        for j in range(1, 10):
            result = i * j
            table.append((i, j, result))
    return table

def display_table(table):
    for row in table:
        print(f"{row[0]} * {row[1]} = {row[2]}")

def main():
    n = int(input("Введите число n: "))
    multiplication_table = generate_multiplication_table(n)
    display_table(multiplication_table)

if __name__ == "__main__":
    main()

# Обоснование выбора процедурной парадигмы:
# Процедурная парадигма программирования организует код вокруг процедур (функций), которые выполняют определенные задачи.
# Простота организации: функции объединяются по задачам (генерация таблицы, отображение таблицы), что делает код понятным.
# Процедурный код выполняется от начала до конца, что соответствует естественному порядку выполнения задачи.
# Такой код легко читаем и обслуживаем, особенно для простых задач.