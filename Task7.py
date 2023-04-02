word = input() #Вводим слово
index1 = word.find('f') #Ищем первое появление буквы f
index2 = word.rfind('f') #Ищем последнее появление буквы f
if index1 == index2 and index1 != -1: #Если буква f встречается только 1 раз, выводим ее индекс
    print(index1)
elif index1 != -1: #Если буква f встречается больше 1 раза, выводим её первый и последний индекс
    print(index1, index2)