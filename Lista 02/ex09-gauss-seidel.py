from math import inf

def calcular_norma_diferenca(v1, v2):
  x1 = v1[0] - v2[0]
  x2 = v1[1] - v2[1]
  x3 = v1[2] - v2[2]

  norma_diferenca  = ((x1 ** 2) + (x2 ** 2) + (x3 ** 2))**0.5
  return norma_diferenca

def criterio_sassenfeld(matriz):
    b1 = (matriz[0][1] + matriz[0][2])/matriz[0][0]
    b2 = (matriz[1][0] * b1 + matriz[1][2])/matriz[1][1]
    b3 = (matriz[2][0] * b1 + matriz[2][1] * b2)/matriz[2][2]

    b = max(b1,b2,b3)
    print(b)
    return b


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
    soma_quadrados = 0

    for j in range(0, colunas):
        for i in range(0, linhas):
            soma_quadrados = soma_quadrados + (matriz[i][j] *  matriz[i][j])
        norma_coluna = max(norma_coluna, (soma_quadrados**0.5))
        soma_quadrados = 0
    return norma_coluna

def criterio_norma_linhas(matriz):
    linhas = len(matriz)
    colunas = linhas
    norma_linha = -inf
    soma_quadrados = 0

    for i in range(0, linhas):
        for j in range(0, colunas):
            soma_quadrados = soma_quadrados + (matriz[i][j] *  matriz[i][j])
        norma_linha = max(norma_linha, (soma_quadrados**0.5))
        soma_quadrados = 0
    return norma_linha

def main():
    matriz = [
        [-6, 2, 1, 1, 0, 0, 0, 0, 0, 0],
        [3, -4, 1, 0, 0, 0, 0, 0, 0, 0],
        [3, 2, -23, 6, 6, 3, 3, 0, 0, 0],
        [1, 0, 2, -3, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, -4, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, -3, 2, 0, 0, 0],
        [0, 0, 3, 0, 2, 6, -23, 6, 3, 3],
        [0, 0, 0, 0, 0, 0, 3, -4, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, -3, 2],
        [0, 0, 0, 0, 0, 0, 3, 2, 6, -13]
    ]
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
        [0, 0, 0, 0, 0, 0, 3 / 13, 2 / 13, 6 / 13, 0]
    ]

    if(criterio_norma_euclidiana(matriz_coeficientes) < 1 or criterio_norma_linhas(matriz_coeficientes) < 1 or criterio_norma_colunas(matriz_coeficientes) < 1 or criterio_sassenfeld(matriz)):
        print("Converge!")
        v = []
        v.append([5, 6, 6, 5, 3, 2, 6, 7, 1, 7])
        v1, v2, v3, v4, v5, v6, v7, v8, v9, v10 = 5,6,6,5,3,2,6,7,1,7

        for i in range(1, 10000):
            size = len(v)
            v1 = (1 / 3) * v2 + (1 / 6) * v3 + (1 / 6) * v4
            v2 = (3 / 4) * v1 + (1 / 4) * v3
            v3 = (3 / 23) * v1 + (2 / 23) * v2 + (6 / 23) * v4 + (6 / 23) * v5 + (3 / 23) * v6 + (3 / 23) * v7
            v4 = (1 / 3) * v1 + (2 / 3) * v3
            v5 = (3 / 4) * v3 + (1 / 4) * v6
            v6 = (1 / 3) * v3 + (2 / 3) * v7
            v7 = (3 / 23) * v3 + (2 / 23) * v5 + (6 / 23) * v6 + (6 / 23) * v8 + (3 / 23) * v9 + (3 / 23) * v10
            v8 = (3 / 4) * v7 + (1 / 4) * v9
            v9 = (1 / 3) * v7 + (2 / 3) * v10
            v10 = (3 / 13) * v7 + (2 / 13) * v8 + (6 / 13) * v9 + (254 / 13)
            v.append([v1, v2, v3, v4, v5, v6, v7, v8, v9, v10])

            if(calcular_norma_diferenca(v[len(v) - 1], v[len(v) - 2]) > -0.01 and calcular_norma_diferenca(v[len(v) - 1], v[len(v) - 2]) < 0.01):
                print(i)
                break;

        print(v[len(v)-1])
    else:
        print("Não converge!")

main()