import json
import pandas as pd

import sys
from Parcial import LoadData
sys.path.append('../')


url = "../data/poblaciones.csv"


def algorithm1(departamento):
    data = pd.read_csv(url)
    data2 = data[data["DEPARTAMENTO"] == departamento]
    responsePath = []
    for i, row in data2.iterrows():
        responsePath.append({"idx": i,
                             "lat": float(row["LATITUD"]),
                             "lon": float(row["LONGITUD"])})

    return json.dumps(responsePath)


def algorithm():
    data = pd.read_csv(url)
    responsePath = []
    for i, row in data.iterrows():
        responsePath.append({"idx": i,
                             "lat": float(row["LATITUD"]),
                             "lon": float(row["LONGITUD"])})

    return json.dumps(responsePath)


# Utilizar peru1
def peru1():

    data = LoadData()
    #data = pd.read_csv(url)
    #responsePath = []
    # for i, row in data.iterrows():
    #    responsePath.append({"cp": row["CENTRO POBLADO"],
    #                         "lat": float(row["LATITUD"]),
    #                         "lon": float(row["LONGITUD"])})

    return json.dumps(data)


def peru2():
    data = pd.read_csv(url)
    responsePath = []
    for i, row in data.iterrows():
        responsePath.append({"cp": row["CENTRO POBLADO"],
                             "lat": float(row["LATITUD"]),
                             "lon": float(row["LONGITUD"])})

    return json.dumps(responsePath)
