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
        '''
        if self.status == False:
            self.status = True
        else:
            self.status = False
        '''
        self.status = not self.status
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

    def mark_task_done(self, aydi):
        try:
            aydi -= 1
            if aydi > len(self.spisok) or aydi <= 0:
                print(f"У вас всего {len(self.spisok)} задач")
            else:
                self.spisok[aydi].change_status()
                print("Статус изменен.")
        except ValueError:
            print("Это не число!")

    def delete_task(self, aydi_task):
        aydi_task -= 1
        if aydi_task > len(self.spisok) or aydi_task <= 0:
            print(f"У вас всего {len(self.spisok)} задач")
        else:
            deleted_task = self.spisok.pop(aydi_task)
            print(f"Вы удалили задачу '{deleted_task.description}' ")
# 
# 
# 
# 
# 
print("Мой список дел.")
 
to_do = to_do_list()

while True:
    print("1 - добавить, 2 - посмотреть весь список, 3 - изменить статус, 4 - удалить задачу, 5 - выйти")
    try:
        ask = int(input("Введите цифру: "))
        if ask == 1:
            desc_ask = input("Введите задачу: ")
            to_do.add_task(desc_ask)
            
        elif ask == 2:
            to_do.show_all_tasks()

        elif ask == 3:
            to_do.show_all_tasks()
            try:
                ask_aydi = int(input("Введите номер задачи: "))
            except ValueError:
                print("Это не число!")
            to_do.mark_task_done(ask_aydi)
        
        elif  ask == 4: 
            to_do.show_all_tasks()
            try:
                ask_aydi_to_delete = int(input("Введите номер задачи: "))
            except ValueError:
                print("Это не число!")
            to_do.delete_task(ask_aydi_to_delete)
        
        elif ask == 5:
            print("Вы вышли.")
            break
        else:
            print("Вы не ввели нужную цифру!")
    except ValueError:
        print("Вводите числа, а не буквы")