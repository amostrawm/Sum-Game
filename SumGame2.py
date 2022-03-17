from SumGameInterface import interface
from random import randint

valor_final = randint(20, 30)
v1 = randint(1, 5)
v2 = randint(6, 10)
v3 = randint(11, 15)
while True:
    interface(valor_final, v1, v2, v3)
