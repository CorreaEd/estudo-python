# Faça um programa modularizado em Python, para resolver um problema usando listas.
# O programa deve ter as seguintes funções:

# - entradas(): Solicita ao usuário a quantidade de carros a serem comparados.
# - economico(carros): Para imprimir a lista dos carros e suas respectivas quilometragens (por litro).

# O programa irá apresentar na tela, o carro que fizer a maior quantidade de Km's com apenas 1 litro.

print("Olá, escolha a quantidade de carros que deseja comparar. Em seguida, insira quantos Km's eles fazem por litro!")

def entradas():
    carros = []  # Lista para armazenar informações sobre os carros
    q_carros = int(input("Quantos carros você deseja comparar? "))
        
    for i in range(q_carros): # Loop para coletar informações sobre cada carro
        modelo = input(f"Digite o modelo do {i + 1}º carro: ")
        kms_litro = float(input(f"Agora digite quantos Km's por litro o {modelo} faz: "))                    
        carros.append({ # Adiciona as informações do carro à lista
                'modelo': modelo,
                'km_litro': kms_litro
            })

    return carros    

def economico(carros):
    
    print("\nLista de Carros:")
    for carro in carros:
        print(f"{carro['modelo']}: {carro['km_litro']} Km/l")

    # Encontra o carro com maior quilometragem por litro
    economico = max(carros, key=lambda x: x['km_litro'])

    # Imprime o carro mais econômico
    print(f"\nO carro mais econômico é {economico['modelo']} "
          f"com {economico['km_litro']} Km's por litro!.")

def main():
    carros = entradas()  # Chama o método para obter as entradas
    economico(carros)  # Chama o método para encontrar e imprimir o carro mais econômico

main()