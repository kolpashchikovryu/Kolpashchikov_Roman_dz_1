numbers = [] #Создаём список

for i in range(1,1000,2): #Делаем перебор от 1 до 10 с шагом 2, что бы брать только нечётные числа
    numbers.append(i**3) #Добволяем к каждому из чисел возведение в куб
#print(numbers) #Выводим результат сформированного списка

sum_cube = []
for item in numbers: #Перебор элементов списка
    s = str(item) #Преобразовываем элемент списка numbers в строку
    list_sum_items = 0 #
    for j in range(len(s)): #Перебор элементов строки приобразованной из элементов items листа numbers
        list_sum_items += int(s[j]) #Сложение эдементов строки с приобразованием в цплочисленное число
    if list_sum_items % 7 == 0: #Проверка на деление без остатка суммы чисел числа.
        sum_cube.append(item) #Если сумма чисел из которых состоит элемент делится на 7 без остатка, то добовляем в новый список sum_cube
#print(sum_cube)
list_sum = 0
for h in sum_cube:
    list_sum += h
print(f'Сумма чисел из списка возведённых в куб, сумма цифр которых делится на 7 равна: {list_sum}')





numbers2 = []
for i in range(1,1000,2): #Делаем перебор от 1 до 10 с шагом 2, что бы брать только нечётные числа
    numbers2.append((i ** 3) + 17) #Добволяем к каждому из чисел возведение в куб
#print(numbers2) #Выводим результат сформированного списка

sum_cube_17=[]
for item in numbers2:
    str_list = str(item)
    list_sum_items = 0
    for j in range(len(str_list)):
        list_sum_items += int(str_list[j])
    if list_sum_items % 7 == 0:
        sum_cube_17.append(item)
#print(sum_cube_17)

list_sum = 0
for h in sum_cube_17:
    list_sum += h
print(f'Сумма чисел из списка возведённых в куб + 17, сумма цифр которых делится на 7 равна: {list_sum}')