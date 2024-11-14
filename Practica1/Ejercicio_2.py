import os  # Importamos el módulo os para poder usar funciones del sistema operativo, como pipe y fork.
import sys  # Importamos sys para manejar la salida estándar.
import time  # Importamos time para poder pausar la ejecución (opcional).

#Ejecutar en https://www.online-python.com/


def main():
    # Creamos un par de descriptores de archivo utilizando os.pipe().
    # fd[0] se usará para leer, y fd[1] se usará para escribir.
    fd = os.pipe()

    # Creamos el mensaje que el padre enviará al hijo.
    saludoPadre = "Buenos días hijo.\n"

    # Creamos un nuevo proceso con fork().
    pid = os.fork()

    # Verificamos en qué proceso estamos (padre o hijo) según el valor de pid.
    if pid < 0:
        # Si el valor de pid es menor que 0, significa que hubo un error al crear el proceso.
        print("No se ha podido crear el proceso hijo...")
        sys.exit(1)  # Salimos del programa con un código de error.

    elif pid == 0:
        # Leemos el mensaje del pipe. Especificamos un tamaño máximo de lectura.
        # Si en la pipe no ha escrito nadie el proceso de lectura se bloquea
        buffer = os.read(fd[0], 80).decode("utf-8")  # Decodificamos los bytes en una cadena de texto.
        # Cerramos el descriptor de lectura.
        os.close(fd[0])
        buffer = buffer.upper()

        os.write(fd[1], buffer.encode("utf-8"))
        os.close(fd[1])

    else:
        # Escribimos el mensaje en el pipe. Codificamos la cadena a bytes.
        os.write(fd[1], saludoPadre.encode("utf-8"))
        print("El padre envía un mensaje al hijo...")

        # Cerramos el descriptor de escritura.
        os.close(fd[1])

        # Esperamos a que el proceso hijo termine.
        os.wait()

        saludoPadreMod = os.read(fd[0], 80).decode("utf-8")  # Decodificamos los bytes en una cadena de texto.
        print(saludoPadreMod)

# Ejecutamos la función principal.
if __name__ == "__main__":
    main()
