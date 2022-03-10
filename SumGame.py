from random import randint

finalValue = int()
sumValue = int()
randomValue1 = int()
randomValue2 = int()
randomValue3 = int()
clear = "\n" * 10

print("[Jogo da Soma]")
print("Você tem que somar valores inteiros até chegar no valor mostrado.")
print("Porém os valores são escolhidos aleatoriamente.")
print("E se ao somar, voce ultapassar o valor apresentado, você perde o jogo.")
print("Continuar? (y/n)")
confirmInput = input()
print(clear)
print("Iniciando Jogo da Soma...")
if confirmInput == 'y':
    while True:
        finalValue = randint(20, 30)
        print("Alcance o valor: [" + str(finalValue) + "]")
        while True:
            randomValue1 = randint(1, 5)
            randomValue2 = randint(6, 10)
            randomValue3 = randint(11, 15)
            print("Valores disponíveis: ")
            print("[" + str(randomValue1) + "]" + "[" + str(randomValue2) + "]" + "[" + str(randomValue3) + "]")
            inputValue = int(input())
            if inputValue in [randomValue1, randomValue2, randomValue3]:
                sumValue += inputValue
            else:
                print("Você inseriu um valor que não está disponível!")
                print("Reiniciando o jogo!")
                sumValue = 0
                break
            if sumValue < finalValue:
                print(clear)
                print("Alcance o valor: [" + str(finalValue) + "]")
                print("Valor somado até agora: [" + str(sumValue) + "]")
                continue
            elif sumValue == finalValue:
                print(clear)
                print("Você alcançou o valor final [" + str(finalValue) + "] e ganhou o jogo!")
                sumValue = 0
                print("Quer reiniciar o jogo? (y/n)")
                confirmInput = input()
                if confirmInput == 'y':
                    sumValue = 0
                    print(clear)
                    break
                else:
                    exit()
            elif sumValue > finalValue:
                print(clear)
                print("Você ultrapassou o valor final e perdeu!")
                print("Valor final era [" + str(finalValue) + "] sua soma foi [" + str(sumValue) + "]")
                print("Quer reiniciar o jogo? (y/n)")
                confirmInput = input()
                if confirmInput == 'y':
                    sumValue = 0
                    print(clear)
                    break
                else:
                    exit()