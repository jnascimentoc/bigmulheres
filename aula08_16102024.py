#Funções
def somar(parametro1,parametro2):
    return parametro1 + parametro2

def subtrair(parametro1,parametro2):
    return parametro1 - parametro2

def multiplicar(parametro1,parametro2):
    return parametro1 * parametro2

def dividir(parametro1,parametro2):
    return parametro1 // parametro2

print(somar(20,30))
print(subtrair(20,30))
print(multiplicar(20,30))
print(dividir(20,30))

###Exemplo de melhoramento de códigio
'''
5) Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, 
deve ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa substitui a 
nota mais baixa entre as duas primeiras avaliações. Escrever a média e mensagens que indiquem se o estudante foi aprovado, reprovado ou se 
está em exame, de acordo com as informações abaixo: 
Aprovado: média >= 6.0, Reprovado: média < 3.0, Exame: média >= 3.0 e < 6.0;
'''

def boletim():
    # Ler as notas das avaliações normais
    av1 = float(input("Digite a nota da Avaliação 1: "))
    av2 = float(input("Digite a nota da Avaliação 2: "))
    optativa = float(input("Digite a nota da Avaliação Optativa (ou -1 caso não tenha feito): "))
    
    # Substituir a menor nota caso a optativa seja fornecida
    if optativa != -1:
        menor_nota = min(av1, av2)
        if menor_nota == av1:
            av1 = optativa
        else:
            av2 = optativa
    
    # Calcular a média
    media = (av1 + av2) / 2
    
    # Definir a situação do estudante
    if media >= 6.0:
        return "✅ Aprovado"
    elif media < 3.0:
        return "❌ Reprovado"
    else:
        return "😣 O aluno deverá realizar o exame final"
    
print(boletim())

#Atividade Assistida
def multiplica():
    # Ler os valores
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    resultado = numero1 * numero2
    return resultado

print(multiplica())