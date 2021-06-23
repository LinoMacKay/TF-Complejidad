import json
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
import networkx as nx
import math
from random import choice, sample
from itertools import permutations
import heapq as hq


class Departamento:
    def __init__(self, nombreDepartamento):
        self.provincias = []
        self.nombreDepartamento = nombreDepartamento

    def addProvincias(self, provincias):
        self.provincias = provincias


class Provincia:
    def __init__(self, nombreProvincia):
        self.distritos = []
        self.nombreProvincia = nombreProvincia

    def addDistritos(self, distritos):
        self.distritos = distritos


class Distrito:
    def __init__(self, nombreDistrito):
        self.nombreDistrito = nombreDistrito
        self.centrosPoblados = []

    def addCentrosPoblados(self, centrosPoblados):
        self.centrosPoblados = centrosPoblados


class CentroPoblado:
    def __init__(self, latitud, longitud, viviendas, poblacion, distrito, provincia, departamento, nombreCentroPoblado):
        self.latitud = latitud
        self.longitud = longitud
        self.viviendas = viviendas
        self.poblacion = poblacion
        self.distrito = distrito
        self.provincia = provincia
        self.nombreCentroPoblado = nombreCentroPoblado
        self.departamento = departamento
        #self.Point = Point(self.longitud,self.latitud)

    def __str__(self):
        return str(self.__dict__)

    def to_dict(self):
        return {
            'lat': self.latitud,
            'lon': self.longitud,
            'viviendas': self.viviendas,
            'poblacion': self.poblacion,
            'distrito': self.distrito,
            'provincia': self.provincia,
            'departamento': self.departamento,
            'cp': self.nombreCentroPoblado
        }


def loadDepartamentos(data):
    ListOfDepartamentos = []
    for i in data:
        ListOfDepartamentos.append(i['DEPARTAMENTO'])
    SetOfDepartamentos = set(ListOfDepartamentos)
    Departamentos = []
    for i in SetOfDepartamentos:
        Departamentoguardar = Departamento(i)
        Departamentos.append(Departamentoguardar)
    return Departamentos


def loadProvincias(departamentos, data):
    Provincias = []
    for i in departamentos:
        listOfProvincias = []
        for j in data:
            if(i.nombreDepartamento == j['DEPARTAMENTO']):
                provinciaGuardar = j['PROVINCIA']
                listOfProvincias.append(provinciaGuardar)
        setOfProvincias = set(listOfProvincias)
        i.addProvincias(list(setOfProvincias))

    for i in departamentos:
        addingPronvicias = []
        for j in i.provincias:
            j = Provincia(j)
            addingPronvicias.append(j)
        i.addProvincias(addingPronvicias)


def loadDistritos(departamentos, data):
    Distritos = []
    for i in departamentos:
        for k in i.provincias:
            listOfDistricts = []
            for j in data:
                if(k.nombreProvincia == j['PROVINCIA']):
                    distritoGuardar = j['DISTRITO']
                    listOfDistricts.append(distritoGuardar)
                setOfDistricts = set(listOfDistricts)
                k.addDistritos(list(setOfDistricts))

    for i in departamentos:
        for k in i.provincias:
            addingDistrito = []
            for j in k.distritos:
                j = Distrito(j)
                addingDistrito.append(j)
            k.addDistritos(addingDistrito)


def loadCentroPoblado(Departamentos, data):
    centrosPoblados = []
    for i in data:
        CentroPobladoGuardar = CentroPoblado(
            i['LATITUD'], i['LONGITUD'], i['NMI1'], i['NMI2'], i['DISTRITO'], i['PROVINCIA'], i['DEPARTAMENTO'], i['CENTRO POBLADO'])
        centrosPoblados.append(CentroPobladoGuardar)

    for i in Departamentos:
        for j in i.provincias:
            for k in j.distritos:
                centrosPobladosguardar = []
                for z in centrosPoblados:
                    if(k.nombreDistrito == z.distrito and j.nombreProvincia == z.provincia and i.nombreDepartamento == z.departamento):
                        centrosPobladosguardar.append(z)
                k.addCentrosPoblados(centrosPobladosguardar)


def getTotalDistance(path, G):
    result = 0
    for i in range(len(path)-1):
        result += G[path[i][0]][path[i+1][0]]['weight']
    result += G[path[len(path)-1][0]][path[0][0]]['weight']
    return result


def getDistancia(nodo1, nodo2):
    x1, x2 = float(nodo1['latitud']), float(nodo2['latitud'])
    y1, y2 = float(nodo1['longitud']), float(nodo2['longitud'])
    d1 = pow(x2-x1, 2)
    d2 = pow(y2-y1, 2)
    distancia = math.sqrt(d1+d2)
    return float(distancia)


def createGraph(centrosPoblados, algtype):
    G = nx.Graph()
    x = 0
    n = len(list(centrosPoblados))
    for j in range(n):
        G.add_node(centrosPoblados[j].nombreCentroPoblado)
        G.nodes[centrosPoblados[j].nombreCentroPoblado]['nombre'] = centrosPoblados[j].nombreCentroPoblado
        G.nodes[centrosPoblados[j].nombreCentroPoblado]['latitud'] = centrosPoblados[j].latitud
        G.nodes[centrosPoblados[j].nombreCentroPoblado]['longitud'] = centrosPoblados[j].longitud
    x += 1

    for i, datai in G.nodes(data=True):
        for j, dataj in G.nodes(data=True):
            if(i != j):
                G.add_edge(i, j)
                G[i][j]['weight'] = getDistancia(datai, dataj)
    # nx.draw_networkx(G)

    if(algtype == 1):
        path = findTspBruteForce(G)
    if(algtype == 2):
        path = DFS(G)
    if(algtype == 3):
        path = dijkstra(G)
    if(algtype == 4):
        path = bfs(G)

    return path


