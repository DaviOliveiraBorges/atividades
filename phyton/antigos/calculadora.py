HIST = " "
def calcula(expr):
    try:
        return eval(expr)
    except:
        print("experssao invalida")
        return None

def historico(expr, res):
    global HIST
    if res is not None:
        HIST += "\n\n" + expr
        HIST += "\n" + str(res)

def principal():
    while True:
        print("informe a expressao matematica")
        print("(h para o historico, s para sair)")
        expr = input()
        if expr.lower() == 's':
            break
        if expr.lower() == 'h':
            print(HIST, '\n')
        else:
            res = calcula(expr)
            historico(expr, res)
            print(res, '\n')

if __name__ == "__main__":
    principal()