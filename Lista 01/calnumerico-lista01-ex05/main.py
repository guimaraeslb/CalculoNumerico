def calc():
    pi = 0
    
    for n in range(0, 11):
        if(pi - 3.141592 >= -0.0001 and pi - 3.141592 <= 0.0001):
            print(n)
            return pi
        pi = pi + ((16 ** (n * -1)) * ((4 / (8*n + 1)) - 
            (2 / (8 * n + 4)) - (1 / (8 *n + 5)) - (1 / (8 * n + 6))))
    print(n)
    return pi
    
def main():
    print(calc())
    
main()