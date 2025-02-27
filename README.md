# O que é a perceptron de camada única?
É uma rede neural com apenas um neurônio artificial treinado utilizando a regra de Hebb.
# Para que serve?
Ela é capaz de aprender a separar classes linearmente separáveis. Um exemplo comum de uso é para realizar as operações lógicas "e" e "ou".
# Como utilizar a rede presente nesse repositório?
A rede presente neste repositório está com os pesos sinápticos e limiar de ativação (presentes no arquivo pesos.txt da pasta treinamento) treinados para realizar a operação "e" lógico. Isso pode ser observado pelos arquivos "entradas.txt" e "saidas.txt" presentes na pasta de treinamento.
Algo como:
Entrada: 1,1
Saída: 1
Pode ser observado nesses arquivos de treinamento. Indicando a operação "e" lógica, que no caso da entrada 1,1 efetua a operação tendo a saída 1.
Para testar a rede nestas condições, basta executar o arquivo main presente na pasta raiz e digitar entradas de dois dígitos separados por vírgula, como por exemplo:
Digite: 1,1 
True
Digite: 1,0
False
# Como treinar a rede para executar outra tarefa?
Para treinar a rede para a execução de outra tarefa, basta alterar os dados presentes nos arquivos de entradas e saidas para que eles contenham um conjunto de entradas e saídas para o problema a ser resolvido. Vale lembrar que a rede perceptron só consegue resolver problemas de classificação que envolvam apenas duas classes linearmente separáveis. Como no exemplo do "e" lógico, onde a saída é "True" ou "False".
Após trocar as entradas e saídas basta abrir o arquivo "treinamento.py" na pasta de treinamento, alterar a quantidade de itens presentes na entrada (para o caso do "e" lógico são dois itens na entrada, então no código está "numeroDeItens = 2") e executar o algoritmo de treinamento.
Após executado o algoritmo de treinamento, basta reexecutar o main.py.
Vale ressaltar: caso o problema não seja mapeável em duas classes linearmente separáveis, pode ser que o treinamento execute um número limite de épocas sem conseguir encontrar os pesos sinápticos corretos. 
