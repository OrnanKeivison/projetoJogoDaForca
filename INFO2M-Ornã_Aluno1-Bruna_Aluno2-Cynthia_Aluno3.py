from time import sleep
from random import choice
from os import system

palavras = ['COMPUTADOR', 'ALGORITMOS', 'PYTHON', 'CODINGLAND', 'HTML', 'CSS','ARDUINO']

palavra = choice(palavras)

estadoAtual = ['_'] * len(palavra)
letrasEscolhidas = []

erros = 0

print('FORCA DE PALAVRAS')
print('Seu objetivo é tentar acertar a palavra secreta')
sleep(2)
print('Você terá que tentar uma letra por vez')
sleep(2)
print('Caso você acerte, a letra será colocada na palavra para que você chegue mais perto de acertar')
sleep(2)
print('você pode errar 5 vezes')
sleep(2)
print('o tema das palavras é programação')
sleep(2)

sleep(3)
system('cls') or None

while True:
    letra = input('Digite uma letra: ')
    letra = letra.upper()

    if (letra in letrasEscolhidas):
        print('Você já tentou essa letra, tente novamente')

        sleep(5)
        system('cls') or None

    else:
        if (letra in palavra):
            for i in range(len(palavra)):
                if letra == palavra[i]:
                    estadoAtual[i] = letra

            letrasEscolhidas.append(letra)
            print('Você acertou!, a palavra ficou assim:')
            print(estadoAtual)
            print('')
            print('vc errou', erros, 'vezes. E já usou essas letras:')
            print(letrasEscolhidas)

            sleep(5)
            system('cls') or None

        else:
            print('Que pena, você errou:(')
            erros = erros + 1
            sleep(5)
            system('cls') or None

        str = ''

        for letraAtual in estadoAtual:
            str += letraAtual

        if (palavra == str):
            print('')
            print('-=' * 45)
            print('Você ganhou!!!')
            print('a palavra foi:', str)
            print('-=' * 45)
            break

        if (erros == 5):
            sleep(5)
            system('cls') or None
            print('Você já errou 5 vezes que pena, você perdeu:(')
            print('a palavra era:', palavra)
            break