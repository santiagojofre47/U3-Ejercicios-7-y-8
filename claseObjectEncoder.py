import json
from pathlib import Path
from claseLista import Lista
from clasePersonal import Personal
from claseDocente import Docente
from clasePersonalApoyo import PersonalApoyo
from claseInvestigador import Investigador
from claseDocenteInvestigador import DocenteInvestigador

class ObjectEncoder(object):

    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Lista':
                personales=d['personales']
                dpersonal = personales[0]
                manejador=class_()
                for i in range(len(personales)):
                    dpersonal=personales[i]
                    class_name=dpersonal.pop('__class__')
                    class_=eval(class_name)
                    atributos=dpersonal['__atributos__']
                    unPersonal=class_(**atributos)
                    manejador.agregarPersonal(unPersonal)
                return manejador 

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
        return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)        