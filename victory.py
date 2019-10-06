# насколько я понял пока не выпендриваться и списки, функции или всякую панду не использовать

# Константы
PUSHKIN_YEAR_OF_BIRTH = 1799
PUTIN_YEAR_OF_BIRTH = 1952
LENIN_YEAR_OF_BIRTH = 1870
CHEGUEVARA_YEAR_OF_BIRTH = 1928
STOLYPIN_YEAR_OF_BIRTH = 1862
AMOUNT_QUESTION = 5


while True:
    # Метки ответов, для последующих посказок
    pushkin_year_true = False
    putin_year_true = False
    lenin_year_true = False
    cheguevara_year_true = False
    stolypin_year_true = False

    true_answers = 0

    year_str = input('Введите год рождения А.С.Пушкина: ')
    if year_str.isnumeric():
        year_numeric = int(year_str)
        if year_numeric == PUSHKIN_YEAR_OF_BIRTH:
            true_answers += 1
            pushkin_year_true = True

    year_str = input('Введите год рождения В.В.Путина: ')
    if year_str.isnumeric():
        year_numeric = int(year_str)
        if year_numeric == PUTIN_YEAR_OF_BIRTH:
            true_answers += 1
            putin_year_true = True

    year_str = input('Введите год рождения В.И.Ленина: ')
    if year_str.isnumeric():
        year_numeric = int(year_str)
        if year_numeric == LENIN_YEAR_OF_BIRTH:
            true_answers += 1
            lenin_year_true = True

    year_str = input('Введите год рождения Э. Че Гевары: ')
    if year_str.isnumeric():
        year_numeric = int(year_str)
        if year_numeric == CHEGUEVARA_YEAR_OF_BIRTH:
            true_answers += 1
            cheguevara_year_true = True

    year_str = input('Введите год рождения П.А.Столыпина: ')
    if year_str.isnumeric():
        year_numeric = int(year_str)
        if year_numeric == STOLYPIN_YEAR_OF_BIRTH:
            true_answers += 1
            stolypin_year_true = True


    print('А теперь подведем итоги:')
    print('Количество правильных ответов:', true_answers)
    print('Количество ошибок:', AMOUNT_QUESTION - true_answers)
    print('Процент правильных ответов: {0:.2f}%'.format(true_answers * 100 / AMOUNT_QUESTION))
    print('Процент неправильных ответов: {0:.2f}%'.format(100 - (true_answers * 100 / AMOUNT_QUESTION)))

    if true_answers == AMOUNT_QUESTION:
        break

    if not pushkin_year_true:
        print('Год рождения А.С.Пушкина', PUSHKIN_YEAR_OF_BIRTH)
    if not putin_year_true:
        print('Год рождения В.В.Путина', PUTIN_YEAR_OF_BIRTH)
    if not lenin_year_true:
        print('Год рождения В.И.Ленина', LENIN_YEAR_OF_BIRTH)
    if not cheguevara_year_true:
        print('Год рождения Э. Че Гевары', CHEGUEVARA_YEAR_OF_BIRTH)
    if not stolypin_year_true:
        print('Год рождения П.А.Столыпина', STOLYPIN_YEAR_OF_BIRTH)

    ans = input('Попробовать еще? ')
    if ans.lower() != 'да':
        break

print('Викторина окончена')