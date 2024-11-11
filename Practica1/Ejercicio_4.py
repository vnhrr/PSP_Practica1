# Es necesario instalar la librería pywin32 para trabajar con el portapapeles en Windows:
# Ejecuta en la terminal: pip install pywin32
import win32clipboard  # Importamos el módulo win32clipboard para interactuar con el portapapeles de Windows.
import subprocess

p1 = subprocess.Popen('ftp', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p2 = subprocess.Popen('ftp', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
comandos = [b"verbose\n",  # Activa el modo detallado para mostrar más información.
            b"open test.rebex.net\n",  # Abre una conexión FTP al servidor 'test.rebex.net'.
            b"demo\n",  # Usuario de prueba para la autenticación.
            b"password\n",  # Contraseña de prueba para la autenticación.
            b"ls\n",  # Lista los archivos y directorios en el servidor remoto.
            b"get readme.txt\n"]  # Descarga el archivo 'readme.txt' desde el servidor.


def comprobar():
    for cmd in comandos:
        p2.stdin.write(cmd)  # Escribimos el comando en la entrada estándar del proceso.
    respuesta = p2.communicate(timeout=5)[0]
    if (respuesta) != (almacenar()):
        print("Ha cambiado el contenido")
        return False


def almacenar():
    for cmd in comandos:
        p1.stdin.write(cmd)  # Escribimos el comando en la entrada estándar del proceso.

    # Esperamos hasta 5 segundos a que el proceso termine y capturamos la salida.
    # p1.communicate() devuelve una tupla con (salida estándar, salida de error).
    # [0] indica que estamos accediendo a la salida estándar.
    respuesta = p1.communicate(timeout=5)[0]

    # Enviar datos al portapapeles
    win32clipboard.OpenClipboard()  # Abre el portapapeles para manipularlo.
    win32clipboard.EmptyClipboard()  # Limpia el contenido actual del portapapeles.
    win32clipboard.SetClipboardText()  # Establece el texto de la respuesta en el portapapeles.
    win32clipboard.CloseClipboard()  # Cierra el portapapeles para liberar el acceso.

    # Obtener datos del portapapeles
    win32clipboard.OpenClipboard()  # Abre nuevamente el portapapeles para leer su contenido.
    datos = win32clipboard.GetClipboardData()  # Obtiene los datos actuales del portapapeles (en este caso, el texto).
    win32clipboard.CloseClipboard()  # Cierra el portapapeles para liberar el acceso.
    # Imprimir el contenido obtenido del portapapeles
    return datos


print(str(almacenar()))
while (True):
    comprobar()
