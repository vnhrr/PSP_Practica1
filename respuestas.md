1-PREGUNTA
  La ejecución sincrona es más sencilla de comprender, ya que la ejecución del código es secuencial, todo se completa por un orden predecible.
    A pesar de eso, el aspecto negativo que nos encontramos es la epsera que sufren las tareas, ya que para que comience una, la otra debe de
    acabar.
  La ejecución asincrona es lo contrario, más difícil de comprender en codigo ya que el flujo de ejecución no es tan predecible pero lo compensa
    con una mayor eficiencia y capacidad de respuesta.

2-PREGUNTA
  Trabajar con procesos y hacer uso de excepciones, nos permite dar mas estabilidad al código, pudiendo tener salidas controladas en caso de error.
  También favorecen la liberación de recursos del sistema, evitando que a causa de errores, los ficheros puedan quedar bloqueados para el resto
    de procesos del sistema.
  Facilita entender los errores del código, ya que controlamos los posibles fallos que puedan existir y podemos mandar mensajes de error que 
    describan el problema.

3-PREGUNTA
  Sincronización: cuando diferentes procesos necesitan acceder a un mismo recurso pueden existir errores de lectura del contenido del recurso
    porque otro proceso le haya modificado. Para solucionar esto, podemos hacer uso de bloqueos, para evitar que un proceso pueda acceder al
    recurso mientras otro se encuentra trabajando con ello.
  DeadLock: cuando dos procesos se encuentran esperando por recursos que tiene el otro, lo cual crea un bucle infinito. Se puede solucionar 
    con el uso de tiempos límite en las operaciones.
  Perdida de datos en comunicación: puede existir pérdida de información al comunicar procesos. Para solucionarlo hay que hacer un control
    adecuado de las excepciones que se puedan presentar.
  Acceso al portapapeles: que varios programas hagan un acceso repetido al portapapeles puede generar errores, para ello lo mejor es hacer uso
    de un tiempo de demora en los reintentos del proceso.
