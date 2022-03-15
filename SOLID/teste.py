linhas = int(input("Quantas linhas: "))
colunas = int(input("Quantas colunas: "))
matriz = list()
for x in range(linhas):
    linha = list()
    for y in range(colunas):
        linha.append(int(input(f'linha {x} coluna {y} = ')))
    matriz.append(linha)
print(matriz)

