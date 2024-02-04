###### Exercício - Tabuada ######

import time #Importação do módulo time para trabalharmos com a função de delay

def tabuada():
	print("Digite um número de 1 a 1000, para descobrir sua tabuada!")
	valor = int(input())

	while valor < 1 or valor > 1000: ### Alterar o "1000" pelo número que deseja limitar.
		print("VALOR INVÁLIDO")
		valor = int(input())

	for i in range (1, 11): ### Alterar o "11" para a quantidade de vezes que deve ocorrer a multiplicação.
		print(f'{valor}x{i}={valor*i}')
		time.sleep(0.8) ### Alterar o "0.8" para modificar a velocidade em que os valores são exibidos.
	continuar()

def continuar():
	print()
	print("Deseja ver a tabuada de outro número?")
	print("1 - Sim")
	print("2 - Não")
	comando = int(input())
	print()
	
	if comando == 1:
		tabuada()

	if comando == 2:
		print("FIM - obrigado!")

	if comando < 1 or comando > 2:
		print("OPÇÃO INVÁLIDA")
		print()
		continuar()

def main():
	tabuada()

main()