import random

def generate_lst(x, y, z):
    return [random.randint(y, z) for i in range(x)]

a = generate_lst(10, 1, 5)
print(a)

def generate_set(x):
    
    st = set(x)
    return st
print(generate_set(a))