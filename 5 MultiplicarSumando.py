n=int(input(""))
m=int(input(""))
def multiplicarSumando(n,m):
    if m==1:
        return n
    else:
        return n+multiplicarSumando(n,m-1)
print(multiplicarSumando(n,m))
