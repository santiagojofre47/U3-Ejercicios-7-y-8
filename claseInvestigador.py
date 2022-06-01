from clasePersonal import Personal

class Investigador(Personal):
    __area = None
    __tipo_investigacion = None

    def __init__(self, cuil = None, apellido = None, nombre = None, sueldo = None, antiguedad = None,carrera = None, cargo = None, catedra = None, area = None, tipo = None):
        super().__init__(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra,area,tipo)
        self.__area = area
        self.__tipo_investigacion = tipo

    def getArea(self):
        return self.__area

    def getTipoInvestigacion(self):
        return self.__tipo_investigacion   

    def calcularSueldo(self):
        sueldo = super().getSueldoBasico()+((super().getAntiguedad()*super().getSueldoBasico())/100)
        return sueldo

    def toJSON(self):
        d = dict(__class__ = self.__class__.__name__,
        __atributos__ = dict(cuil = super().getCUIL(),
        apellido = super().getApellido(),
        nombre = super().getNombre(),
        sueldo = super().getSueldoBasico(),
        antiguedad = super().getAntiguedad(),
        area = self.__area,
        tipo = self.__tipo_investigacion
        )    
        )
        return d
                 
