from zope.interface import Interface

class IDirector (Interface):
    def modificarBasico(cuil, nuevoBasico):
        pass
    
    def modificarPorcentajeporcargo(nuevoPorcentaje):
        pass

    def modificarPorcentajeporcategoria(nuevoPorcentaje):
       pass

    def modificarImporteExtra(cuil, nuevoImporteExtra):
       pass

