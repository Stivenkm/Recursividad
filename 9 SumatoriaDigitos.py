n=int(input(""))
def sumatoriaDigitos(n):
    if n/10==0:
        return 0
    else:
        return (n%10)+sumatoriaDigitos(n/10)
print(sumatoriaDigitos(n))
