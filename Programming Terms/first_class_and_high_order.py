# First class function: A function which is treated like any other variable.
# A function can be passed as an argument, can be assigned to a variable, and can be returned like any other variable.
def square(x):
    return x * x

def cube(x):
    return x * x * x
# f = square
# print(square)
# print(f(5))

# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result

# squares = my_map(square, [1, 2, 3, 4, 5])
# print(squares)
# cubes = my_map(cube, [1, 2, 3, 4, 5])
# print(cubes)

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}<{0}>'.format(tag, msg))
    return wrap_text

# html_tag('h1')('Test headline!')
print_h1 = html_tag('h1')
print_h1('Test headline!')
# print_h1('Test headline!')
# print_h1('Another Tag')
