from math import e

def main():
    i = ((1/e) * (e-1))
    
    for n in range(1, 200):
        i = (1 - n * i)
    print(i)
    
main()
    