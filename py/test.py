# print("Hello World!")

# def test(*args):
#     itog = ""
#     for i in args:
#         itog += i
#     return itog


# print(test("привет", "утро", "ура"))

import time

def second(s):
  def vnutrenost():
    start = time.time()
    s()
    end = time.time()
    print(f"{end - start}")
  return vnutrenost

@second
def calc():
  shet = 0
  for i in range(100000000000):
    shet += i
  return shet

calc()