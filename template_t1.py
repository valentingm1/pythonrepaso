""" El juego del gallina es una competición en la que dos participantes conducen un vehículo en dirección al del contrario;
si alguno se desvía de la trayectoria de choque pierde y es humillado por comportarse como un "gallina".
Se hizo un torneo para ver quién es el menos gallina. Juegan todos contra todos una vez y van sumando puntos, o restando.
Si dos jugadores juegan y se chocan entre sí, entonces pierde cada uno 5 puntos por haberse dañado.
Si ambos jugadores se desvían, pierde cada uno 10 puntos por gallinas.
Si uno no se desvía y el otro sí, el gallina pierde 15 puntos por ser humillado y el ganador suma 10 puntos!
En este torneo, cada persona que participa tiene una estrategia predefinida para competir: o siempre se devía, o nunca lo hace.
Se debe programar la función 'torneo_de_gallinas' que recibe
un diccionario (donde las claves representan los nombres de los participantes que se anotaron en el torneo, y los valores sus respectivas estrategias)
y devuelve un diccionario con los puntajes obtendidos por cada jugador.

problema torneo_de_gallinas (in estrategias: dict⟨String,String⟩) : dict⟨String,Z⟩ {
  requiere: {estrategias tiene por lo menos 2 elementos (jugadores)}
  requiere: {Las claves de estrategias tienen longitud mayor a 0}
  requiere: {Los valores de estrategias sólo pueden ser los strings "me desvio siempre" ó "me la banco y no me desvio"}
  asegura: {Las claves de res y las claves de estrategias son iguales}
  asegura: {para cada jugador p perteneciente a claves(estrategias), res[p] es igual a la cantidad de puntos que obtuvo al finalizar el torneo, dado que jugó una vez contra cada otro jugador}
} """

def torneo_de_gallinas(strats: dict[str,str]) -> dict[str,int]:
  scores = {jugador:0 for jugador in strats}
  jugadores = list(strats.keys())

    # Simular enfrentamientos sin duplicaciones
  for i in range(len(jugadores)): 
        for j in range(i + 1, len(jugadores)):  # Solo jugadores posteriores
            jugador1 = jugadores[i]
            jugador2 = jugadores[j]
            strat1 = strats[jugador1]
            strat2 = strats[jugador2]

            # Aplicar las reglas del enfrentamiento
            if strat1 == "me desvio siempre" and strat2 == "me desvio siempre":
                scores[jugador1] -= 10
                scores[jugador2] -= 10
            elif strat1 == "me la banco y no me desvio" and strat2 == "me la banco y no me desvio":
                scores[jugador1] -= 5
                scores[jugador2] -= 5
            elif strat1 == "me desvio siempre" and strat2 == "me la banco y no me desvio":
                scores[jugador1] -= 15
                scores[jugador2] += 10
            elif strat1 == "me la banco y no me desvio" and strat2 == "me desvio siempre":
                scores[jugador1] += 10
                scores[jugador2] -= 15

  return scores

estrategias = {
    "Alice": "me desvio siempre",
    "Bob": "me la banco y no me desvio",
    "Charlie": "me desvio siempre"
}

print(torneo_de_gallinas(estrategias))

""" 
2) Cola en el Banco (1 puntos)
En el banco ExactaBank los clientes hacen cola para ser atendidos por un representante.
Los clientes son representados por las tuplas (nombre, tipo afiliado) donde
la primera componente es el nombre y el tipo afiliado puede ser "comun" o "vip".
Se nos pide implementar una función en python que dada una cola de clientes del banco, 
devuelva una nueva cola con los mismos clientes pero en donde los clientes vip 
estan primero que los clientes comunes manteniendo el orden original de los clientes vips y los comunes entre sí.


problema reordenar_cola_priorizando_vips (in filaClientes: Cola⟨String x String⟩) : Cola⟨String⟩ {
  requiere: {La longitud de los valores de la primera componente de las tuplas de la cola filaClientes es mayor a 0}
  requiere: {Los valores de la segunda componente de las tuplas de la cola filaClientes son "comun" o "vip" }
  requiere: {No hay dos tuplas en filaClientes que tengan la primera componente iguales entre sí }
  asegura: {todo valor de res aparece como primera componente de alguna tupla de filaClientes}
  asegura: {|res| = |filaCliente|}
  asegura: {res no tiene elementos repetidos}
  asegura: {No hay ningun cliente "comun" antes que un "vip" en res}
  asegura: {Para todo cliente c1 y cliente c2 de tipo "comun" pertenecientes a filaClientes si c1 aparece antes que c2 en filaClientes entonces el nombre de c1 aparece antes que el nombre de c2 en res}
  asegura: {Para todo cliente c1 y cliente c2 de tipo "vip" pertenecientes a filaClientes si c1 aparece antes que c2 en filaClientes entonces el nombre de c1 aparece antes que el nombre de c2 en res}
} """

