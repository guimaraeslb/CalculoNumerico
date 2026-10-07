def main():
    a = 0.0427
    b = 0.06
    medio = (a+b) / 2
    
    ya = (a**3) - (0.0427000000001183 * (a**2)) + (0.011457142857*a) - 0.00048922
    yb = (b**3) - (0.0427000000001183 * (b**2)) + (0.011457142857*b) - 0.00048922
    ymedio = (medio**3) - (0.0427000000001183 * (medio**2)) + (0.011457142857*medio) - 0.00048922
    
    #Contador de iterações
    k = 1
    
    if(((ymedio - 0) >= - 0.000000000001 and ymedio - 0) <= 0.000000000001):
        return medio

    while(((ymedio - 0) < -0.000000000001 or (ymedio - 0) > 0.000000000001) and k < 30):
        if((ya*ymedio) < 0):
            b = medio
            medio = (a+b) / 2
            ymedio = (medio**3) - (0.0427000000001183 * (medio**2)) + (0.011457142857*medio) - 0.00048922
            k+=1
        elif((yb*ymedio) < 0):
            a = medio
            medio = (a+b) / 2
            ymedio = (medio**3) - (0.0427000000001183 * (medio**2)) + (0.011457142857*medio) - 0.00048922
            k+=1
    print(k)
    print(ymedio)
    return medio

print(main())

#valor de x com 4 iterações: 0.04378125
#valor de y que seria aproximado: 0.000014460573384806534

#valor de x com limite de 30 iterações: 0.042700000064447526 (parou na 28º iteração)
#valor de y que seria aproximado: 0.0000000000008495754013487788

#Erro permitido = 0.000000000001. Concluímos que, no primeiro caso, estaríamos fora do erro permitido. O programa só foi interrompido
#por conta do limite na qtd de execuções. No segundo caso, o programa parou de ser executado pois encontrou um valor válido para x.