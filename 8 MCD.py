n=int(input(""))
m=int(input(""))
def mcd(n,m):
    if n%m==0:
        return m
    else:
        return mcd(n,n%m)
print(mcd(n,m))
