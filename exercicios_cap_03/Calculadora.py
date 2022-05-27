# Interface incial sobre operações disponíveis
def interfaceInicial():
    print("\n---------------------Calculadora Python---------------------\n")
    print("Digite um dos seguintes valores para escolher a operação entre dois números: ")
    print("\n 1 - Soma")
    print(" 2 - Subtração")
    print(" 3 - Multiplicação")
    print(" 4 - Divisão")
    
# Função onde realiza operação entre dois valores
def coletarValores(op):
    valor1 = int(input("\nDigite o primeiro valor: "))
    valor2 = int(input("\nDigite o segundoo valor: "))
    nomeOp = ""

    if op == 1:
        nomeOp = "+"
        result = valor1 + valor2
    elif op == 2:
        nomeOp = "-"
        result = valor1 - valor2
    elif op == 3:
        nomeOp = "x"
        result = valor1 * valor2
    else:
        nomeOp = "/"
        result = round((valor1 / valor2),2)
        
    print(f"\n {valor1} {nomeOp} {valor2} = {result}")
    
    ret = int(input("\nDigite 1 para realizar ou qualquer outro valor para finalizar: "))
    if ret == 1:
            print("\n---------------------------------------------------------\n")
            operacao()
    else:
        print("\nCalculadora encerrada!")
        pass
        
# Função onde recebe o sinal da operação
def operacao():
    op = int(input("\nDigite a opção (1/2/3/4): "))
    
    if op > 0 and op <5:
        coletarValores(op)
    else:
        op = int(input("\nOpção invalida, digite outro valor inválido para finalizar, ou escolha uma opção válida (1/2/3/4): "))
        if op > 0 and op <5:
            coletarValores(op)
        else:
            print("\nCalculadora encerrada!")
            
# Chamada das funções
interfaceInicial()
operacao() 
    