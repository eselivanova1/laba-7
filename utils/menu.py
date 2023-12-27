def print_commands(n):
    if n == 1:
        print('Sellers commands: ')
        print('1. Sellers.id - Получить id сотрудника по имени.')
        print('2. Sellers.dismiss - Уволить сотрудника по id.')
        print('3. Sellers.employ - Нанять сотрудника.')
        print('4. Sellers.update - обновление информации.')
    if n == 2:
        print('brand commands: ')
        print('1. Brand.id - Получить id бренда товаров.')
        print('2. Brand.del - Удалить бренд.')
        print('3. Brand.add - Добавить бренда.')
    if n == 3:
        print('Product commands: ')
        print('1. Product.cnt - количество товара')
        print('2. Product.add - добавить товар')
        print('3. Product.get_all_in_Brand - получить все товары бренда')
    if n == 4:
        print('Shops commands: ')
        print('1. Shop.id - Получить id магазина.')
        print('2. Shop.add - Добавить магазин.')
