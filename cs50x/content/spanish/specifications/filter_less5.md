Especificación
-------------

Implemente las funciones en `helpers.c` de manera que el usuario pueda aplicar filtros de escala de grises, sepia, reflexión o desenfoque a sus imágenes.

*   La función `grayscale` debe tomar una imagen y convertirla en una versión en blanco y negro de la misma imagen.
*   La función `sepia` debe tomar una imagen y convertirla en una versión sepia de la misma imagen.
*   La función `reflect` debe tomar una imagen y reflejarla horizontalmente.
*   Por último, la función `blur` debe tomar una imagen y convertirla en una versión desenfocada de la misma imagen.

No se deben modificar ninguna de las firmas de las funciones, ni se deben modificar ningún otro archivo que no sea `helpers.c`.

Aplicación
-----

El programa debe comportarse según los siguientes ejemplos. `INFILE.bmp` es el nombre de la imagen de entrada y `OUTFILE.bmp` es el nombre de la imagen resultante después de que se ha aplicado un filtro.

```
$ ./filter -g INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -s INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -r INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -b INFILE.bmp OUTFILE.bmp
```

Pistas
-----

*  Los valores de los componentes `rgbtRed`, `rgbtGreen` y `rgbtBlue` de un píxel son todos enteros, por lo que asegúrese de redondear cualquier número de punto flotante al entero más cercano al asignarlo a un valor de píxel.
*  Al implementar la función `grayscale`, deberá promediar los valores de 3 enteros. ¿Por qué podría querer dividir la suma de estos enteros por 3.0 y no por 3?
*  En la función `reflect`, deberá intercambiar los valores de los píxeles en lados opuestos de una fila. Recuerde de la clase cómo implementamos el intercambio de dos valores con una variable temporal. ¡No hay necesidad de usar una función separada para el intercambio a menos que quiera!
*  ¿Cómo podría serle útil una función que devuelva el menor de dos enteros al implementar `sepia`, particularmente cuando necesita asegurarse de que el valor de un color no sea mayor a 255?
*  Al implementar la función `blur`, puede descubrir que el desenfoque de un píxel termina afectando el desenfoque de otro píxel. ¿Quizás crear una copia de `image` (el tercer argumento de la función) declarando una nueva matriz (bidimensional) con código como `RGBTRIPLE copy[height][width];` y copiar `image` en `copy`, píxel por píxel, con bucles `for` anidados? ¿Y luego leer los colores de los píxeles desde `copy` pero escribir (es decir, cambiar) los colores de los píxeles en `image`?

Pruebas
-------

Asegúrese de probar todos sus filtros en los archivos de mapa de bits de muestra proporcionados.

Ejecute lo siguiente para evaluar la corrección de su código utilizando `check50`. ¡Pero asegúrese de compilarlo y probarlo usted mismo también!

    check50 cs50/problems/2023/x/filter/less
    

Ejecute lo siguiente para evaluar el estilo de su código utilizando `style50`.

    style50 helpers.c
    

Cómo enviar
-------------

En su terminal, ejecute lo siguiente para enviar su trabajo.

    submit50 cs50/problems/2023/x/filter/less"