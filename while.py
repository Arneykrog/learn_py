number = 21
running = True

while running:
	gues = int(input('Введите целое число: '))

	if gues == number:
		print('Поздравляю, вы угадали!')
		running = False # Это останавливает цикл while
	elif gues < number:
		print('Нет, загаданное число немного больше этого.')
	else:
		print('Нет, загаданное число немного меньше этого.')
else:
	print('Цикл while закончен.')
	#Здесь можно выполнить всё что ещё угодно
print('Завершение.')