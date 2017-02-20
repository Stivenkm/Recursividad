numero = int(input("Introduce el numero de la posicion : "))
def Fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)
 
print(Fibonacci(numero))
    
