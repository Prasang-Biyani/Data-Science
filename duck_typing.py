# # Easier to ask for forgiveness then permission (EAFP)

# first example

# class Duck:
    
#     def quack(self):
#         print('Quack, quack!')
    
#     def fly(self):
#         print('Flap, Flap!')

# class Person:

#     def quack(self):
#         print("I'am Quacking like a Duck!")

#     def fly(self):
#         print("I'm Flapping my Arms!")

# def quack_and_fly(thing):

#     try:
#         thing.quack()
#         thing.fly()
#     except AttributeError as e:
#         print(e)

#     print()

# d = Duck()
# quack_and_fly(d)

# p = Person()
# quack_and_fly(p)

# second example

# person = {'name' : 'Jess', 'age' : 23, 'job': 'developer'}
# # person = {'name' : 'Jess', 'age' : 23}

# # Look Before you Leave (LBYL) (Non-Pythonic)
# # if 'name' in person and 'age' in person and 'job' in person:
# #     print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
# # else:
# #     print('Missing some keys')

# # EAFP (Pythonic)
# try:
#     print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
# except KeyError as k:
#     print('Missing {} key'.format(k))

# third example
import os
my_file = 'tmp.txt'

# Race Condition
# if os.access(my_file, os.R_OK):
#     with open(my_file) as f:
#         print(f.read())
# else:
#     print('File cannot be accessed')

# Non-Race Condition
try:
    f = open(my_file)
except IOError as e:
    print('File can not be accessed')
else:
    with f:
        print(f.read())



