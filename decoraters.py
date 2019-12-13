from functools import wraps
# Decoraters
# A function which takes another function as an argument, adds some kind of 
# functionailty and returns another function
# def decorater_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print('Wrapper executed this before {}'.format(original_function.__name__))
#         return original_function(*args, **kwargs)
#     return wrapper_function

# # class decorater_class(object):

# #     def __init__(self, original_function):
# #         self.original_function = original_function

# #     def __call__(self, *args, **kwargs):
# #         print('call method executed this before {}'.format(self.original_function.__name__))
# #         return self.original_function(*args, **kwargs)

# # @decorater_class
# @decorater_function
# def display():
#     print('display function ran')

# # @decorater_class
# @decorater_function
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))

# display_info('John', 25)
# display()
# # decorater_display = decorater_function(display)
# # decorater_display()

# Practical Example
def my_logger(orig_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_function.__name__), level=logging.INFO)

    @wraps(orig_function)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs)
        )
        return orig_function(*args, **kwargs)
    return wrapper


def my_timer(orig_function):
    import time

    @wraps(orig_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in {} sec'.format(orig_function.__name__, t2))
        return result
    return wrapper

import time

@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Tom', 25)