# Fazer um programa que imprima a tabuada do 0 até o 10
# Obs: O script denominado como Funcoes presente em
# github.com/NanaGabiRamos/Exercicios-Python/tree/main/Exercicios2
# está sendo utilizado para fazer a importação presente na linha 5

from Funcoes import funcoesCalculo
from Funcoes import menu

usuario = input("Entre com o seu nome: ")
print(f"Seja Bem-vindo {usuario}!\n")
while True:
  menu()
  op = int(input("--> "))
  if op in [1,2,3,4,5]:
    if op == 5:
      print("Saindo do sistema...")
      break
    print("\n----------Resultados----------")
    funcoesCalculo(op)
  else:
    print("Opção invalida")
