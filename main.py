from claseLista import Lista
from claseDocenteInvestigador import DocenteInvestigador
from claseObjectEncoder import ObjectEncoder
from claseMenu import Menu
from ITesorero import ITesorero
from IDirector import IDirector

def tesorero(manejador: ITesorero):
    salir = False
    while not salir:
        cuil = input('Ingrese el cuil de un agente (0 para salir): ')
        if cuil == '0':
            salir = True
        else:
            manejador.gastosSueldoPorEmpleado(cuil)
     

def director(manejador: IDirector):
    salir = False
    while not salir:
        print('1- Modificar el sueldo basico de un empleado')
        print('2- Modificar el importe extra de un Docente Investigador')
        print('3- Modificar el porcentaje por cargo')
        print('4- Modificar el porcentaje por categoria')
        print('5- Salir')
        opcion = int(input('Ingrese una opcion: '))
        if opcion == 1:
            cuil = input('Ingrese el cuil de un agente: ')
            nuevoBasico = float(input('Ingrese el nuevo sueldo basico: '))
            manejador.modificarBasico(cuil, nuevoBasico)
        elif opcion == 2:
            cuil = input('Ingrese el cuil de un docente investigador: ')
            nuevoImporteExtra = float(input('Ingrese el nuevo importe extra: '))
            manejador.modificarImporteExtra(cuil, nuevoImporteExtra)
        elif opcion == 3:
            nuevo_porcentaje = float(input('Ingrese el nuevo porcentaje: '))
            manejador.modificarPorcentajeporcargo(nuevo_porcentaje)    
        elif opcion == 4:
            nuevo_porcentaje = float(input('Ingrese el nuevo porcentaje: '))
            manejador.modificarPorcentajeporcategoria(nuevo_porcentaje)
        elif opcion == 5:
            salir = True
            print('Cerrando menu de director...')
        else:
            print('ERROR: Opcion ingresda incorrecta!')   
            input('Presione ENTER para continuar...') 

if __name__ == '__main__':
    objetoEncoder = ObjectEncoder()
    unaLista = Lista()
    objetoMenu = Menu()
    d = objetoEncoder.leerJSONArchivo('personal.json')
    unaLista = objetoEncoder.decodificarDiccionario(d)
    correcto = False
    while not correcto:
        usuario = input('Ingrese el nombre de usuario: ')
        password = input('Ingrese la contrasenia: ')
        if usuario == 'uTesorero'.lower() and password == 'ag@74ck':
            tesorero(ITesorero(unaLista))
            correcto = True
        elif usuario == 'uDirector'.lower() and password == 'ufC77#!1':
            director(IDirector(unaLista))
            correcto = True
        else:
            print('ERROR: Usuario y/o contrasenia incorrectos!')   
            input('Presione ENTER para continuar...') 
    objetoMenu.mostrarMenu(unaLista, objetoEncoder)    
