while True:
    print("----------CALCULADORA----------")
    print("1 - SOMA")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")
    print("5 - POTENCIAÇÃO")
    print("6 - ENCERRAR PROGRAMA")
    op = int(input("Digite o número da operação que deseja realizar: "))

    if(op == 1):
        print("\nSOMA DE DOIS NÚMEROS")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = num1+num2
        print(f"Soma = {resultado}")
    elif op == 2:
        print("\nSUBTRAÇÃO DE DOIS NÚMEROS")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = num1-num2
        print(f"Subtração = {resultado}")
    elif op == 3:
        print("\nMULTIPLICAÇÃO DE DOIS NÚMEROS")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = num1*num2
        print(f"Multiplicação = {resultado}")
    elif op == 4:
        print("\nDIVISÃO DE DOIS NÚMEROS")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        print(f"Divisão = {resultado}")
        resultado = num1/num2
    elif op == 5:
        print("\nPOTÊNCIA DE UM NÚMERO")
        num1 = int(input("Digite a base: "))
        num2 = int(input("Digite o expoente: "))
        resultado = num1**num2
        print(f"Potência de {num1} elevado a {num2} é = {resultado}")
    elif op == 6:
        print("PROGRAMA ENCERRADO")
        break

    SN = int(input("\nRealizar outra operação?\n1 - Sim\n2 - Não\n--> "))
    if SN == 1:
        print("\n")
        continue
    else:
        print("PROGRAMA ENCERRADO")
        break