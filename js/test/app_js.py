class snow:
    
    def __init__(self, kg, sostav):

        self.kg = kg
        self.sostav = sostav

    def chistka(self):
        if self.kg > 20:
            return "Слишком много снега, нужен трактор"
        else:
            return "Мало снега, сейчас почищу"

    def snowman(self):
        if self.sostav == "Влажно" and self.kg > 5:
            return "Вы можете слепить снеговика!"
        else: 
            "Не получится слепить снеговика =("



a = snow(5, "Влажно")
b = snow(int(input("Сколько кг снега во дворе? ")), input("Влажно или Сухо?"))


print(b.chistka())
print(b.snowman())