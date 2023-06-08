Laboratorio 3: Ordenamiento
===========


<div class="alert" data-alert="warning" role="alert"><p>Puedes colaborar con uno o dos compañeros en este laboratorio, aunque se espera que cada estudiante de cualquier grupo contribuya de manera equitativa al laboratorio.</p></div>

Analiza tres programas de ordenamiento para determinar qué algoritmos usan.

Antecedentes
----------

Recuerda en la clase que vimos algunos algoritmos para ordenar una secuencia de números: ordenación por selección, ordenación de burbuja (o burbujeo) y ordenación por mezcla.

* La ordenación por selección itera a través de las partes no ordenadas de una lista, seleccionando el elemento más pequeño cada vez y moviéndolo a su ubicación correcta.
* La ordenación de burbuja compara pares de valores adyacentes uno a la vez e intercambia su lugar si están en el orden incorrecto. Esto continúa hasta que la lista está ordenada.
* La ordenación por mezcla divide recursivamente la lista en dos unidades más pequeñas y luego fusiona las listas más pequeñas en una más grande en el orden correcto.

Empezando
---------------

Abre [VS Code](https://code.cs50.io/).

Comienza haciendo clic dentro de la ventana de tu terminal y luego ejecuta `cd` por sí solo. Deberías encontrar que su "prompt" se parece al que se muestra a continuación:

    $
    

Haz clic dentro de esa ventana de la terminal y luego ejecuta

    wget https://cdn.cs50.net/2022/fall/labs/3/sort.zip
    

seguido de Enter para descargar un archivo ZIP llamado `sort.zip` en tu espacio de códigos. ¡Ten cuidado de no pasar por alto el espacio entre `wget` y la URL siguiente, o cualquier otro carácter por esa materia!

Ahora ejecuta

    unzip sort.zip
    

para crear una carpeta llamada `sort`. Ya no necesitas el archivo ZIP, así que ejecuta

    rm sort.zip
    

y responde con "y" seguido de Enter en el indicador para eliminar el archivo ZIP que descargaste.

Luego escribe

    cd sort
    

seguido de Enter para moverte al interior de (es decir, abrir) ese directorio. Su indicador ahora debería parecerse al siguiente.

    sort/ $
    

Si todo fue exitoso, deberías ejecutar

    ls
    

y deberías ver una colección de archivos `.txt` junto con los programas ejecutables `sort1`, `sort2` y `sort3`.

Si tienes algún problema, ¡sigue estos mismos pasos nuevamente y ve si puedes determinar dónde te equivocaste!

Instrucciones
------------

Se proporcionan tres programas C ya compilados, `sort1`, `sort2` y `sort3`. Cada uno de estos programas implementa un algoritmo de ordenación diferente: ordenamiento por selección, ordenación de burbuja (burbujeo) o ordenación por fusión (aunque no necesariamente en ese orden). Tu tarea es determinar qué algoritmo de ordenamiento es utilizado por cada archivo.

* 
  Los archivos binarios `sort1`, `sort2` y `sort3` no son archivos legibles para los humanos, por lo que no podrás ver el código fuente C de cada uno. Para evaluar qué tipo de ordenamiento aplica cada uno, ejecuta los programas de ordenamientos con diferentes listas de valores.
* Se te proporcionan varios archivos `.txt`. Estos archivos contienen `n` líneas de valores, ya sea invertidos, desordenados o en orden.

    * Por ejemplo, `reversed10000.txt` contiene 10 000 líneas de números que están invertidos desde `10000`, mientras que `random10000.txt` contiene 10 000 líneas de números que están en orden aleatorio.
* Para ejecutar los programas de ordenamiento en los archivos de texto, en la terminal, ejecuta `./[programa] [archivo_texto.txt]`. ¡Asegúrate de haber hecho uso de `cd` para moverte al directorio `sort`!

    * Por ejemplo, para ordenar `reversed10000.txt` con el programa `sort1`, ejecuta `./sort1 reversed10000.txt`.
* Te podría resultar útil cronometrar tus ordenamientos. Para hacerlo, ejecuta `time ./[nombre_de_programa] [archivo_texto.txt]`.
    * Por ejemplo, podrías ejecutar `time ./sort1 reversed10000.txt` para ejecutar `sort1` en 10 000 números inversos. Al final de la salida de su terminal, puedes ver el tiempo `real` para ver cuánto tiempo transcurrió mientras se ejecutaba el programa.
* Registra tus respuestas en `answers.txt`, junto con una explicación de cada programa, completando los espacios en blanco marcados `TODO`.

### Tutorial


<div class="alert" data-alert="primary" role="alert"> <p> ¡Este video fue grabado cuando el curso todavía estaba utilizando CS50 IDE para escribir código. Aunque la interfaz puede verse diferente a su espacio de código, el comportamiento de los dos entornos debe ser muy similar! </p></div> 

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video ="" src="https://video.cs50.io/-Bhxxw6JKKY"></iframe>


### Consejos

* Los diferentes tipos de archivos `.txt` pueden ayudarte a determinar cuál ordenamiento es cuál. Considera cómo cada algoritmo se comporta con una lista ya ordenada. ¿Qué tal una lista invertida? ¿O una lista desordenada? Te puede ayudar a trabajar a través de una lista más corta de cada tipo y seguir todo el proceso de ordenamiento.

<details><summary> ¿No estás seguro de cómo resolverlo? </summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/uOYhrBs37j0"></iframe></details>


### Cómo verificar tus respuestas

Ejecuta lo siguiente para evaluar la corrección de tus respuestas utilizando `check50`. ¡Pero asegúrate de completar tus explicaciones también, que `check50` no revisará aquí!

    check50 cs50/labs/2023/x/sort
    

Cómo presentar
-------------

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/labs/2023/x/sort