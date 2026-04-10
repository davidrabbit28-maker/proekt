''' def test(x, y):
    return x * y


print(test(10, 5))

def test_2(*chto_ugodno):
    print(chto_ugodno)
    shet = 1
    for i in chto_ugodno:
        shet *= i
    return shet
print(test_2(5, 6, 7, 5, 5))

def test_3(x, y, z = 1):
    summa = x + y + z
    return summa
print(test_3(x = 5, y = 6))

def info(**quarcs):
    return quarcs

print(info(name = "david", age = 13, sex = "man", color = "yellow", random = "5"))






def summaa(*args):
    sUm = 0
    for i in args:
        sUm += i
    
    return sUm


print(summaa(1, 5, 5, 6, 7, 8, 9))
'''

def n(*args, x = " "):
    return x.join(args)

print(n("Hello", "World"))


def d(*args, action = "сумма"):
    if action == "сумма":
        return sum(args)
    elif action == "вычитание":
        shetchik = args[0]
        for i in args[1:]:
            shetchik -= i
        return shetchik
    elif action == "умножение":
        shetchik2 = 1
        for i in args:
            shetchik2 *= i
        return shetchik2
print(d(10, 5, 1, action="умножение"))


def test_4(*args):
    for i in args:
        print(i)


print(test_4("Привет", 3, 6.4))