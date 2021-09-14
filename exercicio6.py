"""
6- Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre
a temperatura em graus Celsius.
"""
fah = float(input("Digite uma temperatura em fahrenheit para conversão:"))
celsius = round((fah - 32) / 1.8, 2)
print(f"A temperatura convertida para celsius: {celsius}")

