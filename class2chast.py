# первая задача
class Factory:
    def engine(self):
        return "двигатель создан"
    def bridge(self):
        return "ходовая часть создана"    
f = Factory()   
print(f.engine())
print(f.bridge())


class Toyota(Factory):
    def wheels(self):
        return "калёса готовы"
    def windows(self):
        return "Стёкла готовы" 
t = Toyota()
print(t.wheels())
print(t.windows())
x = [t.engine(), t.bridge(), t.wheels(), t.windows()]
print(x)

# вторая задачa
class Zoo:
    def __init__(Zoo):
        self.animal_1 = "Тигр"
        self.animal_2 = "Бегемот"
        self.animal_3 = ""

# третье задание
class Car:
    # , make, model, year, odometer, fuel
    def __init__(self):
        self.make = ''
        self.model = ''
        self.year = ''
        self.odometer = 0
        self.fuel = 70

    def __add_distance(self, distance):
        self.odometer += distance

    def __subtract_fuel(self, distance):
        self.fuel -= distance / 10

    def drive(self, distance):
        if self.fuel * 10 >= distance:
            print("Let’s drive!")
            self.__add_distance(distance)
            self.__subtract_fuel(distance)
        else:
            print("Need more fuel, please, fill more!")


BMW = Car()
BMW.drive(1000)
  
# четвёртое задание
class Soldier():
    def __init__(self, name, guns):
        self.name = name
        self.guns = guns

class Guns():
    def shoots(self):
        print(f'{self.name} стрелял с {self.guns}')
        self.shop = 30
        while self.shop > 0:
            self.shop -= 1
            if self.shop == 0:
                print("нужно перезаридится")
                self.strelka()
            else:
                pass

    def strelka(self):
        self.strelok = input('prodolzhit strelbu? y/n:') 
        if self.strelok == 'y':
            self.shoots()
        else:
            pass

class Act_of_Shooting(Soldier, Guns):
    def __init__(self, name, guns):
        Soldier.__init__(self, name, guns)
        
s = Act_of_Shooting("Myrza", "Ak_47")
s.shoots()


