class task:
    def __init__(self, description, priority = "Нормально"):
        self.priority = priority
        self.status = False
        self.description = description

    def to_dict(self):
        slovar = {"Описание":self.description, 
                  "Приоритетность":self.priority, 
                  "Статус":self.status}
        return slovar
    
    def change_status(self):
        if self.status == False:
            self.status = True
        else:
            self.status = False
        return self.status


    def change_priority(self, x):
        self.priority = x
        return self.priority


    def show(self):
        if self.status:
            print(f"Выполнено! {self.description}")
        else:
            print(f"Не выполнено! {self.description}")


class to_do_list:
    def __init__(self):
        self.spisok = []

    def add_task(self, description):
        t = task(description)
        self.spisok.append(t)
        print("Задача добавлена.")

    def show_all_tasks(self):
        for i, task in enumerate(self.spisok, 1):
            print(i)
            task.show()
#  
# 
# 
# 
# 
print("Мой список дел.")
 
to_do = to_do_list()

while True:
    print("1 - добавить, 2 - посмотреть весь список, 3 - выйти")
    ask = int(input("Введите цифру: "))
    if ask == 1:
        desc_ask = input("Введите задачу: ")
        to_do.add_task(desc_ask)
        
    elif ask == 2:
        to_do.show_all_tasks()
    elif ask == 3:
        print("Вы вышли.")
        break
    else:
        print("Вы не ввели нужную цифру!")