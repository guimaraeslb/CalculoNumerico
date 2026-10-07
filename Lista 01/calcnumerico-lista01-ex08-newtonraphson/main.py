def main():
    v = 0.0627
    y = (v**3) - (0.0427000000001183 * (v**2)) + (0.011457142857*v) - 0.00048922
    count = 1
    if(((y - 0) >= - 0.000000000001 and y - 0) <= 0.000000000001):
        return v

    while(((y - 0) < -0.000000000001 or (y - 0) > 0.000000000001) and count < 20):
        #print(y)
        derivada = (3*v**2 - 0.0854000000002366*v) + (0.011457142857)
        v = v - (y/derivada)
        y = (v**3) - (0.0427000000001183 * (v**2)) + (0.011457142857*v) - 0.00048922
        count = count + 1
    #print(y)
    print(count)
    print(y)
    return v

print(main())

#Valor de x com 4 iterações: 0.04270001731113605
#Valor de y que seria aproximado: 0.000000002298930899162846

#Valor de x com limite de 20 iterações: 0.04270000000047749 (parou na 5º iteração)
#Valor de y que seria aproximado: 0.000000000000000025587171270657905

#Erro permitido = 0.000000000001. Concluímos que, no primeiro caso, estaríamos fora do erro permitido. O programa só foi interrompido
#por conta do limite na qtd de execuções. No segundo caso, o programa parou de ser executado pois encontrou um valor válido para x.