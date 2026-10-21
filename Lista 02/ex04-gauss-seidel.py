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
    matriz = [[5,2,1],[2,5,2],[1,2,4]]
    matriz_coeficientes = [[0, -2/5, -1/5],[1/4,0, -2/4],[-2/10, 3/10,0]]

    if(criterio_norma_euclidiana(matriz_coeficientes) < 1 or criterio_norma_linhas(matriz_coeficientes) < 1 or criterio_norma_colunas(matriz_coeficientes) < 1 or criterio_sassenfeld(matriz)):
        print("Converge!")
        x = []
        x1,x2,x3 = -2.3, 5, 0.3
        x.append([-2.4,5,0.3])

        for i in range(1, 1000):
            size = len(x)
            x1 = ((-2*x[size-1][1]) - (x[size-1][2]) + 7)/5
            x2 = ((x1) - (2 *x3) + 3)/4
            x3 = ((-2*x1)+ (3*x2) - 1)/10
            x.append([x1,x2,x3])

            if(calcular_norma_diferenca(x[len(x) - 1], x[len(x) - 2]) > -0.01 and calcular_norma_diferenca(x[len(x) - 1], x[len(x) - 2]) < 0.01):
                print(i)
                break;

        print(x[len(x)-1][0], x[len(x)-1][1], x[len(x)-1][2])
    else:
        print("Não converge!")

main()