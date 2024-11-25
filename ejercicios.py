# Ejercicio 1
#
#  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#    requiere: {e pertenece a s }
#    asegura: {res es la posición de la última aparición de e en s}
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,100,0,100,0,-1,-1]
#   e = 0
# se debería devolver res=7

def ultima_aparicion(s: list, e: int) -> int:
    for i in range(len(s) - 1, -1, -1):  # Desde len(s)-1 hasta 0
        if s[i] == e:
            return i


print(ultima_aparicion([1,2,3,4,1],1))

# Ejercicio 2
#
#  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
#    requiere: -
#    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
#    asegura: {res no tiene elementos repetidos }
#  }

# Por ejemplo, dados
s = [-1,4,0,4,3,0,100,0,-1,-1]
t = [0,100,5,0,100,-1,5]
# se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3] 
# ó res = [5,3,4] ó res = [5,4,3]

def pertenece(s:list, e:any) -> bool:
    for i in s:
        if i == e:
            return True
    return False

def elementos_exclusivos(s:list,t:list) -> list:
    elementosEnAlgunaLista:list = []
    for i in s:
        if not pertenece(t,i) and not pertenece(elementosEnAlgunaLista,i):
            elementosEnAlgunaLista.append(i)
    
    for j in t:
        if not pertenece(s,j) and not pertenece(elementosEnAlgunaLista,j):
            elementosEnAlgunaLista.append(j)
    
    return elementosEnAlgunaLista

print(elementos_exclusivos(s,t))

# Ejercicio 3
#
# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
# en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
# en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
# palabras que tienen la misma traducción en inglés y en alemán.

#  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
#    requiere: -
#    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
#  }

#  Por ejemplo, dados los diccionarios
#    aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#    inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#  se debería devolver res=2



def contar_traducciones_iguales(ing:dict[(str,str)], alm:dict[(str,str)]) -> int:
    counter:int = 0
    for keyIng,valueIng in ing.items():
        for keyAlm,valueAlm in alm.items():
            if keyAlm == keyIng and valueIng == valueAlm:
                counter = counter+1
    
    return counter

aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht", "Pingo":"Pingo"}
unglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand","Pingo":"Pingo","Cara": "Gesicht"}

print(contar_traducciones_iguales(unglés,aleman))

# Ejercicio 4
#
# Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
# y sus valores la cantidad de veces que cada uno de esos números aparece en s

#  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
#    requiere: -
#    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
#  }

#  Por ejemplo, dada la lista
#  lista = [-1,0,4,100,100,-1,-1]
#  se debería devolver res={-1:3, 0:1, 4:1, 100:2}
#  
# RECORDAR QUE NO IMPORTA EL ORDEN DE LAS CLAVES EN UN DICCIONARIO

def contarApariciones(s:list, e:any) -> int:
    counter:int = 0
    for i in s:
        if i == e:
            counter = counter+1
    return counter

def convertir_a_diccionario(lista:list) -> dict:
    diccioporonga: dict = {}
    for i in lista:
        existeKey = False
        for key in diccioporonga:
            if i == key:
                existeKey = True
                break
        
        if not existeKey:
            diccioporonga[i] = 0
        
        diccioporonga[i] += 1
    
    return diccioporonga

print(convertir_a_diccionario(["pinga","pinga","pinga","bingo","bango","bongo","bongo","bongo"]))