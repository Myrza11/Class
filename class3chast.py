from typing import final


class Human:
    #статические поля
    default_name = 'No name'
    default_age = 0
    
    def __init__(self, name=default_name, age=default_age):
        #Публичные поля
        #Динамические поля
        self.name = name
        self.age = age
        #приватные поля
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'House: {self.__house}')
        print(f'Money: {self.__money}')

    #статические поля
    @staticmethod
    def default_info():
        print(f'Имя по умолчанию: {Human.default_name}')
        print(f'Возраст по умолчанию: {Human.default_age}')

    #приватный метод
    def __make_deal(self, house, price):
        self.__money += price
        self.__house = house
        
    def earn_money(self, amount):
        self.__money += amount
        print(f'Вы заработали {amount} денег! В вашем кошелке {self.__money} денег')

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print("Иди работай")

class House:
    #динамической метод
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price // 100 * discount
        print(f'Финальный прайс: {final_price}')
        return final_price 

class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)




if __name__ == "__main__":
    Myrza = Human("Myrza", 15)
    Myrza.info()
    Myrza.default_info()
    Myrza.earn_money(5000)
    Myrza.earn_money(40000)
    house = House(100, 50000)
    smallHouse = SmallHouse(40000)
    Myrza.buy_house(smallHouse, 5)
    Myrza.info()
    Myrza.earn_money(5000)
    Myrza.earn_money(5000)
    Myrza.earn_money(5000)
    Myrza.buy_house(house, 5)
    Myrza.buy_house(smallHouse, 10)
    Myrza.info()


from typing import final

'''
class Human:
    #статические поля
    default_name = 'No name'
    default_age = 0
    
    def __init__(self, name=default_name, age=default_age):
        #Публичные поля
        #Динамические поля
        self.name = name
        self.age = age
        #приватные поля
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'House: {self.__house}')
        print(f'Money: {self.__money}')

    #статические поля
    @staticmethod
    def default_info():
        print(f'Имя по умолчанию: {Human.default_name}')
        print(f'Возраст по умолчанию: {Human.default_age}')

    #приватный метод
    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house
        
    def earn_money(self, amount):
        self.__money += amount
        print(f'Вы заработали {amount} денег! В вашем кошелке {self.__money} денег')

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print("Иди работай")

class House:
    #динамической метод
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'Финальный прайс: {final_price}')
        return final_price 

class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)




if __name__ == "__main__":
    Kayrat = Human("Kayrat", 25)
    Kayrat.info()
    Kayrat.default_info()
    Kayrat.earn_money(5000)
    Kayrat.earn_money(4000)
    house = House(100, 50000)
    smallHouse = SmallHouse(25000)
    Kayrat.buy_house(smallHouse, 5)
    Kayrat.info()
    Kayrat.earn_money(5000)
    Kayrat.earn_money(5000)
    Kayrat.earn_money(5000)
    Kayrat.buy_house(house, 10)
    Kayrat.buy_house(smallHouse, 5)
    Kayrat.info()
'''