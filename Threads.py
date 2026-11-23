# import time
# import threading

# def function_one():
#     for n in range(1,11,1):
#         print(n)
#         time.sleep(1)

# def function_two():
#     for n in range(15):
#         print("Agastya")
#         time.sleep(1)

# # function_one()
# # function_two()

# thread1 = threading.Thread(target = function_one)
# thread2 = threading.Thread(target = function_two)

# thread1.start()
# thread2.start()
# thread2.join()


# from threading import Thread

# def print_double(num):
#     print('The double of {} is {}'.format(num, num*2))

# double_maker = Thread(target=print_double, args=(10,))
# double_maker.start()

# print('Thread ended')


# from threading import Thread

# def get_squares(start, end):
#     for num in range(start, end+1, 1):
#         print('The square of {} is {}'.format(num, num*num))

# square_thread = Thread(target=get_squares, args=(10, 20))
# square_thread.start()
# square_thread.join()

# print('Message One')
# print('Message Two')
# print('Message Three')


# from threading import Thread

# def prime_checker(num):
#     prime = True
#     for d in range(2, int(num**0.5) + 1, 1):
#         print('{} checked with {}'.format(num, d))
#         if num % d == 0:
#             prime = False
#     if prime == True:
#         print('{} is a prime number'.format(num))
#     else:
#         print('{} is a not prime number'.format(num))


# def primes(numbers):
#     for num in numbers:
#         t = Thread(target=prime_checker, args=(num,))
#         t.start()
#         t.join()
#         print('Completed check for {}!'.format(num))



# prime_thread = Thread(target=primes, args=([4483, 4493, 4507, 4561, 4567, 4583, 4591], ))
# prime_thread.start()
# prime_thread.join()
# print('The program ended')


# from threading import Thread
# from time import sleep
# letters = ['A', 'B', 'C', 'D']


# def func():
#     for letter in letters:
#         print(letter)
#         sleep(2)


# thread = Thread(target=func)
# thread.start()
# print('E')

# from threading import Thread
# from time import sleep


# def number_printer():
#     for number in range(1, 6, 1):
#         print(number)
#         sleep(1)



# thread = Thread(target=number_printer)
# thread.start()
# print('A')
# thread.join()
# print('B')


# from threading import Thread
# import random

# x = []


# for list in range(5):
#     y = []
#     for num in range(100):
#        z = random.randint(1,100)
#        y.append(z) 
#     x.append(y)

# def product(row):
#     p = 1
#     for n in row:
#         p *= n
#     print(p)

# for row in x:
#     thread = Thread(target = product, args = (row,))
#     thread.start()



# from threading import Thread

# locations = ["C:/Users/Agastya_Prabhu/OneDrive - Cary Academy/Documents/Hello Gus!.txt",
#              "C:/Users/Agastya_Prabhu/OneDrive - Cary Academy/Documents/Hello Agastya!.txt",
#                "C:/Users/Agastya_Prabhu/OneDrive - Cary Academy/Documents/Hello Kabir!.txt"]

# def count(location):
#     c = 0
#     f = open(location, "r")
#     for x in f:
#         c += 1
#     print(c)

# for n in locations:
#     thread = Thread(target = count, args = (n,))
#     thread.start()


from threading import Thread
import random



def hundred():
    for n in range(0,10,1):
        print(random.randint(0,1000))

thread = Thread(target = hundred)
thread.start()


while thread.is_alive():
    print("Running")
else:
    print("Thee programith hath stoppeth")