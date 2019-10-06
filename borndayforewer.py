# Год и день рождения Пушкина

PUSHKIN_YEAR_OF_BIRTH = 1799
PUSHKIN_DAY_OF_BIRTH = 26

while True:
    year_str = input('Введите год рождения А.С.Пушкина: ')
    if year_str.isnumeric():
        year_numeric = int(year_str)
        if year_numeric == PUSHKIN_YEAR_OF_BIRTH:
            while True:
                day_str = input('Введите день рождения А.С.Пушкина: ')
                if day_str.isnumeric():
                    day_numeric = int(day_str)
                    if day_numeric == PUSHKIN_DAY_OF_BIRTH:
                        print('Верно')
                        break
                    else:
                        print('Неверный день рождения')
                else:
                    print('Это не число')
            break
        else:
            print('Неверный год рождения')
    else:
        print('Это не число')