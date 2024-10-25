#Atividades práticas com if/else e switch/case:

#Exercício 1
'''
1) Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. 
Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. Considere que 
a potência necessária é de 3 watts por metro quadrado e a cada 3 m² existe um bocal para uma lâmpada;
'''
def validar_entrada(mensagem):
    while True:
        valor = float(input(mensagem))
        if valor > 0:
            return valor
        else:
            print("⚠️ Digite um valor válido.")

def potencia():
    area = largura * comprimento
    potencia_real = potencia_lampada * 3
    num_lampadas = int(potencia_real/potencia_lampada)
    bocais = int(area /3)

    print ("--------------------------------------")
    print("☑️ Número de lâmpadas necessárias:", int(num_lampadas))
    print("☑️ Número de bocais disponíveis:", int(bocais)) #Impressão final 
    print ("--------------------------------------")

# Entrada de dados
potencia_lampada = validar_entrada('Digite a potência da lâmpada (somente números): ')
largura = validar_entrada('Digite a largura do cômodo (em metros): ')
comprimento = validar_entrada('Digite o comprimento do cômodo (em metros): ')
# Chamada da função para calcular o número de lâmpadas
potencia()


#Exercicio2
'''
2) Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e altura), calcular e escrever a quantidade de 
caixas de azulejos para se colocar em todas as suas paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa 
de azulejos possui 1,5 m²;
'''
#Entrada de dados | Utilizei a função validar entrada já criada no exercício 1
largura_cozinha = validar_entrada('Digite a largura da cozinha: ')           
comprimento_cozinha = validar_entrada('Digite o comprimento da cozinha: ')

area_cozinha = float(largura_cozinha * comprimento_cozinha)
azulejos = 1.5
necessarios = area_cozinha / azulejos

if necessarios < 1:
    print("Será necessária apenas 1 caixa de azuleijos.")
else:
    print("Serão necessárias: ", necessarios, "caixas.")

#Exercicio 3
'''
3) Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de R$ 4,87, escreva um 
programa para ler: a marcação do odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de combustível gasto e o 
valor total (R$) recebido dos passageiros. Calcular e escrever: a média do consumo em km/L e o lucro (líquido) do dia;
'''
# Preço do combustível
preco_combustivel = 4.87


def calculo():
    distancia_percorrida = odometro_fim - odometro_inicio           #Distância percorrida
    consumo_medio = distancia_percorrida / litros_gastos            #Consumo médio em km/L
    custo_combustivel = litros_gastos * preco_combustivel           #Custo do combustível
    lucro_liquido = valor_recebido - custo_combustivel              #Lucro líquido
   
    print(f"Média de consumo: {consumo_medio:.2f} km/L")
    print(f"Lucro líquido do dia: R$ {lucro_liquido:.2f}")

# Entrada de dados | #Utilizei a função validar entrada já criada no exercício 1
odometro_inicio = validar_entrada('Digite a marcação do odômetro (km) no início do dia: ')
odometro_fim = validar_entrada('Digite a marcação do odômetro (km) no final do dia: ')
litros_gastos = validar_entrada('Digite o número de litros de combustível gasto: ')
valor_recebido = validar_entrada('Digite o valor total (R$) recebido dos passageiros: ')

# Verificação dos dados de entrada usando if/else
while True:
    if odometro_fim < odometro_inicio:
        print("A marcação do odômetro no final do dia não pode ser menor que no início.")
    elif litros_gastos <= 0:
        print("O número de litros de combustível deve ser maior que zero.")
    elif valor_recebido < 0:
        print("O valor recebido dos passageiros deve ser maior ou igual a zero.")
    else:
        calculo()
        break

#Exercicio 4
'''
4) Escreva um programa que leia o código de origem de um produto e imprima na tela a região de sua procedência, conforme a tabela que foi passada.
Observação: caso o código não seja nenhum dos especificados, o produto deve ser encarado como “Importado”;
'''
#Função STARTSWITH(), para verificar se o valor digitado é igual ao valor no parâmetro da função

def identificar_regiao(codigo):
    if codigo.startswith("1"):
        return "☑️ Região Sul"
    elif codigo.startswith("2"):
        return "☑️ Região Norte"
    elif codigo.startswith("3"):
        return "☑️ Região Leste"
    elif codigo.startswith("4"):
        return "☑️ Região Oeste"
    elif codigo.startswith("5"):
        return "☑️ Região Nordeste"
    elif codigo.startswith("6"):
        return "☑️ Região Sudeste"
    elif codigo.startswith("7"):
        return "☑️ Região Centro-Oeste"
    elif codigo.startswith("8"):
        return "☑️ Região Noroeste"
    else:
        return "🌍 Importado" 
    
codigo_produto = input("Digite o código de origem do produto: ")

# Chama a função e imprime a região de procedência
regiao = identificar_regiao(codigo_produto)
print ("--------------------------------------")
print(f"A região de procedência do produto é: {regiao}")
print ("--------------------------------------")


#Exercício 5
'''
5) Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, 
deve ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa substitui a 
nota mais baixa entre as duas primeiras avaliações. Escrever a média e mensagens que indiquem se o estudante foi aprovado, reprovado ou se 
está em exame, de acordo com as informações abaixo: 
Aprovado: média >= 6.0, Reprovado: média < 3.0, Exame: média >= 3.0 e < 6.0;
'''
def calcular_media(av1, av2, optativa):
#Se o aluno fez a optativa (não é -1), substituir a menor nota
    if optativa != -1:
        menor_nota = min(av1, av2)  #Encontra a menor nota
        if menor_nota == av1:
            av1 = optativa          #Substitui a AV1 
        else:
            av2 = optativa          #Substitui a AV2 

    media = (av1 + av2) / 2         #Média final
    return media

def verificar_situacao(media):
    if media >= 6.0:
        return "✅ Aprovad"
    elif media < 3.0:
        return "❌ Reprovado"
    else:
        return "😣 O aluno deverá realizar o exame final"

# Entrada de dados
av1 = float(input("Digite a nota da Avaliação 1: "))
av2 = float(input("Digite a nota da Avaliação 2: "))
optativa_resposta = input("O aluno realizou a optativa (S/N)? ").upper()

if optativa_resposta == 'S':
    optativa = float(input("Digite a nota da Avaliação Optativa: "))
else:
    optativa = -1  # Caso o aluno não tenha feito a optativa

media = calcular_media(av1, av2, optativa)  #Calcula a média
situacao = verificar_situacao(media)        #Verifica a situação

# Exibe o resultado
print ("--------------------------------------")
print(f" Média do semestre: {media:.2f}")
print ("--------------------------------------")
print(f"Situação do estudante: {situacao}")
print ("--------------------------------------")


#Exercicio 6
'''
6) Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.
'''

def verificador():
    if num >= 0:
        print("O número", num, "é positivo")
    else:
        print("O número", num, "é negativo")

num = float(input("Digite um número: "))
verificador()