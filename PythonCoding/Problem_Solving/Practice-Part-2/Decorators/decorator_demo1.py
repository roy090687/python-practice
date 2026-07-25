# decorator function with extra login without disturbing the original div() function.
def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner

@smart_div
def div(a, b):  # original function
    print(a/b)

# div = smart_div(div) => not required when using decorator annotation @smart_div
div(2, 6)
