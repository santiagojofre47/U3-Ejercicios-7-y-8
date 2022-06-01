import abc
from abc import ABC

class Personal(ABC):
    __cuil = None
    __apellido = None
    __nombre = None
    __sueldo_basico = None
    __antiguedad = None

    def __init__(self, cuil = None, apellido = None, nombre = None, sueldo = None, antiguedad = None,carrera = None, cargo = None, catedra = None, area = None, tipo = None, categoria = None):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldo_basico = sueldo
        self.__antiguedad = antiguedad

    def setSueldoBasico(self, unSueldo):
        self.__sueldo_basico = unSueldo    

    def getCUIL(self):
        return self.__cuil

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getSueldoBasico(self):
        return self.__sueldo_basico

    def getAntiguedad(self):
        return self.__antiguedad        
    
    def setSuedo(self, unSueldo):
        if isinstance(unSueldo,float):
            self.__sueldo_basico = unSueldo
    @abc.abstractmethod
    def calcularSueldo(self):
        pass                

    