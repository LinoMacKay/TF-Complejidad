import json
#import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point,Polygon
import networkx as nx
import math
from itertools import permutations


class Departamento:
    def __init__(self,nombreDepartamento):
        self.provincias = []
        self.nombreDepartamento = nombreDepartamento
    def addProvincias(self,provincias):
        self.provincias = provincias
       
class Provincia:
    def __init__(self,nombreProvincia):
        self.distritos = []
        self.nombreProvincia = nombreProvincia
    def addDistritos(self,distritos):
        self.distritos = distritos

class Distrito:
    def __init__(self,nombreDistrito):
        self.nombreDistrito = nombreDistrito
        self.centrosPoblados = []     

    def addCentrosPoblados(self,centrosPoblados):
        self.centrosPoblados = centrosPoblados

class CentroPoblado:
    def __init__(self,latitud,longitud,viviendas,poblacion,distrito,provincia,departamento,nombreCentroPoblado):
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
            'latitud': self.latitud,
            'longitud':self.longitud,
            'viviendas':self.viviendas,
            'poblacion':self.poblacion,
            'distrito':self.distrito,
            'provincia':self.provincia,
            'departamento':self.departamento,
            'nombreCentroPoblado':self.nombreCentroPoblado        
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



def loadProvincias(departamentos,data):
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
        
def loadDistritos(departamentos,data):
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
    

def loadCentroPoblado(Departamentos,data):
    centrosPoblados = []
    for i in data:
        CentroPobladoGuardar = CentroPoblado(i['LATITUD'],i['LONGITUD'],i['VIVIENDAS'],i['POBLACIï¿½N'],i['DISTRITO'],i['PROVINCIA'],i['DEPARTAMENTO'],i['CENTRO POBLADO'])
        centrosPoblados.append(CentroPobladoGuardar)
    
    for i in Departamentos:
        for j in i.provincias:
            for k in j.distritos:
                centrosPobladosguardar = []
                for z in centrosPoblados:
                    if(k.nombreDistrito == z.distrito and j.nombreProvincia == z.provincia and i.nombreDepartamento == z.departamento):
                        centrosPobladosguardar.append(z)
                k.addCentrosPoblados(centrosPobladosguardar)

def getDistancia(nodo1,nodo2):
    x1,x2 = float(nodo1['latitud']),float(nodo2['latitud'])
    y1,y2 = float(nodo1['longitud']),float(nodo2['longitud'])


    d1 = pow((x2-x1),2)
    d2 = pow((y2-y1),2)
    distancia = math.sqrt(d1+d2)
    return float(distancia)

def getTotalDistance(path,G):
    result = 0
    for i in range(len(path)-1):
        result+= G[path[i][0]][path[i+1][0]]['weight']
    result+= G[path[len(path)-1][0]][path[0][0]]['weight']
    return result
    
            

        

def findTspBruteForce(G):
    allPaths = []
    results = []
    for path in permutations(G.nodes(data = True)):
        allPaths.append(path)
    
    for path in allPaths:
        results.append(getTotalDistance(path,G))

    lowerResult = 10000
    for i in results:
        if(i < lowerResult):
            lowerResult = i
    return allPaths[results.index(lowerResult)]


def createGraph(centrosPoblados):

    G = nx.Graph()
    for i in centrosPoblados:
        G.add_node(i.nombreCentroPoblado)
        G.nodes[i.nombreCentroPoblado]['nombre'] = i.nombreCentroPoblado
        G.nodes[i.nombreCentroPoblado]['latitud'] = i.latitud
        G.nodes[i.nombreCentroPoblado]['longitud'] = i.longitud
    
    for i,datai in G.nodes(data= True):
        for j, dataj in G.nodes(data = True):
            if(i != j):
                G.add_edge(i,j)
                G[i][j]['weight'] = getDistancia(datai,dataj)
    #nx.draw_networkx(G)
    #Fuerza Bruta
    path = findTspBruteForce(G)
    for i in path:
        print(i[0])
        print("->")
    

def loadMapa(centrosPoblados):
    street_map = gpd.read_file("TrabajoParcial/departamentos/DEPARTAMENTOS.shp")
    #df = pd.DataFrame.from_records([centro.to_dict() for centro in centrosPoblados])
    #crs = {'init':'epsg:4326'}
    #geometry = [Point(xy) for xy in zip(df['longitud'],df['latitud'])]
    #geo_df = gpd.GeoDataFrame(df,crs = crs, geometry = geometry)
    #fig,ax = plt.subplots(figsize=(55,55))
    #street_map.plot(ax = ax,alpha = 0.4, color="grey")
    #geo_df.plot(ax = ax,markersize = 10,color = "blue",marker = ".", label="centro poblado")
    #plt.legend(prop={'size':15})
    
def selectSpecificCenter(Departamentos,departamentoNombre,provinciaNombre,distritoNombre):
    for i in Departamentos:
        if(i.nombreDepartamento == departamentoNombre):
            Provincias = i.provincias
    for i in Provincias:
        if(i.nombreProvincia == provinciaNombre):
            Distritos = i.distritos
    for i in Distritos:
        if(i.nombreDistrito == distritoNombre):
            return i.centrosPoblados




def LoadData():
    f = open('TrabajoParcial/Data.json',)
    data = json.load(f)
    f.close()
    
    Departamentos = loadDepartamentos(data)
    loadProvincias(Departamentos,data)
    loadDistritos(Departamentos,data)
    loadCentroPoblado(Departamentos,data)
    #la libertad / provincia de pataz / distrito de pataz
    centrosPoblados = selectSpecificCenter(Departamentos,"LA LIBERTAD","PATAZ","PATAZ")
    #loadMapa(centrosPoblados)
    createGraph(centrosPoblados)
LoadData()