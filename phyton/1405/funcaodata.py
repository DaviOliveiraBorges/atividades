from datetime import *
agora = datetime.now()
print("data completa: ", agora)
print("dia ", agora.day)
print("mes ", agora.month)
print("ano ", agora.year)
print("hora ", agora.hour)
print("minuto ", agora.minute)
print("segundo ", agora.second)

data = datetime(2019,12,31,23,59,59)

print("data completa: ", data)
print("dia da semana ", data.strftime("%A"))
print("numero da semana ", data.strftime("%U"))
print("nome do mes ", data.strftime("%B"))
diferenca = agora - data
print("diferença entre datas ", diferenca)
data30 = data + timedelta(days=30)
print("soma de 30 dias ", data30)