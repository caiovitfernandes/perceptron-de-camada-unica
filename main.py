# Parâmetros
valorTrue = "True"
valorFalse = "False"
splitDaEntrada = " "
mapeamento = True
indexMapeados = []
mapeadosA = []
mapeadosB = []


def normalizar(valor):
    tratado = float(valor)
    while tratado > 1:
        tratado = tratado / 10
    return tratado

def mapear(valor):
    i = mapeadosB.index(valor)
    return float(mapeadosA[i])

def degrau(u):
    if u >= 0:
        return 1
    else:
        return 0

for i in range(50):
    entradas = input(f"Digite: ")
    entradas = entradas.split(splitDaEntrada)

    # Limiar e Pesos Sinápticos
    with open('./treinamento/pesos.txt', 'r') as arqPesos:
        pesos = arqPesos.readlines()
        
    u = -1 * float(pesos[0])
    for i, valor in enumerate(entradas):
        if mapeamento and i in indexMapeados:
            u = u + float(pesos[i + 1]) * normalizar(mapear(valor))
        else:
            u = u + float(pesos[i + 1]) * normalizar(valor)

    y = degrau(u)

    if y == 1:
        print(f"{valorTrue}")
    elif y == 0:
        print(f"{valorFalse}")
    else:
        print("erro")