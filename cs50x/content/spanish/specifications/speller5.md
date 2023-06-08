Sugerencias
-------

Para comparar dos cadenas de caracteres sin distinguir entre mayúsculas y minúsculas, ¡puede ser útil utilizar [`strcasecmp`](https://man.cs50.io/3/strcasecmp) (declarada en `strings.h`)! También es probable que desee asegurarse de que su función hash no distingue entre mayúsculas y minúsculas, de modo que `foo` y `FOO` tengan el mismo valor hash.

¡Asegúrate de liberar toda la memoria que hayas asignado en `load` en `unload` usando `free`! Recuerda que `valgrind` es tu mejor amigo. Ten en cuenta que `valgrind` supervisa las fugas mientras tu programa se está ejecutando, por lo que asegúrate de proporcionar argumentos de línea de comandos si deseas que `valgrind` analice `speller` mientras usa un diccionario y/o texto específico, como en el siguiente ejemplo. Es mejor utilizar un texto pequeño, de lo contrario `valgrind` podría tardar bastante tiempo en ejecutarse.

    valgrind ./speller texts/cat.txt
    

Si ejecutas `valgrind` sin especificar un `texto` para `speller`, tus implementaciones de `load` y `unload` no se ejecutarán (y, por lo tanto, no serán analizadas).

Si no estás seguro de cómo interpretar la salida de `valgrind`, simplemente pídele ayuda a `help50`:

    help50 valgrind ./speller texts/cat.txt
    

Pruebas
-------

¿Cómo puedes comprobar si tu programa está detectando las palabras mal escritas correctas? Puedes consultar las soluciones propuestas que se encuentran dentro del directorio `keys` que está dentro de tu directorio `speller`. Por ejemplo, dentro de `keys/lalaland.txt` se encuentran todas las palabras que tu programa _debería_ considerar como mal escritas.

Por lo tanto, podrías ejecutar tu programa en algún texto en una ventana, como se muestra a continuación.

    ./speller texts/lalaland.txt
    

Y podrías ejecutar la solución del equipo docente en el mismo texto en otra ventana, como se muestra a continuación.

    ./speller50 texts/lalaland.txt
    

Y podrías comparar las ventanas visualmente lado a lado. Eso podría volverse tedioso rápidamente. Por lo tanto, podrías querer "redirigir" la salida de tu programa a un archivo, como se muestra a continuación.

    ./speller texts/lalaland.txt > student.txt
    ./speller50 texts/lalaland.txt > staff.txt
    

Luego puedes comparar ambos archivos lado a lado en la misma ventana con un programa como `diff`, como se muestra a continuación.

    diff -y student.txt staff.txt
    

Alternativamente, para ahorrar tiempo, podrías simplemente comparar la salida de tu programa (asumiendo que la redirigiste, por ejemplo, a `student.txt`) con una de las soluciones que se encuentran en `keys` sin ejecutar la solución del equipo docente, como se muestra a continuación.

    diff -y student.txt keys/lalaland.txt
    

Si la salida de tu programa coincide con la del equipo docente, `diff` mostrará dos columnas que deberían ser idénticas, excepto, tal vez, los tiempos de ejecución en la parte inferior. Sin embargo, si las columnas son diferentes, verás un `>` o `|` donde difieren. Por ejemplo, si ves

    MISSPELLED WORDS                                                MISSPELLED WORDS
    
    TECHNO                                                          TECHNO
    L                                                               L
                                                                  > Thelonious
    Prius                                                           Prius
                                                                  > MIA
    L                                                               L
    

eso significa que tu programa (cuya salida está a la izquierda) no considera que `Thelonious` o `MIA` están mal escritas, aunque la salida del equipo docente (a la derecha) sí lo hace, como se deduce de la ausencia, por ejemplo, de `Thelonious` en la columna izquierda y de la presencia de `Thelonious` en la columna derecha.

### `check50`

Para probar tu código de manera menos manual (aunque no exhaustiva), también puedes ejecutar lo siguiente.

    check50 cs50/problems/2023/x/speller
    

Ten en cuenta que `check50` también verificará la existencia de fugas de memoria, así que asegúrate de haber ejecutado `valgrind`.

### style50

Ejecuta lo siguiente para evaluar el estilo de tu código usando `style50`.

    style50 dictionary.c
    

Solución del equipo docente
--------------------------

¿Cómo puedes evaluar qué tan rápida (y correcta) es tu código? Bueno, como siempre, siéntete libre de jugar con la solución del equipo docente, como se muestra a continuación, y comparar sus números con los tuyos.

    ./speller50 texts/lalaland.txt
    

Cómo enviarlo
-------------

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2023/x/speller"