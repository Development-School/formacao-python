def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    # letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    letras_acertadas = ["_" for index in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    # print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        # print(erros)

        """if (erros == 6):
            break
        if ("_" not in letras_acertadas):
            break"""

        enforcou = (erros == 6)
        acertou = ("_" not in letras_acertadas)

        print(letras_acertadas, end = "\n\n")

        if(acertou):
            print("Você ganhou!!")
        elif(enforcou):
            print("Você perdeu, suas {} tentativas acabaram!!".format(erros))

    print("Fim do jogo", end = '\n\n')

if(__name__ == "__main__"):
    jogar()