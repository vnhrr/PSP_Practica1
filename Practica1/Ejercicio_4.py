# Es necesario instalar la librería pywin32 para trabajar con el portapapeles en Windows:
# Ejecuta en la terminal: pip install pywin32
import time
import win32clipboard  # Importamos el módulo win32clipboard para interactuar con el portapapeles de Windows.
import subprocess


# Funcion para descargar el archivo. Dentro de ella hacemos llamada a las funciones almacenarPortapapeles() y
# a leerArchivo() con el fin de leer el archivo descargado y almacenar su contenido en el portapapeles.
def descargar():
    p1 = subprocess.Popen('ftp', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p2 = subprocess.Popen('ftp', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    comandos = [b"verbose\n",  # Activa el modo detallado para mostrar más información.
                b"open test.rebex.net\n",  # Abre una conexión FTP al servidor 'test.rebex.net'.
                b"demo\n",  # Usuario de prueba para la autenticación.
                b"password\n",  # Contraseña de prueba para la autenticación.
                b"ls\n",  # Lista los archivos y directorios en el servidor remoto.
                b"get readme.txt\n"]  # Descarga el archivo 'readme.txt' desde el servidor.
    for cmd in comandos:
        p2.stdin.write(cmd)  # Escribimos el comando en la entrada estándar del proceso.
    respuesta = p2.communicate(timeout=5)[0]
    almacenarPortapapeles(leerArchivo())

# Funcion que retorna el contenido de un fichero.
def leerArchivo():
    with open("readme.txt", "r") as txtFile:
        txt = txtFile.read()
    return txt

# Funcion a la que pasamos un parametro de contenido el cual sera almacenado en el portapapeles.
def almacenarPortapapeles(txt):
    # Enviar datos al portapapeles
    win32clipboard.OpenClipboard()  # Abre el portapapeles para manipularlo.
    win32clipboard.EmptyClipboard()  # Limpia el contenido actual del portapapeles.
    win32clipboard.SetClipboardText(txt)  # Establece el texto de la respuesta en el portapapeles.
    win32clipboard.CloseClipboard()  # Cierra el portapapeles para liberar el acceso.

# Funcion para obtener lo que se encuentra en el portapapeles
def datosPortapapeles():
    # Obtener datos del portapapeles
    win32clipboard.OpenClipboard()  # Abre nuevamente el portapapeles para leer su contenido.
    datos = win32clipboard.GetClipboardData()  # Obtiene los datos actuales del portapapeles (en este caso, el texto).
    win32clipboard.CloseClipboard()  # Cierra el portapapeles para liberar el acceso.
    # Imprimir el contenido obtenido del portapapeles
    return datos

# Recive como parametro el contenido del portapapeles y lo compara con el contenido del fichero que hemos
# elegido copiar previamente en el portapapeles para mostrar si existe cambio en el contenido de este ultimo.
def comprobar(portapapeles):
    if (datosPortapapeles()) != (leerArchivo()):
        print("Ha cambiado el contenido")
        return False
    return True

# Variable que almacena el contenido original del fichero.
contenidoInicial = leerArchivo()
# Almacenamos el contenido original en el portapapeles
almacenarPortapapeles(contenidoInicial)
# Bucle infinito que comprobara continuamente si el contenido del portapapeles es igual que el del fichero elegido
# cada 2 segundos.
while (True):
    if not comprobar(contenidoInicial):
        print("El contenido del portapales es diferente al del archivo")
    time.sleep(2)

