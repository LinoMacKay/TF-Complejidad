import json

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

    



def LoadData():
    f = open('D:\Proyectos\Complejidad\TrabajoParcial\Data.json',)
    data = json.load(f)
    f.close()
    
    Departamentos = loadDepartamentos(data)
    loadProvincias(Departamentos,data)
    loadDistritos(Departamentos,data)
    loadCentroPoblado(Departamentos,data)
    print(Departamentos)
LoadData()