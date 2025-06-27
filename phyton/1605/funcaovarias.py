from math import *
from random import *
from datetime import *

def get_area_retangulo(lado1, lado2):
    return lado1 *lado2

def get_area_circulo(raio):
    return pi * raio ** 2

def get_lista_numeros(qtde):
    lista = []
    for n in range(qtde):
        lista.append(randint(1, 100))
    return lista

def data_futura(data,dias):
    return data + timedelta(days=dias)


def data_anterior(data,semanas):
    return data + timedelta(weeks=semanas)


def minuto_futuro(data,minuto):
    return data + timedelta(minutes=minuto)


def hora_anterior(data,hora):
    return data + timedelta(hours=hora)


formato = "%d/%m/%Y - %H:%M:%S"
data = datetime.now()

print(get_area_retangulo(2,4))
print(get_area_circulo(5))
print(get_lista_numeros(10))
print(data_futura(data,10).strftime(formato))
print(data_anterior(data,2).strftime(formato))
print(minuto_futuro(data,20).strftime(formato))
print(hora_anterior(data,10).strftime(formato))