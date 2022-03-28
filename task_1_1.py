# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах.
duration = int(input('Введите размер отрезка времени в секундах: '))
#print(duration)

#Дни
duration_days = duration // (3600 * 24)
#print(f'{duration_days} д.')
#Часы
duration_hour = (duration % (3600 * 24)) // 3600
#print(f'{duration_hour} ч.')
#Минуты
duration_min = ((duration % (3600 * 24)) % 3600) // 60
#print(f'{duration_min} мин.')
#Секунды
duration_sec = duration % 60
#print(f'{duration_sec} сек.')

#Общий вывод
#print(f'В введённом отрезке времени: {duration_days} д., {duration_hour} ч., {duration_min} мин., {duration_sec} сек.')

#решение задания
if (duration_days or duration_hour or duration_min) == 0:
    print(f'В введённом отрезке времени: {duration_sec} сек.')
elif (duration_days or duration_hour) == 0:
    print(f'В введённом отрезке времени: {duration_min} мин., {duration_sec} сек.')
elif duration_days == 0:
    print(f'В введённом отрезке времени: {duration_hour} ч., {duration_min} мин., {duration_sec} сек.')
else:
    print(f'В введённом отрезке времени: {duration_days} д., {duration_hour} ч., {duration_min} мин., {duration_sec} сек.')