from zope.interface import implementer
from Interface import Interface
from ITesorero import ITesorero
from IDirector import IDirector
from claseNodo import Nodo
from clasePersonal import Personal
from claseDocente import Docente
from claseInvestigador import Investigador
from clasePersonalApoyo import PersonalApoyo
from claseDocenteInvestigador import DocenteInvestigador

@implementer(Interface)
@implementer(IDirector)
@implementer(ITesorero)

class Lista:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0

    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato

    def agregarPersonal(self, personal):
            assert isinstance(personal, Personal), "Personal no valido"
            nodo = Nodo(personal)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo=nodo
            self.__actual=nodo
            self.__tope+=1

    def agregarElemento(self, personal):
            assert isinstance(personal, Personal), "Personal no valido"
            nodo = Nodo(personal)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
            self.__actual = nodo
            self.__tope += 1
            print('Personal agregado al final de la lista!')

    def insertarElemento(self, posicion, personal):
        assert isinstance(personal, Personal), "Personal no valido"
        assert isinstance(posicion, int), 'la posicion debe ser un dato entero!'
        aux = self.__comienzo
        i = 0
        encontro = False
        ant = aux
        if posicion>= 0 and posicion <= self.__tope:
            if i == posicion-1:
                if aux.getDato() == None:
                    self.agregarElemento(personal)
                else:
                    nodo = Nodo(personal)
                    nodo.setSiguiente(aux) 
                    aux.setSiguiente(aux.getSiguiente()) 
                    self.__comienzo = nodo
                    self.__actual = nodo
                    self.__tope+=1  
            else:
                while aux != None and not encontro:
                    if i == posicion-1:
                        encontro = True
                        nodo = Nodo(personal)
                        ant.setSiguiente(nodo)
                        nodo.setSiguiente(aux)
                        self.__tope+=1
                        print('Elemento insertado en la posicion: {}' .format(posicion))
                    else:
                        ant = aux
                        aux = aux.getSiguiente()
                        i+=1
        else:
            print('ERROR: Posicion ingresada invalida!')                        

    def mostrarElemento(self, posicion):
        aux = self.__comienzo
        i = 0
        encontro = False
        assert posicion >= 0 and posicion <= self.__tope, "Posicion fuera del rango"
        if i == posicion-1:
            if aux.getDato() != None:
                print('El personal de la posicion {} es {}' .format(posicion,aux.getTipo()))
        else:
            while aux != None and not encontro:
                if posicion-1 == i:
                    encontro = True
                    print('El personal de la posicion {} es {}' .format(posicion,aux.getTipo()))
                   
                else:
                    aux = aux.getSiguiente()
                    i+=1

    def getObjeto(self, posicion):
        objeto = None
        if posicion >= 0 and posicion <= self.__tope:
            aux = self.__comienzo
            i = 0
            encontro = False
            while aux != None and not encontro:
                if i == posicion:
                    objeto = aux.getDato()
                    encontro = True
                else:
                    aux = aux.getSiguiente()
                    i+=1
        return objeto    

    def intercambiarElemento(self, posicion, unPersonal):
        assert isinstance(unPersonal, Personal), "ERROR: Objeto no valido!"
        if posicion >= 0 and posicion <= self.__tope:
            aux = self.__comienzo
            i = 0
            encontro = False
            while aux != None and not encontro:
                if i == posicion:
                    aux.setDato(unPersonal)
                    encontro = True
                else:
                    aux = aux.getSiguiente()
                    i += 1                        

    def ordenarPorNombre(self):
        cota = self.__tope - 1
        k = 1
        while k != -1:
            k = -1
            for i in range(cota):
                personal1 = self.getObjeto(i)
                personal2 = self.getObjeto(i+1)
                if isinstance(personal1, DocenteInvestigador) and isinstance(personal2, DocenteInvestigador):
                    if personal1.getNombre() > personal2.getNombre():
                        self.intercambiarElemento(i, personal2)
                        self.intercambiarElemento(i+1, personal1)
                        k = i
            cota = k 

    def ordenarPorApellido(self):
        cota = self.__tope-1
        k = 1
        while k != -1:
            k = -1
            for i in range(cota):
                personal1 = self.getObjeto(i)
                personal2 = self.getObjeto(i+1)

                if personal1.getApellido() > personal2.getApellido():
                    self.intercambiarElemento(i, personal2)
                    self.intercambiarElemento(i+1, personal1)
                    k = i
            cota = k              

    def mostrarOrdenadoNombre(self, carrera):
        self.ordenarPorNombre()
        encontro = False
        aux = self.__comienzo
        while aux != None:
            if aux.getTipo() == 'Docente Investigador' and aux.getDato().getCarrera().lower() == carrera.lower():
                print(aux.getDato())
                encontro = True
                aux = aux.getSiguiente()
            else:
                aux = aux.getSiguiente()    

        if not encontro:
            print('ERROR: Carrera no encontrada!')   

    def mostrarOrdenadoApellido(self):
        self.ordenarPorApellido()
        aux = self.__comienzo
        while aux != None:
            print('Nombre: {} Apellido: {} Tipo de agente: {} Sueldo: {}' .format(aux.getDato().getNombre(),aux.getDato().getApellido(),aux.getTipo(),aux.getDato().calcularSueldo()))
            aux = aux.getSiguiente()    

    def mostrarPorCategoria(self, categoria):
        assert isinstance(categoria, str), "la categoria debe ser tipo cadena!"
        assert len(categoria) == 1, "Debe ser una cadena de un caracter!"
        aux = self.__comienzo
        encontro = False
        importe = 0
        if aux.getDato() == None:
            print('ERROR: no hay personal cargado!')
        else:
            while aux != None:
                if aux.getTipo() == 'Docente Investigador' and aux.getDato().getCategoria().lower() == categoria.lower():
                    print('Nombre: {} Apellido: {} Importe extra: {}'.format(aux.getDato().getNombre(),aux.getDato().getApellido(),aux.getDato().getSueldoExtra()))
                    importe+=aux.getDato().getSueldoExtra()
                    aux = aux.getSiguiente()
                    encontro = True
                else:
                    aux = aux.getSiguiente()
        if not encontro:
            print('ERROR: categoria no encontrada!')
        else:
            print('Importe a pagar por el Ministerio: {}' .format(importe))                 

    def contarPorArea(self, area):
        assert isinstance(area, str), "El area debe ser una cadena!"
        aux = self.__comienzo
        docentes_investigadores = 0
        investigadores = 0
        encontro = False
        if aux.getDato() == None:       
            print('ERROR: no hay personal cargado!')
        else:
            while aux != None:
                if aux.getTipo() == 'Docente Investigador' and aux.getDato().getArea().lower() == area.lower():
                    docentes_investigadores += 1
                    aux = aux.getSiguiente()
                    encontro = True
                elif aux.getTipo() == 'Investigador' and aux.getDato().getArea().lower() == area.lower():
                    investigadores+=1
                    aux = aux.getSiguiente()
                    encontro = True
                else:
                    aux = aux.getSiguiente()        
        if not encontro:
            print('ERROR: Area no encontrada!')
        else:
            print('Cantidad de docentes investigadores en el area {}: {}'.format(area,docentes_investigadores))
            print('Cantidad de investigadores en el area {}: {}' .format(area,investigadores))      

    #Para ITesorero
    def gastosSueldoPorEmpleado(self, cuil):
        aux = self.__comienzo
        encontro = False

        while aux != None and not encontro:
            if aux.getDato().getCUIL() == cuil:
                encontro = True
                print('Sueldo del agente {} {}: {}'.format(aux.getDato().getApellido(),aux.getDato().getNombre(),aux.getDato().calcularSueldo()))
            else:
                aux = aux.getSiguiente()
        if not encontro:
            print('ERROR: Agente no encontrado!')     
    

    #para IDirector
   
    def modificarBasico(self, cuil, nuevoBasico):
        aux = self.__comienzo
        encontro = False 
        while aux != None and not encontro:
            if aux.getDato().getCUIL() == cuil:
                encontro = True
                aux.getDato().setSuedo(nuevoBasico)
                print('Sueldo modificado con exito!')
            else:
                aux = aux.getSiguiente()
        if not encontro:
            print('ERROR: Agente no encontrado!')     
  

    def modificarImporteExtra(self, cuil, nuevoImporteExtra):
        aux = self.__comienzo
        encontro = False
        while aux != None and not encontro:
            if aux.getTipo() == 'Docente Investigador' and aux.getDato().getCUIL() == cuil:
                encontro = True
                aux.getDato().setImporteExtra(nuevoImporteExtra)
                print('Importe extra modificado con exito!')
            else:
                aux = aux.getSiguiente()
        if not encontro:
            print('ERROR: Agente no encontrado!')            

    def modificarPorcentajeporcargo(self, nuevo_porcentaje):
        print('1- Exclusivo')
        print('2- Semiexclusivo')
        print('3- Simple')
        opcion = int(input('Ingrese una opcion: '))
        Docente.setPorcentaje(opcion, nuevo_porcentaje)

    def modificarPorcentajeporcategoria(self, nuevoPorcentaje):   
        print('1- Categoria 1 a 10')
        print('2- Categoria 11 a 20')
        print('3- Categoria 21 a 22')
        opcion = int(input('Ingrese una opcion: '))
        PersonalApoyo.setPorcentajeCategoria(opcion, nuevoPorcentaje) 

    def toJSON(self):
        d = dict(__class__ = self.__class__.__name__, 
        personales = [personal.toJSON() for personal in self])
        return d