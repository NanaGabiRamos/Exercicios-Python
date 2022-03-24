from fractions import Fraction

# Função menu de escolha do usuário
def menu():
    print("Selecione uma opção:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

# Função para imprimir tabuada de adição
def adicao():
    for i in range(11):
        for j in range(11):
            print(f"{i} + {j} = {i+j}")
        print("\n")

# Função para imprimir tabuada de subtração
def subtracao():
    for i in range(11):
        for j in range(11):
            print(f"{i} - {j} = {i-j}")
        print("\n")

# Função para imprimir tabuada de multiplicação
def multiplicacao():
    for i in range(11):
        for j in range(11):
            print(f"{i} x {j} = {i*j}")
        print("\n")

# Função para imprimir tabuada de Divisão
def divisao():
    for i in range(11):
        for j in range(11):
            if(i == 0 or j == 0):
                print(f"{i} / {j} = 0")
            else:
                print(f"{i} / {j} = {Fraction(i,j)}")
        print("\n")

# Função de chamada das funções
def funcoesCalculo(opcao):
    int(opcao)
    if opcao == 1:
        adicao()
    elif opcao == 2:
        subtracao()
    elif opcao == 3:
        multiplicacao()
    elif opcao == 4:
        divisao()