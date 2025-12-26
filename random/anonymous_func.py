# d = lambda a, b: a + b
# print(d(5, 5))

# cuadrat = lambda a: a * a
# print(cuadrat(5))

# delenie = lambda a, b: "123" if b == 0 else a / b
# print(delenie(10, 0))

# beta_test = lambda x, y, z: "привет" if x + y + z == 10 else "пока"
# print(beta_test(2, 8, 0))
'''
spisok = []
a = input().split()
for i in a:
    try:
        spisok.append(int(i))
    except ValueError:
        continue
print(spisok)
'''

'''
polindrom = lambda a: a.lower() == a[::-1].lower() 
print(polindrom("шалаШ"))
'''

a = ["что-то", "привет", "проект", "Да"]
b = lambda x: len(x) > 3 

print(list(filter(b, a)))