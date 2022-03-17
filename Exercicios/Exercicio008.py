#8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
quantSalario = float(input("Quanto você ganha por hora: "))
quantHoras = int(input("Horas trabalhadas no mês: "))
salario = quantSalario * quantHoras
print(f"Salário  = {salario}")