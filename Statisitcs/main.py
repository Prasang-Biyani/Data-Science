def _median_odd(xs):
    return sorted(xs)[len(xs) // 2]

def _median_even(xs):
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2

def median(xs):
    return _median_even(xs) if len(xs) % 2 == 0 else _median_odd(xs)

assert median([1, 2, 3, 4, 5, 6, 7]) == 4
assert median([4, 5, 6, 7]) == (5 + 6) / 2

def mean(xs):
    return sum(xs) / len(xs)

def quantile(xs, p):
    '''Returns the p-th percentile value in x'''
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

# Dispersion - How spread out the data is
def data_range(xs):
    return max(xs) - min(xs)




 
