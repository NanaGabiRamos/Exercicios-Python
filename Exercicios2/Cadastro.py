# Função menu de escolha do usuário
def menu():
    print("Selecione uma opção:")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Sair")

# Função cadastrar
def cadastrar(nome, data_nasc, endereco, lista):
    registro = {"Nome": nome,"Data_Nascimento": data_nasc, "Endereco": endereco}
    lista.append(registro)

# Menu principal
usuario = input("Entre com o seu nome: ")
print(f"Seja Bem-vindo {usuario}!\n")
lista = []
while True:
    menu()
    opcao = int(input("--> "))
    if opcao in [1, 2, 3]:
        if opcao == 1:  # Cadastrar
            nome = ""
            data_nasc = ""
            dia = ""
            mes = ""
            ano = ""
            endereco = ""

            while nome == "":
                nome = input("Coloque o nome: ")
            while data_nasc == "":
                print("Coloque a data de nascimento")
                dia = input("Dia: ")
                mes = input("Mês: ")
                ano = input("Ano: ")
                data_nasc = (f"{dia}/{mes}/{ano}")
            while endereco == "":
                endereco = input("Coloque o endereço: ")

            cadastrar(nome, data_nasc, endereco, lista)
            print("Sucesso! Cadastrado!")
        elif opcao == 2:  # Listar
            print("\n-------CADASTROS-------")
            for item in lista:
                print(item)
        elif opcao == 3:  # Sair
            print("Saindo do sistema...")
            break
    else:
        print("Opção Inválida!")