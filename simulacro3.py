'''
Un grupo de amigos apasionados por las salas de escape, esas aventuras inmersivas donde tienen 60 minutos para salir de una habitación resolviendo enigmas,
llevan un registro meticuloso de todas las salas de escape que hay en Capital. 
Este registro indica si han visitado una sala y si pudieron o no salir de ella.
Un 0 significa que no fueron, un 61 que no lograron salir a tiempo, y un número entre 1 y 60 representa los minutos que les tomó escapar exitosamente.
Con estos datos, pueden comparar sus logros y desafíos en cada nueva aventura que emprenden juntos.

1) Promedio de salidas [2 puntos]

Dado un diccionario donde la clave es el nombre de cada amigo y el valor es una lista de los tiempos (en minutos)
registrados para cada sala de escape en Capital, escribir una función en Python que devuelva un diccionario.
En este nuevo diccionario, las claves deben ser los nombres de los amigos y los valores deben ser tuplas que
indiquen la cantidad de salas de las que cada persona logró salir y el promedio de los tiempos de salida
(solo considerando las salas de las que lograron salir)

problema promedio_de_salidas (in registro: dict⟨String, seq⟨Z⟩⟩) : dict⟨String, ⟨Z x R⟩⟩ {
  requiere: {registro tiene por lo menos un integrante}
  requiere: {Todos los integrantes de registro tiene por lo menos un tiempo}
  requiere: {Todos los valores de registro tiene la misma longitud}
  requiere: {Todos los tiempos de los valores de registro están entre 0 y 61 inclusive}
  asegura: {res tiene las mismas claves que registro}
  asegura: {El primer elemento de la tupla de res para un integrante, es la cantidad de salas con tiempo mayor estricto a 0 y menor estricto a 61 que figuran en sus valores de registro}
  asegura: {El segundo elemento de la tupla de res para un integrante, si la cantidad de salas de las que salió es mayor a 0: es el promedio de salas con tiempo mayor estricto a 0 y menor estricto a 61 que figuran en sus valores de registro; sino es 0.0}
}  '''
# registro: {mongo:[45,32,21], mongo2:[12,4,1,61,9]}
#res {mongo:(3, 32.66), mongo2:(4, 6.5)}

def cantidadDeSalas(s:list) -> int:
  counter = 0
  for i in s:
    counter+=1
  
  return counter

def sumarLista(s:list) -> int:
  total:int = 0
  for i in s:
    total= total + i
  
  return total



def promedio_de_salidas(registro:dict[str,list[int]]) -> dict[str,list[int,float]]:
  res:dict[str,list[int,float]] ={}
  for key,value in registro.items():
    totalTiempo = 0
    for tiempos in value:
      totalTiempo += sumarLista(tiempos)
      res[key] = (cantidadDeSalas(tiempos),totalTiempo/cantidadDeSalas(tiempos))
  
  return res

  
    

""" registro = {
    "Juan": [[30, 45, 25], [60, 50, 30], [5, 10, 15]],
    "Maria": [[20, 30, 40], [10, 60, 55], [35, 40]],
    "Pedro": [[10, 20, 30], [5, 10, 0], [0, 10, 25]],
}

resultados = promedio_de_salidas(registro)
print(resultados) """

""" 2) Tiempo más rápido [1 punto]

Dada una lista con los tiempos (en minutos) registrados para cada sala de escape de Capital,
escribir una función en Python que devuelva la posición (índice) en la cual se encuentra el tiempo más rápido,
excluyendo las salas en las que no haya salido (0 o mayor a 60).

problema tiempo_mas_rapido (in tiempos_salas: seq⟨Z⟩): Z {
  requiere: {Hay por lo menos un elemento en tiempos_salas entre 1 y 60 inclusive}
  requiere: {Todos los tiempos en tiempos_salas están entre 0 y 61 inclusive}
  asegura: {res es la posición de la sala en tiempos_salas de la que más rápido se salió (en caso que haya más de una, devolver la primera, osea la de menor índice)}
} """

def tiempo_mas_rapido(tiempo_salas:list[int]) -> int:
  indexADevolver:int = 0
  indexCounter:int = 0
  elementCounter:int = 0

  for i in tiempo_salas:
    if i > elementCounter:
      elementCounter = i
      indexADevolver = indexCounter
    indexCounter+=1

  return (elementCounter,indexADevolver)
print(tiempo_mas_rapido([45,6,3,2,60,21,4,1]))


