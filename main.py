print("Hola Gracias por usar mi script!")
print("ScriptByRobertx")
print("Este generador de tarjetas de credito, son aleatorias")
print("No sabemos si son validas o no.")
print("OJO EL 4 NO CUENTA.")

import random 

def generador(): 
    
    prefixList = []
    for i in range(4): 
       prefixList.append(str(random.randint(1111, 9999)))
    print("La tarjeta de credito generada es:")
    print("4",prefixList[0],prefixList[1],prefixList[2],prefixList[3], 
                          str(random.randint(1, 9999)).zfill(4),"")
 
generador()