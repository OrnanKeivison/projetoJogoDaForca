from time import sleep
from random import choice
from os import system

palavras = []

def inicio():
    print('FORCA DE PALAVRAS')
    print('Seu objetivo é tentar acertar a palavra secreta')
    print('Você terá que tentar uma letra por vez')
    print('Caso você acerte, a letra será colocada na palavra para que você chegue mais perto de acertar')
    print('você pode errar 5 vezes')
    print('o tema das palavras é programação')
    sleep(3)

def main():
    inicio()

    while True:
        tema  = input(''' agora escolha o tema que você deseja jogar:
                        [1] programação
                        [2] frutas
                        [3] series
                        ''')

        if (tema == '1'):
            palavras = ['ALGORITMOS', 'PYTHON', 'HTML']

            dica1 = 'é a primeira matéria do curso relacionada a programção'
            dica2 = 'é uma liguagem orientada a objetos'
            dica3 = 'é uma linguagem de marcação'
            break
        
        elif (tema == '2'):
            palavras = ['MARACUJA', 'PITAYA', 'KIWI']

            dica1 = 'é uma delícia em doces'
            dica2 = 'é uma fruta sem sabor'
            dica3 = 'é verde e com pontinhos'
            break

        elif (tema == '3'):
            palavras = ['FRIENDS', 'BRIDGERTON', 'MANIFEST']

            dica1 = 'bebem muito café'
            dica2 = 'serie de época'
            dica3 = 'voo 828'
            break

        else:
            print('número inválido')

    palavra = choice(palavras)

    for i in palavras:
        if (palavra == palavras[1]):
            if(i == 0):
                dica = dica1
        elif(i == 1):
                dica = dica2
        elif(i == 2):
                dica = dica3   

    estadoAtual = ['_'] * len(palavra)
    letrasEscolhidas = []

    erros = 0


    while True:
        letra = input('Digite uma letra: ')
        letra = letra.upper()

        if (letra in letrasEscolhidas):
            print('Você já tentou essa letra, tente novamente')

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

            else:
                print('Que pena, você errou:(')
                if (erros <= 2):
                    print('Diquinha: a palavra tem',len(palavra),'letras')
                elif(erros > 2):
                    print('toma uma dica:',dica)
                print(estadoAtual)
                erros = erros + 1

            # verfica se o usuario acertou
            str = ''

            for letraAtual in estadoAtual:
                str += letraAtual

            if (palavra == str):
                print('')
                print('Você ganhou!!!')
                print('a palavra foi:', str)
                break

            if (erros == 5):
                print('Você já errou 5 vezes que pena, você perdeu:(')
                print('a palavra era:', palavra)
                break

main()

