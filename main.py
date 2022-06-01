from claseLista import Lista
from claseDocenteInvestigador import DocenteInvestigador
from claseObjectEncoder import ObjectEncoder
from claseMenu import Menu
from ITesorero import ITesorero
from IDirector import IDirector

def tesorero(manejador: ITesorero):
        cuil = input('Ingrese el cuil de un agente: ')
        manejador.gastosSueldoPorEmpleado(cuil)

def director(manejador: IDirector):
        print('1- Modificar el sueldo basico de un empleado')
        print('2- Modificar el importe extra de un Docente Investigador')
        print('3- Modificar el porcentaje por cargo')
        print('4- Modificar el porcentaje por categoria')
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
            
        else:
            print('ERROR: Opcion ingresda incorrecta!')    

if __name__ == '__main__':
    objetoEncoder = ObjectEncoder()
    unaLista = Lista()
    objetoMenu = Menu()
    d = objetoEncoder.leerJSONArchivo('personal.json')
    unaLista = objetoEncoder.decodificarDiccionario(d)
    usuario = input('Ingrese el nombre de usuario: ')
    password = input('Ingrese la contrasenia: ')
    if usuario == 'uTesorero'.lower() and password == 'ag@74ck':
        tesorero(ITesorero(unaLista))
       
    elif usuario == 'uDirector'.lower() and password == 'ufC77#!1':
        director(IDirector(unaLista))
    else:
        print('ERROR: Usuario y/o contrasenia incorrectos!')    
    objetoMenu.mostrarMenu(unaLista, objetoEncoder)    
        




    




   
  