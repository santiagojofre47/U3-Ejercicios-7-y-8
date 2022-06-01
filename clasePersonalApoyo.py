from clasePersonal import Personal

class PersonalApoyo(Personal):
    __categoria = None
    porcentajeCategoria1a10 = 10
    porcentajeCategoria11a20 = 20
    porcentajeCategoria21a22 = 30

    def __init__(self, cuil = None, apellido = None, nombre = None, sueldo = None, antiguedad = None, categoria = None):
        super().__init__(cuil,apellido,nombre,sueldo,antiguedad)
        self.__categoria = categoria
    
    @classmethod
    def getPorcentajeCategoria(cls, op):
        assert isinstance(op, int)
        porcentaje = None
        if op == 1:
            porcentaje = cls.porcentajeCategoria1a10
        elif op == 2:
            porcentaje = cls.porcentajeCategoria11a20
        elif op == 3:
            porcentaje = cls.porcentajeCategoria21a22
        return porcentaje    
           
    @classmethod
    def setPorcentajeCategoria(cls, op, nuevo_porcentaje):
        assert isinstance(op, int)
        if op == 1:
            cls.porcentajeCategoria1a10 = nuevo_porcentaje
            print('Porcentaje modificado con exito!')
        elif op == 2:
            cls.porcentajeCategoria11a20 = nuevo_porcentaje
            print('Porcentaje modificado con exito!')
        elif op == 3:
            cls.porcentajeCategoria21a22 = nuevo_porcentaje 
            print('Porcentaje modificado con exito!')      
                 
            
    def calcularSueldo(self):
        sueldo = super().getSueldoBasico()+((super().getAntiguedad()*super().getSueldoBasico())/100)
        if self.__categoria >= 1 and self.__categoria <= 10:
            sueldo += super().getSueldoBasico()+((PersonalApoyo.getPorcentajeCategoria(1)*super().getSueldoBasico())/100)
        elif self.__categoria >= 11 and self.__categoria <= 20:
            sueldo += super().getSueldoBasico()+((PersonalApoyo.getPorcentajeCategoria(2)*super().getSueldoBasico())/100)
        elif self.__categoria >= 21 and self.__categoria <= 22:
            sueldo += super().getSueldoBasico()+((PersonalApoyo.getPorcentajeCategoria(3)*super().getSueldoBasico())/100)
        return sueldo  

    def __str__(self):
        return f'{self.__categoria}'     

    def toJSON(self):
        d = dict(__class__ = self.__class__.__name__,
        __atributos__ = dict(cuil = super().getCUIL(),
        apellido = super().getApellido(),
        nombre = super().getNombre(),
        sueldo = super().getSueldoBasico(),
        antiguedad = super().getAntiguedad(),
        categoria = self.__categoria
        )    
        )
        return d



