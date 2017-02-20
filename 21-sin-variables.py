import random

def jugar(mazo, jugador, casa):
    if(len(jugador) < 2 and len(casa) < 2):
       jugar(mazo[2:], repartir([mazo[0]], jugador), repartir([mazo[1]], casa))
    ordenar(jugador)
    ordenar(casa)
    
    print ("Jugador:")
    print (jugador)
    print ("Casa:")
    print(casa)
    
    if(validarSuma(jugador, 0) > 21):
       print ("Has perdido", validarSuma(jugador,0))
       exit()
       
    if(validarSuma(jugador, 0) < 21):
        print ("Lleva en total ", validarSuma(jugador, 0))
        print ("Puntaje de la casa : ", validarSuma(casa, 0))
        if(input("Desea continuar s/n: ") != "n"):
            jugar(mazo[1:], jugador + [mazo[0]], casa)
        else:
            print ("Has plantado en:  " + str(validarSuma(jugador,0)))
            return jugarMaquina(mazo[1:],casa,validarSuma(jugador,0))
            exit()
            
    if(validarSuma(casa,0) < 21 ):
        jugarMaquina(mazo[1:],casa,validarSuma(casa,0))
        print("Puntaje de la casa" ,validarSuma(casa,0))
        
        
    if(validarSuma(jugador, 0) == 21):
        print ("¡Tenemos 21! Esperemos a la casa" ,validarSuma(jugador,0))
        jugarMaquina(mazo[1:],casa,validarSuma(jugador,0))
        print ("Puntaje de la casa : ", validarSuma(casa,0))
        exit()

def jugarMaquina(mazo, casa,numJugador):
    if(validarSuma(casa,0) > 21):
        print(casa)
        print ("Felicidades , has ganado")
        print ("Puntaje de la casa : "+str(validarSuma(casa,0)))
        print ("Tu puntaje es: "+str(numJugador))
        exit()
    if(validarSuma(casa,0) >= numJugador and validarSuma(casa,0) <= 21):
        print ("¡Vaya, que triste! Ganó la casa ")
        print ("Puntaje de la casa : " + str(validarSuma(casa, 0)))
        print ("Tu puntaje es: " + str(numJugador))
        exit()
    if(validarSuma(casa,0) < numJugador):
        print(casa)
        print ("Puntaje de la casa : "+str(validarSuma(casa,0)))
        return jugarMaquina(mazo[1:],repartir(mazo, casa),numJugador)
    
def validarSuma(jugador, resultado):
    if(jugador == []):
        return resultado
    else:
        if(jugador[0] == "A" and resultado <= 10):
            return (validarSuma(jugador[1:], resultado+11))
        elif(jugador[0] == "A" and resultado > 10):
            return (validarSuma(jugador[1:], resultado+1))
        elif(jugador[0] == "J" or jugador[0] == "Q" or jugador[0] == "K"):
            return (validarSuma(jugador[1:], resultado+10))
        else:
            return (validarSuma(jugador[1:], resultado+jugador[0]))
   
def repartir(mazo, jugador):
    return jugador + [mazo[0]]


def desordenar(mazo):
    random.shuffle(mazo)
    return mazo

def ordenar(jugador):
    for i in range (len(jugador)):
        if(jugador[i] == "A"):
            jugador.remove("A")
            jugador.append("A")
    return jugador

jugar(desordenar([(x)for x in [1,2,3,4,5,6,7,8,9,"A","J","Q","K"]*4] ), [],[])
