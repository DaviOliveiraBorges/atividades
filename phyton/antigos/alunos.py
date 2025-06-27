from random import choice
from random import shuffle

nomes = ['vaz', 'indio vitor', 'manu', 'lulucianus', 'davidson']
escolhido = choice(nomes)
print("o nome escolhido é ", escolhido)
print(nomes)
shuffle(nomes)
escolhido = choice(nomes)
print("o nome escolhido é ", escolhido)
print(nomes)