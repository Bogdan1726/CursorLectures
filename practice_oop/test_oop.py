class Human:
    # static field
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age, money=0, house=None):
        # public field
        self.name = name
        self.age = age
        # private field
        self.__money = money
        self.__house = house

    def info(self):
        print(f'My name is {self.name} my age {self.age} year \n'
              f'Money - {self.__money}$ My house - {self.__house}')

    @staticmethod
    def default_info():
        print(f'Default name: {Human.default_name} \n'
              f'Default age: {Human.default_age}')

    def earn_money(self, values):
        self.__money += values
        print(f'Вы заработали - {values}$ \n'
              f'Ваш баланс: {self.__money}$')

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
            print(f'Вы купили дом: {self.__house}')
        else:
            print('Не достаточно средств')

    # privat method
    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house


class House:

    def __init__(self, area: int, price: int):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_discount = self._price * (100 - discount)/100
        print(f'Цена дома со скидкой: {final_discount}$')
        return final_discount


class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super(SmallHouse, self).__init__(SmallHouse.default_area, price)

    def __str__(self):
        return f'LuxHouse'


if __name__ == '__main__':
    Human.default_info()
    bogdan = Human('Bogdan', 27)
    bogdan.info()
    for i in range(10):
        bogdan.earn_money(2000)
    bogdan.info()
    lux = SmallHouse(15000)
    bogdan.buy_house(lux, 10)
    bogdan.info()








