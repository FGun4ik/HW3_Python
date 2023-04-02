def s4et_pairs(my_list): #Создаем функцию, где в роли аргумента будет наш список
    pairs = 0 #СОздаем переменную pairs, в которой дальше будем хранить кол-во пар элементов
    for num in set(my_list): #В цикле for проходим по уникальным элементам списка, которые можно получить с помощью 'set()'
        formula = my_list.count(num) * (my_list.count(num) - 1) // 2 #Вычисляем кол-во его повторений с помощью 'count', затем вычисляем кол-во пар элементов раных друг другу
        pairs += formula #Добавляем кол-во возможных пар эоементов к переменной pairs
    return pairs #Возвращаем значение переменной из функции


my_list = [1, 2, 3, 2, 3]
pairs = s4et_pairs(my_list)
print(pairs)

my_list = [1, 1, 1, 1, 1]
pairs = s4et_pairs(my_list)
print(pairs)