def selectSpecificCenter(Departamentos, departamentoNombre, provinciaNombre, distritoNombre):
    for i in Departamentos:
        if(i.nombreDepartamento == departamentoNombre):
            Provincias = i.provincias
    for i in Provincias:
        if(i.nombreProvincia == provinciaNombre):
            Distritos = i.distritos
    for i in Distritos:
        if(i.nombreDistrito == distritoNombre):
            return i.centrosPoblados


def findTspBruteForce(G):
    allPaths = []
    results = []
    for path in permutations(G.nodes(data=True)):
        allPaths.append(path)

    if(G.size()) > 1:
        for path in allPaths:
            results.append(getTotalDistance(path, G))

        lowerResult = 10000
        for i in results:
            if(i < lowerResult):
                lowerResult = i
        return allPaths[results.index(lowerResult)]
    else:
        return allPaths[0]


def bfs(G):

    print(G.nodes())
    print("Elige el elemento que desees: ")
    a = input()
    queue = [a]
    bfs_traversal_output = []
    for u in G.nodes:
        G.nodes[u]['visited'] = False
        G.nodes[u]['π'] = -1
    G.nodes[a]['visited'] = True
    while queue:
        u = queue[0]
        bfs_traversal_output.append(u)
        for v in G.neighbors(u):
            if not G.nodes[v]['visited']:
                G.nodes[v]['visited'] = True
                G.nodes[v]['π'] = u
                queue.append(v)
        del queue[0]

    return bfs_traversal_output


def DFS(G):
    path = []
    nodes = list(G.nodes())
    a = sample(nodes, 1)
    stack = [a[0]]
    path.append(G.nodes[a[0]])
    for u in G.nodes:
        G.nodes[u]['visited'] = False
        G.nodes[u]['π'] = -1
    while stack:
        u = stack.pop()
        neighbors = False
        aux = G.nodes[u]
        aux2 = u
        if not G.nodes[u]['visited']:
            G.nodes[u]['visited'] = True
            minWeight = 99999999
            for v in reversed(list(G.neighbors(u))):
                if not G.nodes[v]['visited']:
                    neighbors = True
                if G.edges[(u, v)]['weight'] < minWeight and not G.nodes[v]['visited']:
                    minWeight = G.edges[(u, v)]['weight']
                    aux = G.nodes[v]
                    aux2 = v
            if neighbors:
                stack.append(aux2)
                path.append(aux)
    return path


def dijkstra(G):

    print(G.nodes())
    print("Elige el elemento que desees: ")
    b = input()
    q = [b]
    dijkstra_output = []
    for u in G.nodes:
        G.nodes[u]['visited'] = False
        G.nodes[u]['path'] = -1
        G.nodes[u]['cost'] = math.inf
    G.nodes[b]['cost'] = 0
    q = [(0, b)]

    while q:
        current_g, u = hq.heappop(q)
        dijkstra_output.append(u)
        if not G.nodes[u]['visited']:
            G.nodes[u]['visited'] = True
            for v in G.neighbors(u):
                if not G.nodes[v]['visited']:
                    distancia = G.edges[u, v]['weight']
                    suma = current_g + distancia
                    costo = G.nodes[v]['cost']
                if suma < costo:
                    G.nodes[v]['cost'] = suma
                    G.nodes[v]['path'] = u
                    hq.heappush(q, (suma, v))

    print("El costo del grafo es: " + str(costo))
    return dijkstra_output


def PeruTsp1(DataToUse):
    centrosPoblados = getAllCaminosByListOfDistricts(
        'CUSCO', 'ACOMAYO', DataToUse)
    caminos = []
    for i in range(len(centrosPoblados)):
        caminos.append(createGraph(centrosPoblados[i], 1))
    print(caminos)


def getAllCaminosByListOfDistricts(Departamento, Provincia, data):
    distritos = []
    centrosPoblados = []
    for departamento in data:
        for provincia in departamento.provincias:
            if(departamento.nombreDepartamento == Departamento and provincia.nombreProvincia == Provincia):
                distritos = provincia.distritos
    for distrito in distritos:
        centrosPoblados.append(selectSpecificCenter(
            data, Departamento, Provincia, distrito.nombreDistrito))
    return centrosPoblados


def getAllCaminosByListOfProvincias(Departamento, data):
    provincias = []
    centrosPoblados = []
    for departamento in data:
        if(departamento.nombreDepartamento == Departamento):
            provincias = departamento.provincias

    for provincia in provincias:
        for distrito in provincia.distritos:
            centrosPoblados.append(selectSpecificCenter(
                data, Departamento, provincia.nombreProvincia, distrito.nombreDistrito))
    return centrosPoblados


def getAllCaminosByListOfDepartamentos(data):
    centrosPoblados = []
    departamentos1 = []
    for departamento in data:
        departamentos1.append(departamento)

    for departamento in departamentos1:
        for provincia in departamento.provincias:
            for distrito in provincia.distritos:
                centrosPoblados.append(selectSpecificCenter(
                    data, departamento.nombreDepartamento, provincia.nombreProvincia, distrito.nombreDistrito))
    return centrosPoblados


def getProvinciasByDepartamentoName(Departamento, data):
    provincias = []
    for departamento in data:
        if(departamento.nombreDepartamento == Departamento):
            provincias = departamento.provincias
    return provincias


def LoadData():
    f = open('Data3.json', encoding='UTF-8')
    data = json.load(f)
    f.close()

    DataToUse = loadDepartamentos(data)
    loadProvincias(DataToUse, data)
    loadDistritos(DataToUse, data)
    loadCentroPoblado(DataToUse, data)
    PeruTsp1(DataToUse)


LoadData()
