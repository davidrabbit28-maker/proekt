def test_func(x):
  lst = [1, 2, 'a'] # упорядоченная, изменяемая коллекция
  dct = {'key': 'value'} # неупорядоченная коллекция пар "ключ-значение", ключи должны быть неизменяемыми
  st = {1, 2, 3} # неупорядоченная коллекция уникальных элементов
  tpl = (1, 2, 'a') # упорядоченная, неизменяемая коллекция
  frozenst = frozenset([1, 2, 3]) # неизменяемая версия set
  
  # ________________________________________________________

  if type(x) == str:
    intersting_bam = [i for i in x if i.lower() == i]
  else:
    intersting_bam = "I am not sure about type of x"

  return intersting_bam


print(test_func("Hello world")
