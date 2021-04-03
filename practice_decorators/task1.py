'''
Для того щоб подолати шлях від New Jersey до New York, потрібно проїхатися по платному мосту, який автоматично списує кошти
з людини яка має відповідну мітку. Створіть декоратор Fare, та застосуйте його до функції bridge, по якій їздять люди Person.
За проїзд мостом в них віднімаються кошти, якщо їх достатньо та якщо в них присутня мітка. Якщо мітки немає, але грошей достатньо
для оплати проїзду та покупки мітки, зробіть це, в іншому випадку PassageProhibited exception не дасть людині переїхати міст!
'''
​
MARK_COST = 2.5
CROSS_COST = 0.5
​
​
class PassageProhibited(Exception):
    pass
​
​
vehicle_type = ["Cargo", "Passengers"]
​
​
class Person:
    def __init__(self, cash: float, mark: bool, vehicle: vehicle_type):
        self.cash = cash
        self.mark = mark
        self.vehicle = vehicle
​
​
def fare(func):
    def inner_func(person):
        func(person)
        count_mark_cost = MARK_COST
        count_cross_cost = CROSS_COST
        if person.vehicle == "Cargo":
            count_mark_cost *= 2
            count_cross_cost *= 2
        if person.mark:
            if person.cash >= count_cross_cost:
                person.cash -= count_cross_cost
                print('Crossing is successful!')
            else:
                print("Not enough cash to cross the bridge")
                # raise PassageProhibited
        else:
            if person.cash >= count_mark_cost + count_cross_cost:
                person.cash -= count_mark_cost + count_cross_cost
                person.mark = True
                print('Crossing is successful!')
            else:
                print("Not enough cash to buy mark and cross the bridge")
                # raise PassageProhibited
​
    return inner_func
​
​
@fare
def bridge(person):
    print(f"Person with ${person.cash} and mark is {person.mark} on {person.vehicle} car is crossing the bridge.")
​
​
person1 = Person(3.5, False, "Passengers")
person2 = Person(3.5, True, "Passengers")
person3 = Person(0.5, False, "Passengers")
person4 = Person(0.5, True, "Passengers")
person5 = Person(7, False, "Cargo")
person6 = Person(7, True, "Cargo")
person7 = Person(1, False, "Cargo")
person8 = Person(1, True, "Cargo")
​
bridge(person1)
bridge(person2)
bridge(person3)
bridge(person4)
bridge(person5)
bridge(person6)
bridge(person7)
bridge(person8)