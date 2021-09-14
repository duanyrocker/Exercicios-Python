# 7- Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
celsius = float(input("Digite uma temperatura em celsius para conversão:"))
fah = round((celsius * 1.8) + 32, 2)
print(f"A temperatura convertida para fahrenheit: {fah}")
