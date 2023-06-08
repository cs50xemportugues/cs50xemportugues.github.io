Uso
---

A continuación se presentan algunos ejemplos de cómo debería funcionar el programa. Por ejemplo, si el usuario omite uno de los argumentos de la línea de comandos:

    $ ./reverse input.wav
    Uso: ./reverse input.wav output.wav
    

O si el usuario omite ambos argumentos de la línea de comandos:

    $ ./reverse
    Uso: ./reverse input.wav output.wav
    

Así es como debería funcionar el programa si el usuario proporciona un archivo de entrada que no es un archivo WAV real:

    $ ./reverse image.jpg output.wav
    El archivo de entrada no es un archivo WAV.
    

Se asume que el usuario ingresa un nombre de archivo de salida válido, como `output.wav`.

Un programa ejecutado con éxito no debe producir texto y debe crear un archivo WAV con el nombre especificado por el usuario que reproduzca el audio del archivo WAV de entrada al revés. Por ejemplo:

    $ ./reverse input.wav output.wav
    

Pruebas
-------

Ejecute lo siguiente para evaluar la corrección de su código usando `check50`. ¡Pero asegúrese de compilar y probarlo usted mismo también!

    check50 cs50/problems/2023/x/reverse
    

Ejecute lo siguiente para evaluar el estilo de su código usando `style50`.

    style50 reverse.c
    

Cómo enviar
-----------

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2023/x/reverse