from math import inf

def calcular_norma_diferenca(v1, v2):
  x1 = v1[0] - v2[0]
  x2 = v1[1] - v2[1]
  x3 = v1[2] - v2[2]
  x4 = v1[3] - v2[3]
  x5 = v1[4] - v2[4]
  x6 = v1[5] - v2[5]
  x7 = v1[6] - v2[6]
  x8 = v1[7] - v2[7]
  x9 = v1[8] - v2[8]
  x10 = v1[9] - v2[9]

  norma_diferenca  = ((x1 ** 2) + (x2 ** 2) + (x3 ** 2) + (x4 ** 2) + (x5 ** 2) + (x6 ** 2) + (x7 ** 2) + (x8 ** 2) + (x9 ** 2) + (x10 ** 2) )**0.5
  return norma_diferenca

def criterio_norma_euclidiana(matriz):
    linhas = len(matriz)
    colunas = linhas
    soma_quadrados = 0
    norma_euclidiana = 0

    for i in range(0, linhas):
        for j in range(0, colunas):
            soma_quadrados = soma_quadrados + (matriz[i][j] *  matriz[i][j])
    norma_euclidiana = (soma_quadrados ** 0.5)
    return norma_euclidiana

def criterio_norma_colunas(matriz):
    linhas = len(matriz)
    colunas = linhas
    norma_coluna = -inf
    soma_coluna = 0

    for j in range(0, colunas):
        for i in range(0, linhas):
            soma_coluna = soma_coluna + abs(matriz[i][j])
        norma_coluna = max(norma_coluna, soma_coluna)
        soma_coluna = 0
    return norma_coluna

def criterio_norma_linhas(matriz):
    linhas = len(matriz)
    colunas = linhas
    norma_linha = -inf
    soma_linha = 0

    for i in range(0, linhas):
        for j in range(0, colunas):
            soma_linha = soma_linha + abs(matriz[i][j])
        norma_linha = max(norma_linha, soma_linha)
        soma_linha = 0
    return norma_linha

def main():
    matriz_coeficientes = [
        [0, 1 / 3, 1 / 6, 1 / 6, 0, 0, 0, 0, 0, 0],
        [3 / 4, 0, 1 / 4, 0, 0, 0, 0, 0, 0, 0],
        [3 / 23, 2 / 23, 0, 6 / 23, 6 / 23, 3 / 23, 3 / 23, 0, 0, 0],
        [1 / 3, 0, 2 / 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3 / 4, 0, 0, 1 / 4, 0, 0, 0, 0],
        [0, 0, 1 / 3, 0, 0, 0, 2 / 3, 0, 0, 0],
        [0, 0, 3 / 23, 0, 2 / 23, 6 / 23, 0, 6 / 23, 3 / 23, 3 / 23],
        [0, 0, 0, 0, 0, 0, 3 / 4, 0, 1 / 4, 0],
        [0, 0, 0, 0, 0, 0, 1 / 3, 0, 0, 2 / 3],
        [0, 0, 0, 0, 0, 0, 3 / 13, 2 / 13, 6 / 13, 0],
    ]
    
    if(criterio_norma_euclidiana(matriz_coeficientes) < 1 or criterio_norma_linhas(matriz_coeficientes) < 1 or criterio_norma_colunas(matriz_coeficientes) < 1 or True):
        print("Converge!")
        v = []
        v.append([5, 6, 6, 5, 3, 2, 6, 7, 1, 7])

        for i in range(1, 10000):
            size = len(v)
            v1 = (1 / 3) * v[size - 1][1] + (1 / 6) * v[size - 1][2] + (1 / 6) * v[size - 1][3]
            v2 = (3 / 4) * v[size - 1][0] + (1 / 4) * v[size - 1][2]
            v3 = (3 / 23) * v[size - 1][0] + (2 / 23) * v[size - 1][1] + (6 / 23) * v[size - 1][3] + (6 / 23) * v[size - 1][4] + (3 / 23) * v[size - 1][5] + (3 / 23) * v[size - 1][6]
            v4 = (1 / 3) * v[size - 1][0] + (2 / 3) * v[size - 1][2]
            v5 = (3 / 4) * v[size - 1][2] + (1 / 4) * v[size - 1][6]
            v6 = (1 / 3) * v[size - 1][2] + (2 / 3) * v[size - 1][6]
            v7 = (3 / 23) * v[size - 1][2] + (2 / 23) * v[size - 1][4] + (6 / 23) * v[size - 1][5] + (6 / 23) * v[size - 1][7] + (3 / 23) * v[size - 1][8] + (3 / 23) * v[size - 1][9]
            v8 = (3 / 4) * v[size - 1][6] + (1 / 4) * v[size - 1][9]
            v9 = (1 / 3) * v[size - 1][6] + (2 / 3) * v[size - 1][9]
            v10 = (3 / 13) * v[size - 1][6] + (2 / 13) * v[size - 1][7] + (6 / 13) * v[size - 1][8] + (254 / 13)
            v.append([v1, v2, v3, v4, v5, v6, v7, v8, v9, v10])

            if(calcular_norma_diferenca(v[len(v) - 1], v[len(v) - 2]) > -0.01 and calcular_norma_diferenca(v[len(v) - 1], v[len(v) - 2]) < 0.01):
                print(i)
                break;

        print(v[len(v)-1])
    else:
        print("Não converge!")

main()