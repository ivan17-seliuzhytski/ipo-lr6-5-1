### Задание 1
# Написать программу, которая:
# - Создаёт список из 6 строк (строки определяются в коде, на ваш вкус).
# - Подсчитывает количество строк, содержащих букву `д`.
# - Использует циклы для подсчета.
list = ["Я", "Он", "Она дрожит", "Оно", "Ядерная пыль", "Я пыль"] # Создаем список строк.
count = 0 # Инициализируем переменную count, для подсчета строк содержащих букву 'д' в нашем списке.
for i in list: # Перебираем значение списка.
	d = 'д' # Инициализируем переменную letter.
	if d in i: # Проверка на содержание в строке буквы.
		count+=1 # Если есть буква 'д', тогда увеличиваем счетчик на 1.
print(f"Количество строк в которых содержится буква д: {count}") # Выводим на экран количество строк содержащих букву 'д'.