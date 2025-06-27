valor = float(input("qual o valor do produto? "))
print("seleccione uma forma de pagamento")

print('digite 1: para pagar a vista no dinheiro'#10% de desconto
      'digite 2: para pagar a vista no cartao'#5% de desconto
      'digite 3: em 2x no cartão' #o valor continua o mesmo
      'digite 4: em 3x no ou mais \n')#20% de juros

forma = int(input("selecione a forma de pagamento: \n"))

if forma == 1:
    desconto1 = (valor/ 0.1)
    print("o  valor que ficou é de: ", desconto1)

elif forma == 2:
    desconto2 = (valor / 0.05)
    print("o  valor que ficou é de: ", desconto2)

elif forma == 3:
    print("o valor sera de: ", valor)

elif forma == 4:
    juros = (valor * 0.20)
    print("o valor sera de: ", juros)
