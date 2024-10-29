from _winapi import TerminateProcess

import psutil

print("Que proceso desea terminar? Introduzca su PID")
pid = input()

try :
    for proce in psutil.process_iter(["pid"]):
        if proce.pid == int (pid):
            proce.terminate()


except psutil.NoSuchProcess as e:
    print("No existe el proceso con ese PID")
except psutil.AccessDenied as e:
    print("No cuenta con permisos para realizar esa accion en ese proceso")

