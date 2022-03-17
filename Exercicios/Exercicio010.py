#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
fahre = (celsius * 1.8) + 32
print(f"{celsius}°C é igual a {fahre}°F")