###ATIVIDADE###
# Crie um código que seja capaz de ler e armazenar uma sequência de 20 números pares e 20 números ímpares.
# Obs: utilize estruturas de repetição para fechar esse conjuntode números.

numeros = []
pares = []
impares = []
contador_par = 0
contador_impar = 0

while contador_par < 20 or contador_impar < 20:
    numero = int(input("Digite um número: "))
    if numero in numeros:
        print("Esse número já foi inserido. Tente novamente.")
        continue
    numeros.append(numero)

    if numero % 2 == 0 and contador_par < 20:
        pares.append(numero)
        contador_par += 1
    elif numero % 2 != 0 and contador_impar < 20:
        impares.append(numero)
        contador_impar += 1

# Exibe os resultados
print("Números:", numeros)
print("Pares:", pares)
print("Ímpares:", impares)