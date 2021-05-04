# Trabajo Complejidad Algoritmica

<center><b>Complejidad Algorítmica – CC42</b></center> <br>
<center><b>Trabajo Parcial</b></center> <br>
<center><b> Carrera de Ingeniería de Software y Ciencias de la computación </b></center> <br>
<center><b>Sección: CC42 </b></center> 


# Profesor
  Luis Martín Canaval Sánchez
# Alumnos
 - U201819681 Mac Kay Rodriguez, Lino Raul
 - U20181a275 Tejada Silva, Cledmir Gerardo
 - U20181a576 Jauregui Gonzales, Daniel
 - U201722579 Yuen Delgado, Alonso Manuel


# Introducción
Motivación:  Como grupo de trabajo nos enfocamos en la capacidad de reconocer responsabilidades éticas y profesionales en situaciones de ingeniería y hacer juicios informados, que deben considerar el impacto de las soluciones de ingeniería en contextos globales, económicos, ambientales y sociales. 

Problema: El problema presentado fue "El Problema del Viajante" / "Travelling Salesman Problem" / "TSP"

Este proyecto es intentar generar soluciones para el problema elegido y evaluar si es una solucion posible o no.

# Objetivos
  - Generar posibles soluciones para el problema.
  - Analizar si las soluciones planteadas son viables.

# Marco Teórico 
Para el trabajo utilizaremos 4 maneras para resolver este problema.

# Problema
El problema "Travelling Salesman" trata de buscar la solución de "Dado una lista de ciudades y las distancias entre cada par de ellas, ¿Cuál es la ruta más corta posible que visita cada ciudad exactamente una vez y al finalizar regresa a la ciudad origen?
![problema](https://upload.wikimedia.org/wikipedia/commons/2/23/Nearestneighbor.gif)

# Estado del Arte
# Búsqueda por fuerza bruta
La "Búsqueda por fuerza bruta" consiste en generar permutaciones de todas las posibilidades posibles y de ellas elegir la que cumple con todas las condiciones para ser considerada una solucion.

![Fuerza Bruta](https://image.slidesharecdn.com/introduccionmultihilo-150824031136-lva1-app6892/95/introduccion-algoritmos-multihilo-11-638.jpg?cb=1440388120)

# Grafos
Un grafo es un conjunto de objetos llamados vértices o nodos unidos por enlaces llamados aristas o arcos, que permiten representar relaciones binarias entre elementos de un conjunto.

![Grafo](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/6n-graf.svg/250px-6n-graf.svg.png)

# DFS
DFS es un algoritmo de búsqueda que se utiliza en gráfos. La estrategia de DFS es buscar en profundida, en base a un nodo elegido como inicio recorre los nodos de forma recurrente y se va "expandiendo" hasta que no encuentre un nodo donde continuar y utliza "BackTracking" para repetir el mismo proceso en los nodos vecinos.

![DFS](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Depth-first-tree.svg/250px-Depth-first-tree.svg.png)

# Implementacion
- Generacion del Grafo
  - Para la generación del grafo convertimos el Dataframe a Json mediante https://mapshaper.org/ y lo leemos. 
  - Luego lo convertimos a un arreglo  de objetos que tienen todos los departamentos posibles, y estos contienen sus provincias , así hasta obtener los centros poblados. 
  - Nuestro grafo se genera en base al Departamento y provincia que el usuario ingresa, luego itera creando multiples grafos segun los distritos de las provincias.
 
    ![Paso1](https://media.discordapp.net/attachments/708078392376950807/839264895354273852/unknown.png)
    
    ![Paso2](https://media.discordapp.net/attachments/708078392376950807/839265044888813588/unknown.png)
- Resolucion del problema
  - Luego de generar el grafo, se aplica la solucion deseada y este retorna un arreglo que contiene el camino para luego imprimirlo y continuar con todos los centros poblados       restantes.
  
    ![Paso3](https://media.discordapp.net/attachments/708078392376950807/839264989244424212/unknown.png)
    
  - En caso de que solo exista 1 centro poblado en algun distrito, este retorna como camino solo ese centro poblado.
    
  

# Resolucion con Fuerza Bruta
Para resolverlo con fuerza bruta fue sencillo, mediante "itertools" obtuvimos todas las posibilidades de las conexiones de nodo de un distrito y sus centros poblados. Para luego validar cuál es la distancia mínima y asi retornas el camino que cumple como solución. Esta solucion al ser de complejdad **O(N!)** consume muchos recursos y tiempo para lograr obtener la solución deseado y en algunos casos por falta de estos no se puede obtener la solución.

![Fuerza Bruta Solucion](https://media.discordapp.net/attachments/708078392376950807/839262741704212540/51a43df8-64c1-4a51-afcc-3219118f6695.png)
