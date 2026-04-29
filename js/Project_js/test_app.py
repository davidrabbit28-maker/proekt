'''
def convert(a):
    hours = a // 60 
    mins = a % 60
    return f"{a} минут это {hours} часов, и {mins} минут"

print(convert(243))
'''
'''
s = [10, 5, 9, -4, 2, -8]

def tiposet(s):
    bolshe = []
    for i in s:
        if i > 0:
            bolshe.append(i)
    return sorted(bolshe, reverse=True)

print(tiposet(s))
'''
'''
s = [10, 5, 9, -4, 2, -8]

def tipoEtoNeSet(s):
    bolshe = [i for i in s if i > 0]
    return sorted(bolshe, reverse=True)

print(tipoEtoNeSet(s))
'''
'''
pokupki = ["Свитер", "Галстук", "Ананас", "Туфли"]

def poisk(pokupki, slovo):
    shet = 1
    for i in pokupki:
        if i == slovo:
            return f"Да, это есть в наличии! Номер позиции {shet}"
    
        shet += 1
    return "Объект не найден"

print(poisk(pokupki, "Туфли"))
'''

'''
class scoreboard:
    def __init__(self, points):
        self.points = points


    def add_points(self, how_many_points):
        self.points += how_many_points
    
    
        return self.points
    

    def del_points(self, how_many_del):
        if how_many_del > self.points:
            self.points = 0
        else:
            self.points -= how_many_del

        return self.points
    

a = scoreboard(10)
print(a.del_points(8))
'''



def lensort(a):
    lended = len(a)
    return f"Количество слов: {len(a.split())}, Количество символов: {lended}" 

print(lensort("Hello World"))