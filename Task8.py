primer = input().split() # Считываем выражение и разбиваем его на список чисел и операций
my_list = [] # Создаем my_list для хранения чисел

for element in primer:
    if element.isdigit(): # Если элемент является числом
        my_list.append(int(element)) # То добавляем его в my_list
    else: # Если элемент является операцией, то выполняем ее над двумя последними числами в листе и записываем результат в my_list
        b = my_list.pop()
        a = my_list.pop()
        if element == '+':
            my_list.append(a + b) #Если эл-т это "+", то получаем пример a + b
        elif element == '-':
            my_list.append(a - b) #Если эл-т это "-", то получаем пример a - b
        elif element == '*':
            my_list.append(a * b) #Если эл-т это "*", то получаем пример a * b
        elif element == '//':
            my_list.append(a // b) #Если эл-т это "//", то получаем пример a // b

print(my_list.pop()) # Принтим результат выражения
