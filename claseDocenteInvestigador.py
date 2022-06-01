from claseDocente import Docente
from claseInvestigador import Investigador
from clasePersonalApoyo import PersonalApoyo

class DocenteInvestigador(Docente,Investigador):
    __sueldoExtra = None
    __categoria = None
    
    
    def __init__(self, cuil = None, apellido = None, nombre = None, sueldo = None, antiguedad = None,carrera = None, cargo = None, catedra = None, area = None, tipo = None, categoria = None, sueldoExtra = None):
        super().__init__(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra,area,tipo)
        self.__sueldoExtra = sueldoExtra
        self.__categoria = categoria

    def __str__(self):
        return 'CUIL: {} Apellido: {} Nombre: {} Sueldo: {} Antiguedad: {} Cargo: {} Catedra: {} Area: {} Tipo: {} Sueldo extra: {} Categoria: {}' .format(super().getCUIL(),super().getApellido(),
        super().getNombre(),super().getSueldoBasico(),super().getAntiguedad(),super().getCargo(),super().getCatedra(),super().getArea(),super().getTipoInvestigacion(),self.__sueldoExtra,self.__categoria)

    def calcularSueldo(self):
        sueldo = Docente.calcularSueldo(self)
        sueldo+= self.__sueldoExtra    
        return sueldo  

    def getCategoria(self):
        return self.__categoria    

    def getSueldoExtra(self):
        return self.__sueldoExtra 
    
    def setImporteExtra(self, nuevoImporteExtra):
        self.__sueldoExtra = nuevoImporteExtra

    def toJSON(self):
        d = dict(__class__ = self.__class__.__name__,
        __atributos__ = dict(cuil = super().getCUIL(),
        apellido = super().getApellido(),
        nombre = super().getNombre(),
        sueldo = super().getSueldoBasico(),
        antiguedad = super().getAntiguedad(),
        carrera = super().getCarrera(),
        cargo = super().getCargo(),
        catedra = super().getCatedra(),
        area = super().getArea(),
        tipo = super().getTipoInvestigacion(),
        categoria = self.__categoria,
        sueldoExtra = self.__sueldoExtra
        )
        )       
        return d
                



