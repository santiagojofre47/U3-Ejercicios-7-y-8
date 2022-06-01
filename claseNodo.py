from clasePersonal import Personal
from clasePersonalApoyo import PersonalApoyo
from claseDocente import Docente
from claseInvestigador import Investigador

class Nodo:
    __personal=None
    __siguiente=None

    def __init__(self, personal):
        assert isinstance(personal, Personal), "Personal no valido"
        self.__personal = personal
        self.__siguiente=None
    
    def getTipo(self):
        tipo=None
        if type(self.__personal)==Docente:
            tipo='Docente'
        elif type(self.__personal)==PersonalApoyo:
            tipo='Personal Apoyo'
        elif type(self.__personal)==Investigador:
            tipo='Investigador'
        else:
            tipo='Docente Investigador'
        return tipo

    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__personal

    def setDato(self, unDato):
        assert isinstance(unDato, Personal)
        self.__personal = unDato    