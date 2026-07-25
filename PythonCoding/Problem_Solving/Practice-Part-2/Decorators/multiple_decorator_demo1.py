from functools import wraps

def log(func):
    @wraps(func)
    def wrap(a, b):
        output = func(a, b)
        print(f"[LOG] {func.__name__}({a}, {b}) = {output}")
        return output
    return wrap

def greater_first(func):
    @wraps(func)
    def wrap(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return wrap

@log
@greater_first
def div(a, b):
    return a/b

@log
@greater_first
def sub(a, b):
    return a - b


div(7, 14)
sub(2, 6)