import queue

def reordenar_cola_priorizando_vips(filaClientes: queue.Queue[tuple[str,str]]) -> queue.Queue[tuple[str,str]]:
  vips =  queue.Queue()
  comunes = queue.Queue()

  res= queue.Queue()

  while not filaClientes.empty():
    cliente = filaClientes.get()
    nombre,tipo = cliente
    if tipo == "vip":
      vips.put(cliente)
    else: comunes.put(cliente)
  
  while not vips.empty():
    res.put(vips.get())

  while not comunes.empty():
    res.put(comunes.get())
  
  return res

""" ) Sufijos que son palíndromos (2 puntos)
Decimos que una palabra es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda.
Se nos pide programar en python la siguiente función:

problema cuantos_sufijos_son_palindromos(in texto:String) : Z {
  requiere: -
  asegura: {res es igual a la cantidad de palíndromos que hay en el conjunto de sufijos de texto}
}
Nota: un sufijo es una subsecuencia de texto que va desde una posición cualquiera hasta el al final de la palabra. 
Ej: "Diego", el conjunto de sufijos es: "Diego", "iego","ego","go", "o". 
Para este ejercicio no consideraremos a "" como sufijo de ningun texto. """

def esPalindromo(texto:str) -> bool:
  left,right = 0, len(texto)-1
  while left > right:
    if texto[left] != texto[right]:
      return False
    left +=1
    right -=1
  return True


def cuantos_sufijos_son_palindromos(texto:str) -> int:
  contador = 0
  for i in range(len(texto)):
    sufijo = texto[i:]
    if esPalindromo(sufijo):
      contador+=1
  return contador



""" 
4) Ta-Te-Ti-Facilito (2 puntos)
Ana y Beto juegan al Ta-Te-Ti-Facilito. El juego es en un tablero cuadrado de lado entre 5 y 10. 
Cada jugador va poniendo su ficha en cada turno.
Juegan intercaladamente y comienza Ana. Ana pone siempre una 'X' en su turno y Beto pone una 'O' en el suyo.
Gana la persona que logra poner 3 fichas suyas consecutivas en forma vertical.
Si el tablero está completo y no ganó nadie, entonces se declara un empate.
El tablero comienza vacío, representado por ' ' en cada posición.
Dado que juegan por turnos y comienza Ana poniendo una 'X' se cumple que 
la cantidad de 'X' es igual a la cantidad de 'O' o bien la cantidad de 'X' son uno más que la cantidad de 'O'.
Se nos pide implementar una función en python 'problema quien_gano_el_tateti_facilito' que determine si ganó alguno,
o si Beto hizo trampa (puso una 'O' cuando Ana ya había ganado).

problema quien_gano_el_tateti_facilito(in tablero:seq⟨seq⟨Char⟩) : Z {
  requiere: {tablero es una matriz cuadrada}
  requiere: {5<=|tablero[0]|<= 10}
  requiere: {tablero sólo tiene 'X', 'O' y ' ' (espacio vacío) como elementos}
  requiere: {En tablero la cantidad de 'X' es igual a la cantidad de 'O' o bien la cantidad de 'X' es uno más que la cantidad de 'O'}
  asegura: {res = 1 <==> hay tres 'X' consecutivas en forma vertical(misma columna) y no hay tres 'O' consecutivas en forma vertical(misma columna) }
  asegura: {res = 2 <==> hay tres 'O' consecutivas en forma vertical (misma columna) y no hay tres 'X' consecutivas en forma vertical(misma columna) }
  asegura: {res = 0 <==> no hay tres 'O' ni hay tres 'X' consecutivas en forma vertical}
  asegura: {res = 3 <==> hay tres 'X' y hay tres 'O' consecutivas en forma vertical (evidenciando que beto hizo trampa)}
 """

def quien_gano_el_tateti_facilito(tablero:list[list[str]]) -> int:
  res:int = 0

  longitudTablero = len(tablero)
  ganoAna = False
  ganoBeto = False

  for i in range(longitudTablero):
    for j in range(longitudTablero - 2):
      if(tablero[j][i] == "X" and tablero[j+1][i] == "X" and tablero[j+2][i] == "X"):
        ganoAna = True
      if(tablero[j][i] == "O" and tablero[j+1][i] == "O" and tablero[j+2][i] == "O"):
        ganoBeto = True
  
  if(ganoAna and ganoBeto):
    res = 3
  elif(ganoBeto):
    res = 2
  elif(ganoAna):
    res = 1
  else: res = 0

  return res

    
tablero = [
    ['X', ' ', ' ', ' ', ' '],
    ['X', 'O', ' ', ' ', ' '],
    ['X', 'X', 'O', ' ', ' '],
    ['O', 'X', 'O', 'O', ' '],
    ['X', 'X', 'O', 'O', ' ']
]

print(quien_gano_el_tateti_facilito(tablero))