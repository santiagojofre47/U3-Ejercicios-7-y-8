from claseLista import Lista
from claseObjectEncoder import ObjectEncoder
from claseDocente import Docente
from claseInvestigador import Investigador
from clasePersonalApoyo import PersonalApoyo
from claseDocenteInvestigador import DocenteInvestigador

class Menu:
    __opcion = None

    def mostrarMenu(self, unaLista, objetoEncoder):
        assert isinstance(unaLista, Lista) and isinstance(objetoEncoder, ObjectEncoder) , "manejadores importados erroneos"
        salir = False
        while not salir:
            print('1- Insertar personal a la lista')
            print('2- Agregar un personal al final de la lista')
            print('3- Mostrar tipo de personal en una posicion dada')
            print('4- Mostrar docentes investigadores de una carrera dada, ordenados alfabeticamente por nombre')
            print('5- Contar docentes y docentes investigadores de un area dada')
            print('6- Mostrar listado del personal ordenado alfabeticamente por apellido')
            print('7- Mostrar datos de los docentes investigadores de una categoria dada e importe total a pagar por el Ministerio')
            print('8- Guardar archivo')
            print('9- Salir')
            self.__opcion = int(input('Ingrese una opcion: '))

            if self.__opcion == 1:
                objeto = self.datoPersonal()
                assert objeto != None, "ERROR: Objeto no valido!"
                posicion = int(input('Ingrese la posicion: '))
                unaLista.insertarElemento(posicion,objeto)
            elif self.__opcion == 2:
                objeto = self.datoPersonal()
                assert objeto != None , "ERROR: Objeto no valido!"
                unaLista.agregarElemento(objeto)  
            elif self.__opcion == 3:
                posicion = int(input('Ingrese la posicon:'))
                unaLista.mostrarElemento(posicion)
            elif self.__opcion == 4:
                carrera = input('Ingrese una carrera: ')
                unaLista.mostrarOrdenadoNombre(carrera)
            elif self.__opcion == 5:
                area = input('Ingrese un area: ')
                unaLista.contarPorArea(area)
            elif self.__opcion == 6:
                unaLista.mostrarOrdenadoApellido()   
            elif self.__opcion == 7:
                categoria = input('Ingrese una categoria: ')
                unaLista.mostrarPorCategoria(categoria)
            elif self.__opcion == 8:
                diccionario = unaLista.toJSON()
                objetoEncoder.guardarJSONArchivo(diccionario, 'personal.json')
                print('Archivo guardado con exito!')
            elif self.__opcion == 9:
                salir = True
                print('Cerrando menu...')
            else:
                print('ERROR: Opcion ingresada invalida!')
                input('Presione ENTER para continuar...')
                
    def datoPersonal(self):
        unPersonal = None
        cuil = input('Ingrese el CUIL: ')
        apellido = input('Ingrese el apellido: ')
        nombre = input('Ingrese el nombre: ')
        sueldoBasico = float(input('Ingrese el sueldo basico: '))
        antiguedad = int(input('Ingrese la antiguedad: '))
        print('\n')
        print('a- Docente')
        print('b- Investigador')
        print('c- Personal de apoyo')
        print('d- Docente investigador')
        opcion = input('ingrese el tipo de personal: ')
        assert len(opcion) == 1, "Debe ser un caracter!"

        if opcion.lower() == 'a':
            carrera = input('Ingrese la carrera del docente: ')
            cargo = input('Ingrese el cargo: ')
            catedra = input('Ingrese la catedra: ')
            unPersonal = Docente(cuil,apellido,nombre,sueldoBasico,antiguedad,carrera,cargo,catedra)
        elif opcion.lower() == 'b':
            area = input('Ingrese el area del investigador: ')
            tipo = input('Ingrese el tipo de investigacion: ')
            unPersonal = Investigador(cuil,apellido,nombre,sueldo,antiguedad,area,tipo)
        elif opcion.lower() == 'c':
            categoria = int(input('Ingrese la categoria de investigacion (1 a 22): '))
            if categoria >= 1 and categoria <= 22:
                unPersonal = PersonalApoyo(cuil,apellido,nombre,sueldoBasico,antiguedad,categoria)
            else:
                print('Categoria ingresada incorrecta! ')
        elif opcion.lower() == 'd':
            carrera = input('Ingrese la carrera del docente: ')
            cargo = input('Ingrese el cargo: ')
            catedra = input('Ingrese la catedra: ')
            area = input('Ingrese el area del investigador: ')
            tipo = input('Ingrese el tipo de investigacion: ')
            categoria = input('Ingrese la categoria (en romano): ')
            sueldoExtra = float(input('Ingrese el sueldo extra: '))
            unPersonal = DocenteInvestigador(cuil,apellido,nombre,sueldoBasico,antiguedad,carrera,cargo,catedra,area,tipo,categoria,sueldoExtra)
        else:
            print('ERROR: Opcion ingresada invalida')
        return unPersonal                    