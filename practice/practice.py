import sqlite3


class ErrorInit(Exception):

    def __str__(self):
        return f'Ваша карта заблокирована'


connection = sqlite3.connect('users.db')

cur = connection.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
               user_id integer PRIMARY KEY,
               name TEXT,
               number_card TEXT,
               pin_cod TEXT,
               balance TEXT
               date_registered TEXT);
            """)


class ATM:
    locked_card = ['123-333-123-555']

    print(f'Введите номер карты и pin cod')

    def __init__(self, number_card=input('Введите номер карты: '),
                 pin_cod=input('Введите пин код: ')):
        self.number_card = number_card
        self.pin_cod = pin_cod

    def check_balance(self):
        try:
            if self.number_card not in self.locked_card:
                if self.initialization(self.number_card, self.pin_cod) is True:
                    cur.execute("SELECT * FROM users")
                    for el in cur.fetchall():
                        if self.number_card == el[2]:
                            print(f'\n'
                                  f'Добро пожаловать {el[1]}\n'
                                  f'Ваш баланс: {el[4]}-грн\n')
                else:
                    error = 0
                    while True:
                        error += 1
                        print(f'Неверный пароль осталось: {3 - error} попыток')
                        if error == 3:
                            self.locked_card.append(self.number_card)
                            print('Ваша карта заблокирована!')
                            break
                        self.pin_cod = input('Введите пин код: ')
                        if self.initialization(self.number_card, self.pin_cod) is True:
                            cur.execute("SELECT * FROM users")
                            for el in cur.fetchall():
                                if self.number_card == el[2]:
                                    print(f'\n'
                                          f'Добро пожаловать {el[1]}\n'
                                          f'Ваш баланс: {el[4]}-грн\n')
                            break
            else:
                raise ErrorInit
        except ErrorInit:
            print(ErrorInit())

    def money(self):
        try:
            if self.number_card not in self.locked_card:
                if self.initialization(self.number_card, self.pin_cod) is True:
                    balance = 0
                    money = int(input('Сколько хотите снять? '))
                    cur.execute("SELECT * FROM users")
                    for el in cur.fetchall():
                        if self.number_card == el[2]:
                            balance = int(el[4])
                    if money > balance:
                        print('Не достаточно средств')
                    else:
                        result = balance - money
                        sqlite_connection = sqlite3.connect('users.db')
                        cursor = sqlite_connection.cursor()

                        sql_update_query = f"""Update users set balance = {result} where user_id = 1"""
                        cursor.execute(sql_update_query)
                        sqlite_connection.commit()
                        print(f'{money}-грн успешно сняты')
                        cursor.close()
                else:
                    error = 0
                    while True:
                        error += 1
                        print(f'Неверный пароль осталось: {3 - error} попыток')
                        if error == 3:
                            self.locked_card.append(self.number_card)
                            print('Ваша карта заблокирована!')
                            break
                        self.pin_cod = input('Введите пин код: ')
                        if self.initialization(self.number_card, self.pin_cod) is True:
                            balance = 0
                            money = int(input('Сколько хотите снять? '))
                            cur.execute("SELECT * FROM users")
                            for el in cur.fetchall():
                                if self.number_card == el[2]:
                                    balance = int(el[4])
                            if money > balance:
                                print('Не достаточно средств')
                            else:
                                result = balance - money
                                sqlite_connection = sqlite3.connect('users.db')
                                cursor = sqlite_connection.cursor()

                                sql_update_query = f"""Update users set balance = {result} where user_id = 1"""
                                cursor.execute(sql_update_query)
                                sqlite_connection.commit()
                                print(f'{money}-грн успешно сняты')
                                cursor.close()
                            break
            else:
                raise ErrorInit
        except ErrorInit:
            print(ErrorInit())

    @staticmethod
    def initialization(number_card, pin_cod):
        cur.execute("SELECT * FROM users")
        for el in cur.fetchall():
            if number_card == el[2]:
                if pin_cod == el[3]:
                    return True
                return False


connection.commit()

if __name__ == '__main__':
    user1 = ATM()
    user1.check_balance()
    user1.money()
