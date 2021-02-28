import argparse

def parsear_argumentos():
    parser = argparse.ArgumentParser(
        description="""
        En este Script personalizamos un saludo
        """
    )

    parser.add_argument("saludo", help="""
                        Indica el metodo que se quiere usar.
                        Valores válidos son casual,formal
                        """,  choices=["casual", "formal"])
    
    parser.add_argument("nombre", help="""
                        Indica el nombre de quien quieres saludar.
                        """)
    
    parser.add_argument("--capitalizar", help="Capitaliza el nombre del usuario",
                    action="store_true")
    argumentos = parser.parse_args()
    return argumentos


def main(argumentos):
    """
    Aquí ponemos la funcionalidad principal de nuestro script
    """
    # Asignar nombre
    nombre = argumentos.nombre
    
    # Si la bandera capitalizar se paso como argumento
    if argumentos.capitalizar:
        nombre = nombre.capitalize()
    
    if argumentos.saludo == "casual": # Si el saludo es casual
        print("Que onda {}".format(nombre))
    elif argumentos.saludo == "formal": # Si el saludo es informal
        print("Buen día {}".format(nombre))
    
if __name__ == "__main__":
    argumentos = parsear_argumentos()
    main(argumentos)