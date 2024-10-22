# 1 Um pescador precisa pagar uma multa caso o peso dos 
#peixes exceda 100 quilos. Crie uma função para calcular a multa, se aplicável.

peso = float(input("Insira o peso: "))

def calcula_multa():
    if peso > 100:
        multa = (peso / 3) + 1.5
        print(f'Você ultrapassou o peso permitido, pague: R$ {multa:.2f}')
    else:
       return print("Pode continuar a pescar!")

calcula_multa()


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
def exibir_cardapio(cardapio):
    print("\n===== CARDÁPIO =====")
    for item, preco in cardapio.items():
        print(f"{item.capitalize():<20} R$ {preco:.2f}")
    print("====================\n")
def cardapio():
    return {
        'hamburguer': 15,
        'pizza': 30,
        'salgadinho': 36,
        'cachorro quente': 8,
        'batata frita': 6,
        'refrigerante': 4
    }

def realizar_pedido(cardapio):
    pedido = {}
    while True:
        item = input('Digite o item (ou "sair" para fechar o pedido): ').strip().lower()
        if item == 'sair':
            break
        if item not in cardapio:
            print('Item não encontrado. Tente novamente.')
            continue
        quantidade = int(input('Digite a quantidade: '))
        pedido[item] = quantidade
    return pedido

def calcular_total(cardapio, pedido):
    total = sum(cardapio[item] * qtd for item, qtd in pedido.items())
    return total

def fechar_conta(total):
    print(f'Total: R$ {total:.2f}')
    pagamento = float(input('Valor pago: R$ '))
    troco = pagamento - total
    print(f'Troco: R$ {troco:.2f}')

# Fluxo do programa
menu = cardapio()
exibir_cardapio(menu)

pedido = realizar_pedido(menu)
total = calcular_total(menu, pedido)
fechar_conta(total)
