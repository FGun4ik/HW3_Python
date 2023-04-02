def can_eat(figure, horse): #Создаем функцию
    x_distance = abs(figure[0] - horse[0]) #Проверяем,может ли конь съесть другую фигуру
    y_distance = abs(figure[1] - horse[1]) #Проверяем,может ли конь съесть другую фигуру

#Конь может съесть фигуру если расстояние между их координатами по горизонтали равно 2, а по вертикали - 1, или наоборот.

    return (x_distance, y_distance) in [(1, 2), (2, 1)] #Проверяем разность координат и возвращаем функцию.


result = can_eat((5, 5), (6, 6))
print(result) #Вывод False

# result = can_eat((2, 1), (4, 2))
# print(result) #Вывод True
