'''
Deseja-se fazer uma pesquisa a respeito do consumo mensal de energia elétrica em determinada cidade. 
Para isso, são fornecidos os seguintes dados: 
   - o preço de KW/hora consumido; 
   - a quantidade de KW/hora consumida durante o mês/ e
   - o tipo de consumidor (Industrial, Comercial, Residencial). 

Dependendo do tipo de consumidor, a conta mensal sofre um acréscimo: 
   industrial – 15%; 
   comercial – 5%;
   residencial – não tem acréscimo. 
    
Faça um programa em Python que receba os dados de entrada, calcule e mostre o valor final da 
conta mensal do consumidor.
'''

import math
import time

def tipo_conta():
   print ("Informe o tipo da sua conta:\n")
   print ("1 - Industrial \n2 - Comercial \n3 - Residencial")
   tipo = (int(input("Digite a opção: ")))

   if (tipo == 1):
      valor_conta = (float(input("Digite o valor da conta: ")))
      valor_conta = float(valor_conta + valor_conta*0.15)
      print ("Valor total é:", round(valor_conta,2))

   elif (tipo == 2):
      valor_conta = (float(input("Digite o valor da conta: ")))
      valor_conta = float(valor_conta + valor_conta*0.05)
      print ("Valor total é:", round(valor_conta,2))

   elif (tipo == 3):
      valor_conta = (float(input("Digite o valor da conta: ")))
      print ("Valor total é:", valor_conta, "(Não tem acréscimo!)")

   else:
      print ("Opção inválida")
   
   continuar()

def continuar():
   time.sleep(0.8)
   print ("\nDeseja calcular outra conta?")
   print ("1 - Sim")
   print ("2 - Não\n")
   comando = int(input())
	
   if (comando == 1):
      tipo_conta()
      
   elif (comando == 2):
      print ("FIM - obrigado!")
      
   else:
      print ("OPÇÃO INVÁLIDA\n")
      continuar()

def main():
   tipo_conta()

main()