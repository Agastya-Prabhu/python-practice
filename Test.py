# class Vehicle:
#     def __init__(self, brand, model, rental_price_per_day):
#         self.brand = brand
#         self.model = model
#         self.rental_price_per_day = rental_price_per_day
#     def display(self):
#         print("Brand: ", self.brand)
#         print("Model: " , self.model)
#         print("Rental price daily: ", self.rental_price_per_day)
# class Car(Vehicle):
#     def __init__(self, brand, model, rental_price_per_day, num_doors):
#         super().__init__(brand, model, rental_price_per_day)
#         self.num_doors = num_doors
#     def display(self):
#         super().display()
#         print("# of doors: ", self.num_doors)

# class Bike(Vehicle):
#     def __init__(self, brand, model, rental_price_per_day, has_gears):
#         super().__init__(brand, model, rental_price_per_day)
#         self.has_gears = has_gears
#     def display(self):
#             super().display()
#             print("Has gear: ", self.has_gears)

# C1 = Car("Honda", "Oddysey", 75, 50)
# C2 = Car("Lambo", "Hurrican", 101, 90)

# B1 = Bike("Bikes.com", "SuperBike1000", 11, 25)
# B2 = Bike("Bikes.org", "AwesomeBike1001", 12, 52)

# vehicles = [C1, C2, B1, B2]

# for x in vehicles:
#     x.display()
#     print()


# import tkinter as tk
# from tkinter import *

# def insertion():
#     a = [int(x) for x in entry.get().split(",")]

#     for n in range(1,len(a)):
#         x = a[n]
#         j = n - 1

#         while j >= 0 and a[j] > x:
#             a[j + 1] = a[j]
#             j -= 1

#         a[j + 1] = x

#     result.config( text = a)

# def bubble():
#     a = [int(x) for x in entry.get().split(",")]

#     for i in range(9):
#         for j in range(9 - i):
#             if a[j] > a[j+1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#     result.config( text = a)

# window = tk.Tk()
# window.title("Sort")

# tk.Label(window, text = "enter 10 nums: ").pack()

# entry = tk.Entry(window)
# entry.pack()

# tk.Button(window, text = 'Insertion Sort!!!', command = insertion).pack()
# tk.Button(window, text = 'Bubbly Sort!!!', command = bubble).pack()

# result = tk.Label(window, text = "")
# result.pack()

# window.mainloop()

# import threading
# import time

# def task(name, steps, delay):
#     for step in range(1, steps + 1):
#         time.sleep(delay)
#         print(f"{name} Step {step}/{steps} completed")
#     print(f"{name} Finished!!")

# tasks_config = [("Make tea", 3, 1.0),("Toast bread", 2, 1.5),("Read news", 4, 0.8)]

# threads = []

# for name, steps, delay in tasks_config:
#     thread = threading.Thread(target = task, args = (name, steps, delay))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# print("\nBreakfast Ready!!")


# import sqlite3 

# con = sqlite3.connect("database.db")
# cur = con.cursor()

# while True:
#     print("\n1. Create a table")
#     print("2. Read a table")
#     print("3. Update a table")
#     print("4. Delete a table")
#     print("5. Exit")

#     choice = input("What would you like to do? ")

#     if choice == '1':
#         name = input("Enter the table name: ")
#         n = int(input("How many columns? "))
#         columns = []

#         for i in range(n):
#             col = input("Enter column name: ")
#             columns.append(col + " TEXT")

#         cur.execute("CREATE TABLE " + name + " (" +  ", ".join(columns) + ")")
#         con.commit()
#         print("Table created!")

#         values = []
#         for col in columns:
#             value = input("Enter value for " + col.split()[0] + ": ")
#             values.append(value)

#         cur.execute("INSERT INTO " + name + " VALUES (" + ", ".join(["?"] * n) + ")", values)

#     elif choice == "2":
#         name = input('Enter the table name: ')
#         cur.execute("SELECT * FROM " + name)
#         rows = cur.fetchall()

#         for row in rows:
#             print(row)
#     elif choice == "3":
#         name = input("Enter the table name: ")
#         col = input("Enter the column to update: ")
#         value = input("Enter the new value: ")
#         condition = input("Enter the condition column: ")
#         old = input("Enter the value to find: ")

#         cur.execute("UPDATE " + name + " SET " + col + " = ? WHERE " + condition + " = ?", (value, old))
#         con.commit()
#         print("Table deleted!!")

#     elif choice == "4":
#         name = input("Enter the table name: ")
#         cur.execute("DROP TABLE " + name)
#         con.commit()
#         print("Table deleted!")

#     elif choice == "5":
#         break
#     # else:
#     #     print("Invalid Choice! Try again.")
# con.close()


def summation(n):
    if n < 10:
        return n
    return (n % 10) + summation(n // 10)

num = 163
result = summation(num)
print("The sum of the digits of "+ str(num) + "is: " + str(result) + "!!")