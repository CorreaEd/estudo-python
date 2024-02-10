import random
import string
import time

class Tank(object):
    def __init__(self, nome):
        self.nome = nome
        self.vivo = True
        self.tiros = 10
        self.vida = 60

    def __str__(self):
        if self.vivo:
            return "%s (%i vida, %i municao)" % (self.nome, self.vida, self.tiros)
        else:
            return "%s (Está MORTO)" % self.nome

    def atirou_em(self, inimigo):
        if self.tiros >= 1:
            self.tiros -= 1
            time.sleep(0.5)
            print("->", self.nome, "atirou em", inimigo.nome)
            inimigo.dano()
        else:
            time.sleep(0.5)
            print("\n***O tank de", self.nome, "ficou sem munição! ***")

    def dano(self):
        self.vida -= 20
        time.sleep(0.5)
        print("♥ Ai!... o tank de", self.nome, "foi atingido! ♥")
        print("-------------------------------------------------------")
        time.sleep(0.5)
        if self.vida <= 0:
            self.explosao()

    def explosao(self):
        self.vivo = False
        time.sleep(0.5)
        print("~ Já era! O tank do", self.nome, "explodiu!!")
        print("-------------------------------------------------------")


def batalha(dic, qtd, alphabet):
    if qtd == 1:
        time.sleep(0.5)
        print("\n###############################")
        print("☻  E o Tank campeão foi o:  ☻")
        time.sleep(0.5)
        print("-------------------------------")
        print("  ♦♦", dic[alphabet[0]].nome, "♦♦")
        print("###############################")
    else:
        dado = random.randint(0, qtd - 1)
        jogador = dic[alphabet[dado]]
        time.sleep(0.5)
        print("-------------------------------------------------------")
        print(jogador.nome, "é a sua vez de jogar! ☻")
        print("-------------------------------------------------------")

        time.sleep(0.5)
        print("☻ Agora escolha, em quem você irá atirar?")

        for i in range(qtd):
            if i != dado and dic[alphabet[i]].vivo:
                print(alphabet[i], " - ", dic[alphabet[i]].nome)

        vitim = input("R: ")
        print("----------------------------------------------------------------------")

        if dic[vitim].vivo:
            jogador.atirou_em(dic[vitim])

            for i in range(qtd):
                print(alphabet[i], " - ", dic[alphabet[i]])

            if dic[vitim].vivo:
                batalha(dic, qtd, alphabet)
            else:
                dic.pop(vitim)
                alphabet.remove(vitim)
                batalha(dic, qtd - 1, alphabet)
        else:
            dic.pop(vitim)
            alphabet.remove(vitim)
            batalha(dic, qtd - 1, alphabet)


qtde = int(input("Olá soldados! Digitem a quantidade de tanks/jogadores que irão participar: "))
alph = list(string.ascii_lowercase)
Tanks = []
filterAlph = []

print("---------------------------------------------------------------------------------------------------")
for i in range(qtde):
    nomes = input(f"Qual é o seu nome {i + 1}º soldado? ")
    Tanks.append((alph[i], Tank(nomes)))
    filterAlph.append(alph[i])

dictionary = dict(Tanks)

batalha(dictionary, qtde, filterAlph)
