# 3- Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
raio = float(input("Digite o raio do circulo:"))
result = math.pi * (raio ** 2)
print(f"A area do circulo é: {result} e arredondado com duas casas decimais: {round(result, 2)}")
