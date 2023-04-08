#EXERCÍCIO 1

c = float(input("Digite a temperatura em Celsius: "))

f = c * (9/5) + 32

print(f"A temperatura em Fahrenheit é: {f}")

#EXERCÍCIO 2

f = float(input("Digite a temperatura em Fahrenheit: "))

c = 5 * (f - 32) / 9

print(f"A temperatura em Celsius é: {c}")

#EXERCÍCIO 3

k = float(input("Digite a temperatura em Kelvin: "))

c = k - 273.17

print(f"A temperatura em Celsius é: {c}")

#EXERCÍCIO 4

km = float(input("Digite a velcidade em km/h: "))

m = km / 3.6

print(f"A velocidade em m/s é: {m}")

#EXERCÍCIO 5

m = float(input("Digite a distância em milhas: "))

k = 1.61 * m

print(f"A distância em quilômetros é: {k}")

#EXERCÍCIO 6

rad = int(input("Digite o ângulo em radianos: "))

g = (rad * 130) / 314

print(f"O ângulo em graus é: {g}")

#EXERCÍCIOS 7

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

print(f"A soma dos quadrados é: {n1**2 + n2**2 + n3**2}")

#EXERCÍCIOS 8

real = float(input("Digite o valor: R$"))
cdolar = float(input("Digite a cotação do dolar: $"))

print(f"O valor em dólares é: {real/cdolar}")

#EXERCÍCIOS 9

n1 = int(input("Digite um número: "))

print(f"O seu antecessor é: {n1-1}")
print(f"O seu sucessor é: {n1+1}")

#EXERCÍCIOS 10

a = int(input("Cateto maior: "))
b = int(input("Cateto menor: "))

import math

hip = math.sqrt(a**2 + b**2)

print(f"A hipotenusa é: {hip}")

#EXERCÍCIOS 11

valor = float(input("Digite o valor do produto: R$"))

print(f"O valor final é: R${valor * 0.88}")

#EXERCÍCIOS 12

print(f"O primeiro ganhador ganhará: {780000 * 0.46}")
print(f"O segundo ganhador ganhará: {780000 * 0.32}")
print(f"O terceiro ganhador ganhará: {780000 * 0.22}")