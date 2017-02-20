numero=int(input("Ingrese el numero: "))
f=-1
def ValorAbs(n):
    if n==0:
        return 0
    elif n<0:
        return ValorAbs(n*-1)
    elif n>0:
        return n
print(ValorAbs(numero))
