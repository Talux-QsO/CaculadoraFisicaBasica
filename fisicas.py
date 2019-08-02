from math import sqrt
def distacia():
    tiempo=float(input("Cual es el timepo:"))
    velocidad=float(input("Cual es la velocidad:"))
    return print(tiempo*velocidad)

def tiempo():
    distacia=float(input("Cual es la distacia:"))
    velocidad=float(input("Cual es la velocidad:"))
    return print(distacia/velocidad)

def velocidad():
    distacia=float(input("Cual es la distacia:"))
    tiempo=float(input("Cual es el timepo:"))
    return print(distacia/tiempo)
def sinDitacia():
    vel0=float(input("Cual es la Velocidad inical:"))
    acelera=float(input("Cual es la Aceleracion:"))
    tiempo=float(input("Cual es la Tiempo:"))
    res=vel0+(acelera*tiempo)
    return print(res)

def sinAceleracion():
    vel0=float(input("Cual es la Velocidad inical:"))
    velF=float(input("Cual es la Velocidad Final:"))
    tiempo=float(input("Cual es la Tiempo:"))
    res = ((vel0+velF)/2)*tiempo
    return print(res)

def sinVelocidadFinal():
    vel0=float(input("Cual es la Velocidad inicial:"))
    acelera=float(input("Cual es la Aceleracion:"))
    tiempo=float(input("Cual es la Tiempo:"))
    res =(vel0*tiempo)+(acelera*tiempo**2/2)
    return print(res)

def sinTiempo():
    vel0=float(input("Cual es la Velocidad inicial:"))
    acelera=float(input("Cual es la Aceleracion:"))
    distancia=float(input("Cual es la Distancia:"))
    res =sqrt((vel0**2)+2*(acelera*distancia))
    return print(res)

def aceleracion():
    vel0=float(input("Cual es la Velocidad inicial:"))
    velF=float(input("Cual es la Velocidad final:"))
    tiempo0=float(input("Cual es la Tiempo inicial:"))
    tiempoF=float(input("Cual es la Tiempo final:"))
    res = (velF-vel0)/(tiempoF-tiempo0)
    return print(res)
