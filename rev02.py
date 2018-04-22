str = input('please enter a couple of strings:')
def f(x):
    if len(x) <1:
        return x
    return f(x[1:])+x[0]
