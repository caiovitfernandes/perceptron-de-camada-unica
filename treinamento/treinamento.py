import random

# Parâmetros
numeroDeItens = 2
n = 0.01
maxEpocas = 100000
#[viés, valor1, valor2...]
pesosAtualizar = []
def normalizar(valor):
    tratado = float(valor)
    while tratado > 1:
        tratado = tratado / 10
    return tratado


# Preenche os pesos iniciais aleatoriamente
for i in range(numeroDeItens + 1):
    pesosAtualizar.append(random.uniform(0.05, 0.5))

def degrau(u):
    if u >= 0:
        return 1
    else:
        return 0

def atualizaOsPesos(pesosFinais):
    with open('./pesos.txt', 'w') as arqPesos:
        for item in pesosFinais:
            arqPesos.write(f"{item}\n")



# Entradas do treinamento
with open('./entradas.txt', 'r') as arqEntradas:
    entradas = arqEntradas.readlines()

# Saídas esperadas
with open('./saidas.txt', 'r') as arqSaidas:
    saidas = [float(s.strip()) for s in arqSaidas.readlines()]


epocas = 0

erro = 1

while (erro == 1 and epocas <= maxEpocas):
    
    print(f"Iniciando a época: {epocas}")
    erro = 0

    for i, entrada in enumerate(entradas):
        valores = entrada.split(',')
        u = float(-1) * float(pesosAtualizar[0])
        for j, valor in enumerate(valores):
            u = u + normalizar(valor) * float(pesosAtualizar[j + 1])
        y = degrau(u)
        if float(y) != saidas[i]:
            pesosAtualizar[0] += n * (saidas[i] - float(y)) * (-1)
            for k, valor in enumerate(valores):
                pesosAtualizar[k + 1] += n * (saidas[i] - float(y)) * normalizar(valor)
            erro = 1
    epocas = epocas + 1

atualizaOsPesos(pesosAtualizar)

if(erro == 0):
    print('Pesos sinápticos ajustados!')
else:
    print(f'Não foi possível treinar a rede com apenas {epocas} épocas.')

