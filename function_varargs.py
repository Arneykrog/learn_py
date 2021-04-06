def total(a = 5, *numbers, **phonebook):
	print('a', a)

	#проход по всем элементам кортежа
	for single_items in numbers:
		print('single_items', single_items)

	#проход по всем элементам словаря
	for first_part, second_part in phonebook.items():
		print(first_part, second_part)

print(total(10, 1, 2, 3, Jack = 1123, John = 2231, Inge = 1560))