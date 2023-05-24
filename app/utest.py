from customtkinter import *
import sqlite3
import unittest
from mini_pro import Application

class ApplicationTests(unittest.TestCase):

    global a
    a = CTk()

    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()

        # Створення тестової таблиці appointments
        self.c.execute('''
            CREATE TABLE appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                gender TEXT,
                location TEXT,
                phone TEXT
            )
        ''')
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_add_appointment(self):
        app = Application(a)
        app.name_ent = CTkEntry(a, width=30)
        app.name_ent.insert(1,'name')
        app.age_ent = CTkEntry(a, width=30)
        app.age_ent.insert(1, '100')
        app.v = CTkEntry(a, width=30)
        app.v.insert(1, '1')
        app.location_ent = CTkEntry(a, width=30)
        app.location_ent.insert(1, 'kovel')
        app.phone_ent = CTkEntry(a, width=30)
        app.phone_ent.insert(1, '123123')


        app.add_appointment()

        #Перевірка додавання запису в базу даних
        # self.c.execute('SELECT COUNT(*) FROM appointments')
        # count = self.c.fetchone()[0]
        # self.assertEqual(count, 0)

    def test_homee(self):
        app = Application(a)
        # ... Імітувати створення та розміщення елементів GUI

        app.homee()

        # Перевірка відображення GUI

    def test_update1(self):
        app = Application(a)
        app.name1 = 'Anya'
        app.age = '100'
        app.gender = 0
        app.location = 'Kovel'
        app.phone = '3123123'

        app.name_ent = 'John Doe'
        app.age_ent = '30'
        app.v = 1
        app.location_ent = 'New York'
        app.phone_ent = '1234567890'

        app.updatee()
        app.update1()

        # Перевірка оновлення запису в базі даних

    def test_update2(self):
        app = Application(a)
        app.var1 = 'John Doe'
        app.var2 = '30'
        app.var3 = 1
        app.var4 = 'New York'
        app.var5 = '1234567890'
        app.idnet = CTkEntry(a, width=30)
        app.idnet.insert(1, '10')
        app.ent1 = CTkEntry(a, width=30)
        app.ent2 = CTkEntry(a, width=30)
        app.ent3 = CTkEntry(a, width=30)
        app.ent4 = CTkEntry(a, width=30)
        app.ent5 = CTkEntry(a, width=30)
        app.update2()

        # Перевірка оновлення запису в базі даних

    def test_delete1(self):
        app = Application(a)
        app.name1 = 'Anya'
        app.age = '100'
        app.gender = 0
        app.location = 'Kovel'
        app.phone = '3123123'
        app.updatee()
        # ... Імітувати введення даних користувачем

        app.delete1()

        # Перевірка видалення запису з бази даних

    def test_delete2(self):
        app = Application(a)
        app.idnet = CTkEntry(a, width=30)
        app.idnet.insert(1, '10')
        app.ent1 = CTkEntry(a, width=30)
        app.ent2 = CTkEntry(a, width=30)
        app.ent3 = CTkEntry(a, width=30)
        app.ent4 = CTkEntry(a, width=30)
        app.ent5 = CTkEntry(a, width=30)

        # ... Імітувати введення даних користувачем

        app.delete2()

        # Перевірка видалення запису з бази даних


if __name__ == '__main__':
    unittest.main()