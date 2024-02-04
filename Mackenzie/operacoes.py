# Escreva um programa em Python que permite ao usuário digitar dois números inteiros 
# e exibir o resultado para cada uma das seguintes operações, nesta ordem: 
# soma, subtração, multiplicação, divisão, divisão truncada, resto e exponenciação.

import time #Importação do módulo time para trabalharmos com a função de delay

def numeros():
    print ("Olá, digite dois números a sua escolha!\n")
    numero1 = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))

    soma = (numero1 + numero2)
    subtracao = (numero1 - numero2)
    multiplicacao = (numero1 * numero2)
    divisao = (numero1 / numero2)
    truncada = (numero1 // numero2)
    resto = (numero1 % numero2)
    exponenciacao = (numero1 ** numero2)

    time.sleep(0.4)
    print ("A soma dos números escolhidos é: ", soma)
    time.sleep(0.4)
    print ("A subtração dos números escolhidos é: ", subtracao)
    time.sleep(0.4)
    print ("A multiplicação dos números escolhidos é: ", multiplicacao)
    time.sleep(0.4)
    print ("A divisão dos números escolhidos é: ", divisao)
    time.sleep(0.4)
    print ("A divisão truncada dos números escolhidos é: ", truncada)
    time.sleep(0.4)
    print ("O resto da divisão dos números escolhidos é: ", resto)
    time.sleep(0.4)
    print ("A exponenciação dos números escolhidos é: ", exponenciacao)
    continuar()

def continuar():
	print ("\nDeseja escolher outros números?")
	print ("1 - Sim")
	print ("2 - Não\n")
	comando = int(input())
	
	if (comando == 1):
		numeros()

	elif (comando == 2):
		print ("FIM - obrigado!")

	else:
		print ("OPÇÃO INVÁLIDA\n")
		continuar()

def main():
    numeros()

main()