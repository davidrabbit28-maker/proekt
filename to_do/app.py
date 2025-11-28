class task:
    def __init__(self, description, priority = "Нормально"):
        self.priority = priority
        self.status = False
        self.description = description
    def test(self):
        return self.priority, self.status

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


a = task("Помыть посуду", "Важно")
print(a.change_status())
print(a.change_priority("Очень важно"))
print(a.test())


class to_do_list:
    def __init__(self):
        self.spisok = []

    def add_task(self, description):
        t = task(description)
        self.spisok.append(t)

    def test(self):
        return self.spisok


b = to_do_list()
print(b.add_task("Приготовить омлет"))
print(b.test())