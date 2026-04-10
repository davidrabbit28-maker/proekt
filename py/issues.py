'''
scores = [120]

def second(scores):
    if len(scores) >= 2:
        seted = list(set(scores))
        seted.remove(min(scores))
        
        return min(seted)
    else:
        print("Всего один заяц в списке")
print(second(scores))
'''

'''
spisok = [1, -7, 4, 8, -4, 1, 10]
spisok2 = []
for i in spisok:

    if 1 <= i <= 5:
        spisok2.append(i)
        

print(sum(spisok2) // len(spisok2))


print(spisok2)
'''
a = {"Батарея":5, "CPU":3, "GPU":4, "Колесо":20}
# b = a.get("CPU", 1)
# def zapros(a, b):

#     for i in a:
#         if a.get(i, 0):


print(a.get("CPU", "Такого ключа нет"))