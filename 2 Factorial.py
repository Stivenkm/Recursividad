numero = int(input("Introduce un numero: "))
def Factorial(n):
    if n < 0:
        print("No existe el factorial de un numero negativo")
    elif n < 2:
            return 1
    else:
         return n * Factorial(n-1)
    
print (Factorial(numero))

