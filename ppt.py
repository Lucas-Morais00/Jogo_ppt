import random

querer = int(input("\nQuantas vezes vc quer jogar? Digite um numero de 1 a 10\n"))

contador = 0
placar_jog = 0
placar_com = 0

for i in range (querer):

    jogada = input("Qual vai ser a sua jogada? Digite: Pedra, Papel ou Tesoura\n")

    def ppt(jogada):

        lista = ["Pedra", "Papel", "Tesoura"]
        comp = random.choice(lista)

        if jogada == comp:
            return jogada + " X " + comp +" , deu empate!"

        elif jogada == "Pedra" and comp == "Papel":
            return "Pedra X Papel, vc perdeu!"

        elif jogada == "Pedra" and comp == "Tesoura":
            return "Pedra X Tesoura, vc ganhou!"

        elif jogada == "Papel" and comp == "Pedra":
            return "Papel X Pedra, vc ganhou!"

        elif jogada == "Papel" and comp == "Tesoura":
            return "Papel X Tesoura, vc perdeu!"
            
        elif jogada == "Tesoura" and comp == "Pedra":
            return "Tesoura X Pedra, vc perdeu!"
            
        elif jogada == "Tesoura" and comp == "Papel":
            return "Tesoura X Papel, vc ganhou!"

    lista = ["Pedra", "Papel", "Tesoura"]
    comp = random.choice(lista)

    if jogada == "Pedra" and comp == "Tesoura":
        placar_jog = placar_jog + 1

    elif jogada == "Papel" and comp == "Pedra":
        placar_jog = placar_jog + 1

    elif jogada == "Tesoura" and comp == "Papel":
        placar_jog = placar_jog + 1

    if jogada == "Pedra" and comp == "Papel":
        placar_com = placar_com + 1

    elif jogada == "Papel" and comp == "Tesoura":
        placar_com = placar_com + 1

    elif jogada == "Tesoura" and comp == "Pedra":
        placar_com = placar_com + 1

    print(placar_com)
    print(placar_jog)

    print(ppt(jogada))

    contador += 1
    if contador == (querer - 1):
        print("\nUltima jogada! Fique atento!!!\n")






    

