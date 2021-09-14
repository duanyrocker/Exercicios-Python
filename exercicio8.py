"""
8- Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
- o produto do dobro do primeiro com metade do segundo .
- a soma do triplo do primeiro com o terceiro.
- o terceiro elevado ao cubo.
"""
number_one = int(input("Digite um numero inteiro:"))
number_two = int(input("Digite outro numero inteiro:"))
number_three = float(input("Digite um numero real:"))
result = (number_one * 2) * (number_two / 2)
result_two = (number_one * 3) + number_three
result_three = number_three ** 3
print(f"O produto do dobro do primeiro com metade do segundo numero: {result}."
      f"A soma do triplo do primeiro com o terceiro {result_two}, o terceiro elevado ao cubo {result_three}.")
