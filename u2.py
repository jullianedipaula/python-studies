#EXERCÍCIO 1

n1 = int(input("Digite um número: "))

import math
if n1>=1:
    print(f"A raiz quadrada desse número é: {math.sqrt(n1)}")
elif n1<=-1:
    print("Número invalido.")

#EXERCÍCIO 2

n1 = int(input("Digite um número: "))

import math
if n1>=1:
    print(f"O quadrado desse número é: {n1**2}")
    print(f"A raiz quadrada desse número é: {math.sqrt(n1)}")
    

#EXERCÍCIO 3

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

if n1==n2:
    print("Os dois números são iguais!")
elif n1>n2:
    print(f"O maior número é: {n1}")
elif n2>n1:
    print(f"O maior número é: {n2}")

#EXERCÍCIO 4

sal = float(input("Digite o valor do seu salário: R$"))
emp = float(input("Digite o valor da parcela do empréstimo: R$"))

if emp >= 1.2 * sal:
    print("Empréstimo não concedido!")
else:
    print("Empréstimo concedido!")

#EXERCÍCIO 5

lab = float(input("Digite a nota do laboratório: "))
avs = float(input("Digite a nota da avaliação semestal: "))
avf = float(input("Digite a nota da avaliação final: "))

soma = ((lab * 2) + (avs * 3) + (avf * 5)) / 10

if soma >=5:
    print("Aprovado")
elif soma >= 3 and soma < 5:
    print("Recuperação")
else:
    print("Reprovado")

#EXERCÍCIO 6 

num = int(input("Digite um número: "))

if num == 1:
    print("Hoje é Domingo.")
elif num == 2:
    print("Hoje é Segunda-Feira.")
elif num == 3:
    print("Hoje é Terça-Feira.")
elif num == 4:
    print("Hoje é Quarta-Feira.")
elif num == 5:
    print("Hoje é Quinta-Feira.")
elif num == 6:
    print("Hoje é Sexta-Feira.")
elif num == 7:
    print("Hoje é Sábado.")
else:
    print("Comando inválido.")

#EXERCÍCIO 7

num = int(input("Digite um número: "))

if num == 1:
    print("Janeiro")
elif num == 2:
    print("Fevereiro")
elif num == 3:
    print("Março")
elif num == 4:
    print("Abril")
elif num == 5:
    print("Maio")
elif num == 6:
    print("Junho")
elif num == 7:
    print("Julho")
elif num == 8:
    print("Agosto")
elif num == 9:
    print("Setembro")
elif num == 10:
    print("Outubro")
elif num == 11:
    print("Novembro")
elif num == 12:
    print("Dezembro")
else:
    print("Comando inválido.")

#EXERCÍCIO 8

num = int(input("Digite um número: "))

if num % 3 == 0 and num % 5 == 0:
    print("Este número é divisível por 3 e por 5")
elif num % 3 == 0:
    print("Este número é divisível por 3")
elif num % 5 == 0:
    print("Este número é divisível por 5")
else:
    print("Comando inválido")

#EXERCÍCIO 9

cmd = int(input("Escolha uma das opções: "))

if cmd == 1:
    n1 = float(input("Escolha um número: "))
    n2 = float(input("Escolha um número: "))
    print(f"A soma dos dois números é: {n1 + n2}")
elif cmd == 2:
    s1 = float(input("Escolha um número: "))
    s2 = float(input("Escolha um número: "))
    if s1>s2:
        print(f"A diferença entre esses número é: {s1 - s2}")
    else:
        print(f"A diferença entre esses numeros é: {s2 - s1}")
elif cmd == 3:
    p1 = float(input("Escolha um número: "))
    p2 = float(input("Escolha um número: "))
    print(f"O produto desses números é: {p1 * p2}")
elif cmd == 4:
    d1 = float(input("Escolha um número: "))
    d2 = float(input("Escolha um número: "))
    if d2 > 0:
        print(f"A divisão desses números é: {d1 / d2}")
else:
    print("Comando inválido!")

#EXERCÍCIO 10

idade = int(input("Digite a sua idade: "))
trab = int(input("Digite o seu tempo de contribuição: "))

if idade >= 65 and trab >=0:
    print("Pode se aposentar!")
elif idade < 65 and trab >= 30:
    print("Pode se aposentar!")
elif idade <= 60 and trab >= 25:
    print("Pode se aposentar!")
else:
    print("Não pode se aposentar!")
    
#EXERCÍCIO 11

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

import math

delta = b ** 2 - (4 * a * c)

x1 = - b + (math.sqrt(delta)) / (2 * a)
x2 = - b - (math.sqrt(delta)) / (2 * a)

if a == 0:
    print("Não é uma equação de 2° grau")
elif delta < 0:
    print("Não existe raiz")
elif delta == 0:
    print("Raiz única")
elif delta > 0:
    print(f"x'{x1} e x''{x2}")