def dict(x):
        slovar = {"мама":"mother", "кот":"cat", "солнце":"sun"}
        getFunc = slovar.get(x, "Напишите другое слово.")
        return getFunc
        

a = input("Слово сюда --> ")

while a != "стоп":
    print(dict(a))


    a = input("Слово сюда --> ")