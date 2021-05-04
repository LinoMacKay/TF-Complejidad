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
