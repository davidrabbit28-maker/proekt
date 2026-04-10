'''def rekurs(n):
    schet = 0
    for i in range(0, n + 1):
        schet += i
    return schet 

print(rekurs(5))'''

def rekurs(n):
    if n == 0:
        print("Всё")
        return 0

    return n + rekurs(n - 1) 

print(rekurs(5))