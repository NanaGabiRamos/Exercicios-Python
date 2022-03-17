#4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
soma = 0
for i in range(4):
  nota = float(input(f"Digite a nota {i+1}: "))
  soma += nota
print(f"Media = {soma/4}")