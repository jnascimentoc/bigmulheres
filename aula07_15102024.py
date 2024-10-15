lista1=[2,4,6,8,10]
lista1.remove(6) #Remove o número 4 da minha lista
lista1.remove(lista1[2]) #Remove o elemento que está na posição 1 da minha lista
print(lista1)

lista2=lista1.insert(2,1000)
print(lista2) #none
lista2 = lista1.copy()
print(lista2)

lista3 = lista1.copy()
lista4 = lista1.copy()
lista3.clear()
print(lista3) #[]
lista4.pop(0) #estou removendo o elemento de 'índice zero' da minha lista.
print(lista4) #[4, 1000, 10]
lista4.sort() #coloquei meus elementos da lista em ordem crescente.
print(lista4) #[4, 10, 1000]
lista4.reverse() #Altera a ordem dos elementos
print(lista4)

frutas = ['uva', 'maça', 'carambola','melancia', 'uva', 'carambola', 'uva']
frutas.sort()
print(frutas)

#TUPLAS são mutáveis: podemos consultar e reordenar tuplas

frutas = tuple(frutas) #convertendo a lista e tupla
frutas.sort()
print(frutas)
frutas2=tuple(frutas)
print(frutas2.index('uva'))
print(frutas2.count('uva'))

#DICIONÁRIOS são mutáveis: podemos consultar, adicionar, alterar e excluir pares de chave-valor

estados = {'RJ': 'Rio de Janeiro',
           'SP': 'São Paulo',
           'MG': 'Minas Gerais',
           'ES': 'Espírito Santo'}
print(estados)




