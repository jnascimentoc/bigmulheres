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
