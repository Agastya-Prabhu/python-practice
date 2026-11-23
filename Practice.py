# x = int(input('What's your age? :'))

# if x >= 18: 
#     y = input('Do you have a voter ID card? :')
#     if y == 'Yes':
#         print('Hurray, you are eligible to vote and you have a voter id card so you can vote.')
#     else:
#         print('Sorry, you are eligible to vote but cannot vote since you don't have a voter id card.')
# else:
#     print('You are not eligible to vote.')


# x = int(input('Enter a number: '))

# if x%2 == 0:
#     print('Divisible by 2')
#     if x%4 == 0:
#         print('Multiple of 4')
#     else:
#         print('Not a multiple of 4')
# elif x%3 == 0:
#     print('Multiple of 3')
# else:
#     print('Number is not a multiple of 2 or 3')


# for n in range(0,11,1):
#     print('5 x ',n,' = ',5*n)


# for y in range(0,3,1):
#     print()
#     for n in range(0,4,1):
#         print('# ', end = '')


# for n in range(0,6,1):
#     print()
#     for y in range(0,n,1):
#         print('# ', end = '')


# l = []
# y = 0
# while True:
#     x = int(input('Number: '))
#     if x > 0:
#         l.append(x)
#     else:
#         for n in l:
#             y += n
#         print(y)
#         print(y/len(l))
#         break


# x = int(input('Principal? : '))
# y = int(input('Rate Of Interest? : '))
# z = int(input('Time? : '))

# print('Simple interest is',(x * y * z)/100)


# x = input('1: ')
# y = int(input('2: '))
# z = float(input('3: '))

# list = [x,y,z]
# for n in list:
#     print(type(n))

# while True:
#     x = input('Password: ')

#     if len(x) < 8:
#         print('Password must be at least 8 characters')

#     if len(x) >= 8:
#         print('Weak Password')
#         break

#     if len(x) >= 15:
#         print('Strong Password')
#         break



# temps = [98,88,72,50,46,103,87]

# print('The coldest temperature was ',min(temps),' degrees.')
# print('The hottest temperature was ',max(temps),' degrees.')
# print('The difference was ',max(temps) - min(temps),' degrees.')


# l = []

# for n in range(0,7,1):
#     x = int(input('Expense for today?: '))
#     l.append(x)
# print(sum(l))
# print(sum(l)/len(l))


# students = [
#     {'name': 'A', 'marks': 80},
#     {'name': 'B', 'marks': 95},
#     {'name': 'C', 'marks': 70}
# ]

# for n in range(len(students)):


# for n in range(0,11,1):
#     print(5,' * ',n,' = ',5*n)


# names = ['A', 'B']
# marks = [90, 80]

# print(list(zip(names, marks)))


# x = input('word: ')

# print(x.split(' '))

# y = x.split(' ')
# z = ' '.join(y)

# print(z)


# x = 1
# y = 2

# print(x==y)


class Guitar:
    def __init__(self,strings, pegs, frets, type):
        self.strings = strings
        self.pegs = pegs
        self.frets = frets
        self.type = type
        self.tuned = False
    def song(self):
        if self.tuned:
            print("Playing song!")
    def setup(self):
        x = input("What strings?")
        self.strings = x
        y = input("What tuning?")
        self.pegs = y
        z = input("What notes?")
        self.frets = z
        q = input("what type of guitar?")
        self.type = q
        self.tuned = True

x = Guitar(False,"Untuned","Unhit","IDK")
x.setup()
x.song()


class Double_Headed_Guitar(Guitar):
    def __init__ (self,heads):
        self.heads = heads
        Guitar.__init__(self,1,2,31,"Acoustic")
        self.pegs = 1
    
y = Double_Headed_Guitar(2)
y.setup()
y.song()