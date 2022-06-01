from zope.interface import Interface
from zope.interface import implementer

class iInterface(Interface):
    def insertarElemento(posicion, unAparato):
        pass

    def agregarElemento(unAparato):
        pass

    def mostrarElemento(posicion):
        pass



