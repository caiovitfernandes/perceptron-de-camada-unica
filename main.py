# Parâmetros
valorTrue = "True"
valorFalse = "False"

def degrau(u):
    if u >= 0:
        return 1
    else:
        return 0

for i in range(50):
    entradas = input(f"Digite: ")
    entradas = entradas.split(",")

    # Limiar e Pesos Sinápticos
    with open('./treinamento/pesos.txt', 'r') as arqPesos:
        pesos = arqPesos.readlines()
        
    u = -1 * float(pesos[0])
    for i, valor in enumerate(entradas):
        u = u + float(pesos[i + 1]) * float(valor)

    y = degrau(u)

    if y == 1:
        print(f"{valorTrue}")
    elif y == 0:
        print(f"{valorFalse}")
    else:
        print("erro")