# Faça um programa em Python para resolver o seguinte problema:

# O programa deve receber um número inteiro (n1), digitado pelo usuário (input), e apresentar uma mensagem.
 
# - Se o número que o usuário digitou for divisível por 3 e por 5 ao mesmo tempo, a mensagem será: 
#       "O número escolhido é divisível por 3 e 5".

# - E se o número que o usuário digitou, não for divisível por 3 e por 5 ao mesmo tempo, a mensagem será: 
#       "O número escolhido não é divisível por 3 ou 5".

print('Olá! digite um número para saber se ele é divisível por 3 e também por 5:')
n1 = int(input())
if n1 % 3 == 0 and n1 % 5 == 0:
    print('O número escolhido é divisível por 3 e 5')
    print('O resultado do número', n1,'dividido por 3 é :', n1 // 3)
    print('O resultado do número', n1,'dividido por 5 é :', n1 // 5)
else:
    print('O número escolhido não é divisível por 3 ou 5')

# Este é um programa simples escrito em Python para praticar as funções de INPUT, PRINT, IF e ELSE, bem como as equações de divisão e resto.
