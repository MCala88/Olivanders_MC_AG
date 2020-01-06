def barricada_gilded_rose(elementos, rutaArchivo):
    
    try:
        if not isinstance(rutaArchivo, str):
            raise ValueError
        fichero = open(rutaArchivo, 'r')
    except FileNotFoundError:
        print("Fichero no encontrado")
        return []
    except ValueError:
        print("El nombre del fichero ha de ser un string")
        return []
    else:
        elementos = []
        for linea in fichero:
            if linea.find("day") != -1:
                casosTestDia = []
            elif linea == "\n":
                elementos.append(casosTestDia)
            elif linea.find("name") != -1:
                numeroPropiedadesItem = len(linea.split(','))
            else:
                item = linea.rstrip().rsplit(',', maxsplit=numeroPropiedadesItem-1)
                casosTestDia.append(item)
        fichero.close()
        return elementos

def mostrarCasosTest(matrizCasosTest):
    """
    Muestra en consola los casos test cargados en memoria
    """
    for (offset, casosTestDia) in enumerate(matrizCasosTest):
        print('-' * 5 + " Dia %d: " % offset + '-' * 5)
        for item in casosTestDia:
            print(item)

if __name__ == "__main__":

    rutaArchivo = "./stdout.txt"

    elementos = []

    elementos = barricada_gilded_rose(elementos, rutaArchivo)

    mostrarCasosTest(elementos)



  

   