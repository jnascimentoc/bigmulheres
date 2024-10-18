#Atividade assistida

'''Criem quatro funções para cada uma das operações aritméticas fundamentais (soma, subtração, multiplicação 
e divisão). Cada função deve receber dois números como parâmetros e retornar o resultado apropriado.
Em seguida, todas as funções devem ser integradas em um único programa: 
criem uma nova função para gerar números aleatórios e aplicá-los às operações anteriores.
'''
#Resolução:
 
#Funções Matemáticas:

def somar(a,b):
    return a+b

def subtrair(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b != 0:
        return a/b
    else:
        return "Divisões por zero não são permitidas."

print(somar(40,20))
print(subtrair(40,20))
print(multiplicar(40,20))
print(int(dividir(40,20))) #forçar o resultado a ser inteiro

import random

def gerando_numeros(quantidade,valor_minimo,valor_maximo):
    return [random.randint(valor_minimo,valor_maximo) for i in range(quantidade)]

numeros=gerando_numeros(2,1,100)
n1,n2= numeros[0],numeros[1]

print(numeros)
print(f"Números gerados:{n1} e {n2}.")
print(f"Soma:{somar(n1,n2)}")
print(f"Subtração:{subtrair(n1,n2)}")
print(f"Multiplicação:{multiplicar(n1,n2)}")
print(f"Divisão:{dividir(n1,n2)}")

import calculadora
from calculadora import somar
print(somar(2,8))

#Tratamento de excessões (Try e Except)
def dividisao(a,b):
    try:
        resultado = a/b
    except ZeroDivisionError:
        return "Divisão por zero não é permitida."
    else:
        print(f"O resultado da divisão é {resultado}")
    finally:
        print("Operação finalizada")

#Teste
dividisao(20,2)
dividisao(20,0)
dividisao(2,5)
    