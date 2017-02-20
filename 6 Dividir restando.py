dividendo=int(input("Ingrese el dividendo: "))
divisor=int(input("Ingrese el divisor: "))
def DivRestando(n,m):
    if m>n:
        return 0
    return DivRestando(n-m,m)+1
print(DivRestando(dividendo,divisor))
