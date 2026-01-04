class Cafe:
    def __init__(self):
        self.products = {}
        self.orders = []

    def add_product(self, name, quantity, price):
        self.products[name] = {'quantity': quantity, 'price': price}

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]

    def update_product(self, name, quantity):
        if name in self.products:
            self.products[name]['quantity'] += quantity

    # def sell_product(self, name, quantity, price): вариант с каждым товаром
    #     if name in self.products:
    #         if quantity <= self.products[name]['quantity']:
    #             self.products[name]['quantity'] -= quantity
    #             # price = self.products[name]['price'] * quantity
    #             self.ordered_products.append((name, quantity, price)) # заказ на один продукт
    #             print(name, quantity, price)
    #         else:
    #             print("Нет досточного количества товаров")
    #     else:
    #         print('Продукта нет в наличии в кафе')

        # if name in self.products: # вариант №2
        #     if quantity >  self.products[name]['quantity']:
        #         print("Нет досточного количества товаров")
        #     else:
        #       self.ordered_products.append((name, quantity, price))
        #       self.products[name]['quantity'] -= quantity
        # else:
        #     print('Продуктов нет в кафе')

    def add_order(self, names, quantites, prices):
        order = []
        for name, quantity, price in zip(names, quantites, prices):
            if name in self.products:
                if quantity <= self.products[name]['quantity']:
                    self.products[name]['quantity'] -= quantity
                    total_price = price * quantity
                    order.append([name, quantity, total_price])
                else:
                    print(f"Нет досточного количества товарa {name}. В наличии есть только {self.products[name]['quantity']}")
            else:
                print(f'Продукта {name} нет в наличии в кафе')

        self.orders.append(order)
        print(order)

        def report_stock(self):
            return self.products

    def report_sales(self):
        return self.order

def main_menu():
        print('1. Касса')
        print('2. Управление')
        print('3. Выйти')

def cash_register(cafe):
    while True:
        print('1. Новая продажа')
        print('2. В главное меню')
        choice = input('Выберите опцию: ')

        if choice == '1': # Для продажи клиенту кофе
            product_name = input('Введите название товаров через запятую: ')
            product_name = product_name.split(',')
            product_name = list(map(lambda x: x.strip(),  product_name))
            quantity = input('Введите количество для продуктов через запятую: ')
            quantity = quantity.split(',')
            quantity = list(map(lambda x: int(x), quantity))
            price = input('Введите цену для продукта через запятую: ')
            price = price.split(',')
            price = list(map(lambda x: float(x), price))
            # if product_name or quantity == "":
            #     print("Ведите данные в строку продукты")
            #     break
            # cafe.sell_product(product_name,quantity,price)
            cafe.add_order(product_name,quantity,price)
        elif choice == '2':
           break

def manager(cafe): # Для работы персонала кофе
    while True:
        print('1. Добавить в продажу товар"')
        print('2. Исключить товар из продажи')
        print('3. Изменить количество товара')
        print('4. Вывести отчет по остаткам')
        print('5. В главное меню')
        choice = input('Выберите опцию:  ')

        if choice == '1':
           name = input('"Введите название товара: ')
           quantity = int(input('Введите количество: '))
           price = float(input('Введите цену:'))
           cafe.add_product(name,quantity,price)
           print(f"Товар {name} добавлен.")

        if choice == '2':
            name = input('Введите название товара для исключения:')
            cafe.remove_product(name)
            print(f"Количество товара {name} исключен.")

        if choice == '3':
            name = input('Введите название товара:')
            cafe.update_product(name,quantity)
            print(f"Количество товара {name} изменен.")

        if choice == '4':
            stock = cafe.report_stock()
            for product, info in stock.items():
                print(f"{product}: {info['quantity']} штук по {info['price']} рублей")

        if choice == '5':
            break

def main():
    cafe = Cafe()
    # cafe.add_product('coffee',10,5) # для теста и проверки работы кода
    # cafe.add_product ('tea',10,3)
    # cafe.add_product ('cake',10,7)
    while True:
        main_menu()
        choice = input('Выберите опцию: ')

        if choice == '1':
            cash_register(cafe)
        elif choice == '2':
            manager(cafe)
        elif choice == '3':
            print('Выход из программы.')
            break

if __name__ == "__main__":
    main()













