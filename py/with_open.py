import os as os 

file_name = "with_open.txt"
'''
print(f"Работа с файлом {file_name} началась")

with open(file_name, "w", encoding="utf-8") as wdo:
    wdo.write("Учимся писать на питоне")
    wdo.write("\nТеперь мы умеем писать на питоне")


print("запись закончена и можем запускать")

'''
# with open(file_name, "r", encoding="utf-8") as rdo:
#     print(rdo.read()) 
 

# with open(file_name, "a", encoding="utf-8") as ado:
#     ado.write("\nА вот этот текст мы добавили")


with open(file_name, "r", encoding="utf-8") as r2do:
    content = r2do.readlines()

# print(len(content))
shet = 1
inputik = input()
for i in content:
    
    if inputik in i:
        print(f"'{inputik}' находится на {shet} строке")
    shet += 1