'''number = int(input('Введите число от 1 до 20: '))

if number == 1: print(f'Вы ввели - {number} процент')
elif 2 <= number <= 4:
    print(f'Вы ввели - {number} процента')
elif 5 <= number <= 20:
    print(f'Вы ввели - {number} процентов')
else:
    print('Введите число в промежутке от 1 до 20.')
'''
#Вывод чисел от 1 до 20 со скланениями
numbers = [] #Создаём пустой список
for i in range(1,101): #Наполняем список с помошью цикла и функции range указав параметры начала и конца списка
    numbers.append(i)
    if i==1: print(f'{i} процент') #Проверяем условия
    elif 2<=i<=4: print(f'{i} процента')
    elif i>20 and (i%10)==1: print(f'{i} процент')
    elif 5<=i<=20: print(f'{i} процентов')
    elif i>20 and 2<=(i%10)<=4: print(f'{i} процента')
    elif i>20 and 5<=(i%10)<=9:print(f'{i} процентов')
    else: print(f'{i} процентов')