# -*- coding: utf-8 -*-
"""
Este es un script de Python
Nos ayudara a ver como se importa este modulo, desde otro
"""

__author__ = "David Quintanar Pérez"
__credits__ = ["David Quintanar Pérez"]
__version__ = "1.0.0"


def saludar_formal(nombre="Mundo"):
    print("Buen día {}".format(nombre))
    
def saludar_informal(nombre="Mundo"):
    print("Que onda {}!".format(nombre))
    
def main():
    print("Modulo importable")
    
if __name__ == "__main__":
    main()