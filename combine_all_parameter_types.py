# 5. Combine all parameter types

# Consider this function:

def example(a, /, b, *args, c = 100, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("c:", c)
    print("kwargs:", kwargs)
example(10, 20, 30, 40, c = 50, name = "Raj")