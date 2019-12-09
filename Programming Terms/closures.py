# Closures :  A function which remembers/stores the variable information.
# Closures : A closure gives you access to an outer function's scope from an inner function.

# def Hello():
#     msg = 'Hello'
#     def World():
#         print(msg + ' ' + 'World')
#     return World


# hello = Hello()
# hello()
import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info(
            'Running with "{}" with arguments {}'.format(func.__name__, args)
        )
        print(func(*args))
    return log_func


def add(x, y):
    return x + y

def sub(x, y):
    return x - y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 4) # 7
sub_logger(9, 5) # -4


