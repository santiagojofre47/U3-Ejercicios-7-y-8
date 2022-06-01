from clasePersonal import Personal

class Docente(Personal):
    __carrera = None
    __cargo = None
    __catedra = None
    porcentajeExclusivo = 50
    porcentajeSemiexclusivo = 20
    porcentajeSimple = 10

    def __init__(self, cuil = None, apellido = None, nombre = None, sueldo = None, antiguedad = None,carrera = None, cargo = None, catedra = None, area = None, tipo = None):
        super().__init__(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra,area,tipo)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra

    def getCarrera(self):
        return self.__carrera

    def getCargo(self):
        return self.__cargo

    def getCatedra(self):
        return self.__catedra   

    @classmethod
    def getPocentajeCargo(cls, op):
        assert isinstance(op, int)
        porcentaje = None
        if op == 1:
            porcentaje = cls.porcentajeExclusivo
        elif op == 2:
            porcentaje = cls.porcentajeSemiexclusivo
        elif op == 3:
            porcentaje = cls.porcentajeSimple      
        return porcentaje        

    @classmethod
    def setPorcentaje(cls, op, nuevo_porcentaje):    
        assert isinstance(op, int)
        if op == 1:
            cls.porcentajeExclusivo = nuevo_porcentaje
            print('Porcentaje por cargo exclusivo modificado con exito!')
        elif op == 2:
            cls.porcentajeSemiexclusivo = nuevo_porcentaje
            print('Porcentaje por cargo semiexclusivo modificado con exito!')
        elif op == 3:
            cls.porcentajeSimple = nuevo_porcentaje
            print('Porcentaje por cargo simple modificado con exito!')
        else:
            print('ERROR: Opcion ingresada incorrecta!')    
                   
    def calcularSueldo(self):
        sueldo = super().getSueldoBasico()+((super().getAntiguedad()*super().getSueldoBasico())/100)
        if self.__cargo == 'Simple':
            sueldo += super().getSueldoBasico()+((Docente.getPocentajeCargo(1)*super().getSueldoBasico())/100)
        elif self.__cargo == 'Semiexclusivo':
            sueldo += super().getSueldoBasico()+((Docente.getPocentajeCargo(2)*super().getSueldoBasico())/100)
        elif self.__cargo == 'Exclusivo':
            sueldo += super().getSueldoBasico()+((Docente.getPocentajeCargo(3)*super().getSueldoBasico())/100)
        return sueldo

    def __str__(self):
        return 'Nombre: {} carrera: {}  cargo: {} catedra: {}' .format(super().getNombre(),self.__carrera, self.__cargo, self.__catedra)    

    def toJSON(self):
        d = dict(__class__ = self.__class__.__name__,
        __atributos__ = dict(cuil = super().getCUIL(),
        apellido = super().getApellido(),
        nombre = super().getNombre(),
        sueldo = super().getSueldoBasico(),
        antiguedad = super().getAntiguedad(),
        carrera = self.__carrera,
        cargo = self.__cargo,
        catedra = self.__catedra
        ))    
        return d

        
    




