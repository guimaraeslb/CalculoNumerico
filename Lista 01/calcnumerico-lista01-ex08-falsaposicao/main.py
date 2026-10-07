def main():
    a = 0.0427
    b = 0.06
    
    ya = (a**3) - (0.0427000000001183 * (a**2)) + (0.011457142857*a) - 0.00048922
    yb = (b**3) - (0.0427000000001183 * (b**2)) + (0.011457142857*b) - 0.00048922
    
    medio = ((-b*ya + a*ya)/(yb-ya)) + a
    ymedio = (medio**3) - (0.0427000000001183 * (medio**2)) + (0.011457142857*medio) - 0.00048922
    
    #Contador de iterações
    k = 1
    
    if(((ymedio - 0) >= - 0.000000000001 and ymedio - 0) <= 0.000000000001):
        print(ymedio)
        return medio

    while(((ymedio - 0) < -0.000000000001 or (ymedio - 0) > 0.000000000001) and k < 4):
        if((ya*ymedio) < 0):
            b = medio
            medio = ((-b*ya + a*ya)/(yb-ya)) + a
            ymedio = (medio**3) - (0.0427000000001183 * (medio**2)) + (0.011457142857*medio) - 0.00048922
            k+=1
        elif((yb*ymedio) < 0):
            a = medio
            medio = ((-b*ya + a*ya)/(yb-ya)) + a
            ymedio = (medio**3) - (0.0427000000001183 * (medio**2)) + (0.011457142857*medio) - 0.00048922
            k+=1
    print(k)
    print(ymedio)
    return medio

print(main())

#Nesse caso, como partimos de um intervalo incial com a muito próximo da raiz, o método chegou ao resultado final
#na 1º iteração.