# Год рождения Пушкина

PUSHKIN_YEAR_OF_BIRTH = 1799

while True:
    year_str = input('Введите год рождения А.С.Пушкина: ')
    if year_str.isnumeric():
        year_numeric = int(year_str)
        if year_numeric == PUSHKIN_YEAR_OF_BIRTH:
            print('Верно')
            break
        else:
            print('Неверно')
    else:
     print('Это не число')