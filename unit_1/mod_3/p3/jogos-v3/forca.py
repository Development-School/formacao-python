def jogar():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    while (not acertou and not enforcou):

        chute = input("Qual letra? {}".format(letras_acertadas))
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

            if (not "_" in letras_acertadas):
                acertou = True

        #print(letras_acertadas)
        if(acertou):
            print("Acertou!!! Palavra secreta: {}".format(letras_acertadas))
        print("Fim do jogo")

if(__name__ == '__main__'):
    jogar()