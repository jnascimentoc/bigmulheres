'''Leia três pares de números inteiros fornecidos pelo usuário, 
calcule e imprima a soma de cada par separadamente. 
Utilize  tratamento de erros para garantir que os valores inseridos sejam válidos e, 
se o número for ÍMPAR, ter uma exceção personalizada.
'''

for i in range(1, 4):
    print(f"\nPar {i}:")
    
    while True:
        try:
            num1 = int(input("Digite o primeiro número: "))
            break
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

    while True:
        try:
            num2 = int(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

    soma = num1 + num2

    if soma % 2 != 0:
        print(f"A soma do Par {i} é: {soma} (A soma é um valor ímpar)")
    else:
        print(f"A soma do Par {i} é: {soma}")