""" 3) Escape en solitario [2 puntos]
Dada una matriz donde las columnas representan a cada amigo y las filas representan las salas de escape, y los valores son los tiempos (en minutos) registrados para cada 
sala (0 si no fueron, 61 si no salieron, y un número entre 1 y 60 si salieron), escribir una función en Python que devuelva los índices de todas las filas (que representan 
las salas) en las cuales el primer, segundo y cuarto amigo no fueron (0), pero el tercero sí fue (independientemente de si salió o no).

problema escape_en_solitario (in amigos_por_salas: seq⟨seq⟨Z⟩⟩): seq⟨Z⟩ {
  requiere: {Hay por lo menos una sala en amigos_por_salas}
  requiere: {Hay 4 amigos en amigos_por_salas}
  requiere: {Todos los tiempos en cada sala de amigos_por_salas están entre 0 y 61 inclusive}
  asegura: {La longitud de res es menor igual que la longitud de amigos_por_salas}
  asegura: {Por cada sala en amigos_por_salas cuyo primer, segundo y cuarto valor sea 0, y el tercer valor sea distinto de 0, la posición de dicha sala en amigos_por_salas 
            debe aparecer res}
  asegura: {Para todo i pertenciente a res se cumple que el primer, segundo y cuarto valor de amigos_por_salas[i] es 0, y el tercer valor es distinto de 0}
}
 """

def escape_en_solitario(amigosPorSalas: list[list[int]]) -> list[int]:
  res = []
  index:int = 0

  for i in amigosPorSalas:
    if i[0] == 0 and i[1] == 0 and not i[2] == 0 and i[3] == 0:
      res.append(index)
    index+=1
  
  return res

amigos_por_salas = [
    [0, 0, 1, 0],  # Cumple (primer, segundo, cuarto = 0; tercero ≠ 0)
    [0, 0, 0, 0],  # No cumple (tercero = 0)
    [0, 1, 1, 0],  # No cumple (segundo ≠ 0)
    [0, 0, 5, 0]   # Cumple
]

print(escape_en_solitario(amigos_por_salas))  # Salida esperada: [0, 3]


""" 4) Subsecuencia más larga de salidas [3 puntos]
Dada una lista con los tiempos (en minutos) registrados para cada sala de escape a la que fue una persona, escribir una función en Python que devuelva una tupla con el índice 
de inicio y el índice de fin de la subsecuencia más larga de salidas exitosas de salas de escape consecutivas.

problema racha_mas_larga (in tiempos: seq⟨Z⟩): ⟨Z x Z⟩ {
  requiere: {Hay por lo menos un elemento en tiempos entre 1 y 60 inclusive}
  requiere: {Todos los tiempos en tiempos están entre 0 y 61 inclusive}
  asegura: {En la primera posición de res está la posición (índice de la lista) de la sala que inicia la racha más larga}
  asegura: {En la segunda posición de res está la posición (índice de la lista) de la sala que finaliza la racha más larga}
  asegura: {El elemento de la primer posición de res en tiempos es mayor estricto 0 y menor estricto que 61}
  asegura: {El elemento de la segunda posición de res en tiempos es mayor estricto 0 y menor estricto que 61}
  asegura: {La primera posición de res es menor o igual a la segunda posición de res }
  asegura: {No hay valores iguales a 0 o a 61 en tiempos entre la primer posición de res y la segunda posición de res}
  asegura: {No hay otra subsecuencia de salidas exitosas, en tiempos, de mayor longitud que la que está entre la primer posición de res y la segunda posición de res}
  asegura: {Si hay dos o más subsecuencias de salidas exitosas de mayor longitud en tiempos, res debe contener la primera de ellas.}
} """

def racha_mas_larga(tiempos: list[int]) -> tuple[int, int]:
    # Variables para rastrear la racha actual
    inicio_actual = 0
    longitud_actual = 0
    
    # Variables para rastrear la racha más larga
    inicio_mejor = -1
    longitud_mejor = 0

    # Iterar sobre los tiempos
    for i in range(len(tiempos)):
        if 1 <= tiempos[i] <= 60:
            # Si el tiempo es una salida exitosa, extendemos la racha actual
            if longitud_actual == 0:
                inicio_actual = i  # Nueva racha comienza
            longitud_actual += 1
        else:
            # Si el tiempo no es válido, revisamos si la racha actual es la mejor
            if longitud_actual > longitud_mejor:
                inicio_mejor = inicio_actual
                longitud_mejor = longitud_actual
            # Reiniciamos la racha actual
            longitud_actual = 0

    # Última comparación después de salir del bucle
    if longitud_actual > longitud_mejor:
        inicio_mejor = inicio_actual
        longitud_mejor = longitud_actual

    # Devolver la tupla con el inicio y el fin de la racha más larga
    return (inicio_mejor, inicio_mejor + longitud_mejor - 1)