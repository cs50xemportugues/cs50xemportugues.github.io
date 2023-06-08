Detalles de Implementación
----------------------

Completa la implementación de `tournament.py`, de modo que simule una serie de torneos y muestre la probabilidad de ganar de cada equipo.

En primer lugar, en la función `main`, lee los datos del equipo desde un archivo CSV en la memoria del programa, y agrega cada equipo a la lista `teams`.

*   El archivo a utilizar se proporcionará como argumento de línea de comandos. Puedes acceder al nombre del archivo con `sys.argv[1]`.
*   Recuerda que puedes abrir un archivo con `open(filename)`, donde `filename` es una variable que almacena el nombre del archivo.
*   Una vez que tienes un archivo `f`, puedes usar `csv.DictReader(f)` para darle un "lector": un objeto en Python que puedes recorrer para leer el archivo una fila a la vez, tratando cada fila como un diccionario.
*   De forma predeterminada, todos los valores leídos desde el archivo serán cadenas. Asegúrate de convertir primero la `calificación` del equipo a un `int` (puedes usar la función `int` en Python para hacer esto).
*   En última instancia, agrega el diccionario de cada equipo a `teams`. La llamada a la función `teams.append(x)` agregará `x` a la lista `teams`.
*   Recuerda que cada equipo debe ser un diccionario con el nombre del `equipo` y una `calificación`.

A continuación, implementa la función `simulate_tournament`. Esta función debe aceptar como entrada una lista de equipos y simular repetidamente rondas hasta que te quede un equipo. La función debe devolver el nombre de ese equipo.

*   Puedes llamar a la función `simulate_round`, que simula una única ronda, aceptando una lista de equipos como entrada y devolviendo una lista de todos los ganadores.
*   Recuerda que si `x` es una lista, puedes usar `len(x)` para determinar la longitud de la lista.
*   No debes suponer el número de equipos en el torneo, pero puedes asumir que será una potencia de 2.

Finalmente, en la función `main`, ejecuta `N` simulaciones de torneos y realiza un seguimiento de cuántas veces gana cada equipo en el diccionario `counts`.

*   Por ejemplo, si Uruguay gana 2 torneos y Portugal gana 3 torneos, entonces el diccionario `counts` debería ser `{"Uruguay": 2, "Portugal": 3}`.
*   Debes usar tu función `simulate_tournament` para simular cada torneo y determinar al ganador.
*   Recuerda que si `counts` es un diccionario, la sintaxis como `counts[nombre_equipo] = x` asociará la clave almacenada en `nombre_equipo` con el valor almacenado en `x`.
*   Puedes usar la palabra clave `in` en Python para comprobar si un diccionario ya tiene una clave en particular. Por ejemplo, `if "Portugal" in counts:` comprobará si `"Portugal"` ya tiene un valor existente en el diccionario `counts`.