name = input('Здравствуйте! Как вас зовут?')
print(f'Очень приятно, {name}! Меня зовут Марк.')
age = int(input('Сколько вам лет?'))
if age < 80:
    old_age = 80 - age
    print(f'Да, {name}, я старше Вас на {old_age} лет.')
else:
    young_age = age - 80
    print(f'Да, {name}, Вы старше меня на {young_age} лет.')
hobby = input('Вам нравится программировать?')
if hobby == 'да':
    print('Превосходно! Уверен, у Вас получится написать множество полезных и хороших программ.')
else:
    print('Жаль, я думал, Вы сможете написать интересную программу для меня.')
