import datetime
import json

class Persona(object):

    def __init__(self, nombre=None, apellido=None, fechaNac=None):

        self.nombre = nombre
        self.apellido = apellido
        self.fechaNac = fechaNac



P1 = Persona("Pepe", "Lopez", "2000/12/2")

listaPersona = [P1, P1, P1, P1, P1]

d = {"Personas": []}

for item in listaPersona:
    d["Personas"].append(item.__dict__)

'''
with open("Diccionario.json", "w") as f:
    for item in d["Personas"]:
        f.write(json.dumps(d, ensure_ascii =False, indent=4))
'''

with open("Diccionario.json","r") as f:
    datos = f.read()
    usable = json.loads(datos)

for item in usable["Personas"]:
    A = Persona()
    A.nombre = item["nombre"]
    A.apellido = item["apellido"]
    A.fechaNac = item["fechaNac"]
    listaPersona.append(A)