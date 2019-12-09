import time
import itertools

# A programming technique where we use cache 
# to store the result of a expensive function

ef_cache = dict()

def expensive_func(num):
    result = num * num
    if num in ef_cache:
        return result
    print('Computing {}...'.format(num))
    time.sleep(1)
    ef_cache[num] = result
    return result

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)