base=int(input("Ingrese la base :"))
exp=int(input("Ingrese el exponente :"))

def Potencia(b,e):
    if e==0:
        return 1
    else: 
        return b*Potencia(b,e-1)
print(Potencia(base,exp))
        
        
    
