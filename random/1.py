names = ["David", "Ilya", "Vladimir", "Donald"]
def onlynames(names):
    names_on_d = []
    for i in names:
        if i[0] == "D":
            names_on_d.append(i)
    return names_on_d

def sumnames(names):
    sum = 0
    for i in names:
        sum += len(i)
    return sum



print(onlynames(names))
print(sumnames(names))