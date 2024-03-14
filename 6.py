com_1, com_2 = map(int, input('Введите счет игры: ').split(":"))
if com_1 > com_2:
    print(1)
elif com_2 > com_1:
    print(2)
else:
    print(0)
