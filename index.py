print('Тест программы\n')
print('Для получения номера разработчика, нажмите 1')
print('Для получения номера директора, нажмите 2\n')
while True:
    number = int(input('Введите код клиента: '))
    if number == 1:
        print('Номер разработчика: +7999-999-99-99')
	print('e-mail разработчика: novoklin@mail.ru')
        break
    elif number == 2:
        print('Номер диретора: +7888-888-88-88')
	print('e-mail Диретора: klin@mail.ru')
        break
    else:
        print('Неверные данные, попробуйте еще раз!\n')
	print('Номер тех. поддержки: 8-800-88-88')
