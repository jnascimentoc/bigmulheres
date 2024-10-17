# 1 Um pescador precisa pagar uma multa caso o peso dos 
#peixes exceda 100 quilos. Crie uma função para calcular a multa, se aplicável.
'''
peso = float(input("Insira o peso: "))

def calcula_multa():
    if peso > 100:
        multa = (peso / 3) + 1.5
        print(f'Você ultrapassou o peso permitido, pague: R$ {multa:.2f}')
    else:
       return print("Pode continuar a pescar!")

calcula_multa()
'''

# Crie um programa que faça a leitura da altura e do peso de N pessoas para o cálculo do IMC, 
#mostrando ao final a classificação de acordo com a tabela de IMC.


def calcula_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f'IMC: {imc:.2f}')
    if imc <= 18.5:
        print('Abaixo do peso')
    elif imc <= 24.9: 
        print('Peso normal')
    elif imc <= 29.9:
        print("Sobrepeso")
    elif imc <= 34.9:
        print("Obesidade grau I")   
    elif imc <= 39.9:
        print("Obesidade grau II (severa)")
    else:
        print("Obesidade grau III (mórbida)")

peso = float(input("Insira o peso: "))
altura = float(input("Insira a altura: "))

calcula_imc(peso,altura)

# 3) Crie funções que mostrem um cardápio de um restaurante (pelo menos 4 itens) e que permitam 
#realizar pedidos e fechar a conta.

