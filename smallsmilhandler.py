#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    """
    Clase para manejar un fichero SMIL
    """
    def __init__(self):
        """Constructor. Inicializamos las variables"""

        self.list = []
        self.dicc = {'root-layout': ['width', 'height', 'blackground-color'],
                     'region': ['id', 'top', 'bottom', 'left', 'right'],
                     'img': ['src', 'region', 'dur'],
                     'audio': ['src', 'begin', 'dur'],
                     'textstream': ['src', 'region']}

    def startElement(self, name, attrs):
        """
        Método para etiqueta de inicio
        """
        if name in self.dicc:
            print(name)
            for atributo in self.dicc[name]:
                self.atr = {}
                self.atr[atributo] = attrs.get(atributo, "")
                self.list.append(self.atr)

    def get_tags(self):
        return self.list

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))

    print(cHandler.get_tags())
