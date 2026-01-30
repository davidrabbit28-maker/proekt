import random as r
spisok = [r.randint(500, 1000) for i in range(10)]
spisok_2 = list(range(0, 500, 2))
spisok_3 = [r.choice(spisok_2) for i in range(10) ] 

print(spisok_3)
