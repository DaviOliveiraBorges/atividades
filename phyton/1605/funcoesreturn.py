from random import *
from datetime import *

caracteres = "1234567890abcdefgh@#$*"
semana_brasil = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
semana_italia = ["lun", "mar", "ter", "gio", "van", "sab", "dom"]

def somar (a, b):
    return a+b

def gerar(qtde):
    senha = ""
    for n in range(qtde):
        senha+= choice(caracteres)
    return senha

def get_dia_da_semana(data,idioma):
    dia = data.weekday()
    if idioma == "br":
        return semana_brasil[dia]
    elif idioma == "it":
        return semana_italia[dia]
    else:
        return data.striftime("%a")

print(somar(5,10))
print(gerar(6))
data = datetime.now()
print(get_dia_da_semana(data, "br"))