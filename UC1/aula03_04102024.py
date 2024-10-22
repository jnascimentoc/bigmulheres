print("Teste para verificar se você está com febre")
temperatura = float(input('Digite sua temperatura: '))
#Teste lógico

if temperatura <37.5:
    print("Você não esta com febre!")
elif temperatura == 37.5:
    print("Você está febril")
else:
    print("Você está com febre!")                    