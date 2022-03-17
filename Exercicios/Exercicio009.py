#9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).
Fahre = float(input("Digite a temperatura em Fahrenheit: "))
celsius = 5 * ((Fahre - 32) / 9)
print(f"{Fahre}°F é igual a {celsius}°C")