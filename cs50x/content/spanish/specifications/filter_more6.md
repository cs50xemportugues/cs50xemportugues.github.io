Uso
---

Su programa debería comportarse según los ejemplos a continuación. `INFILE.bmp` es el nombre de la imagen de entrada y `OUTFILE.bmp` es el nombre de la imagen resultante después de que se haya aplicado un filtro.

```
$ ./filter -g INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -r INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -b INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -e INFILE.bmp OUTFILE.bmp
```

Sugerencias
-----------

*   Los valores de los componentes `rgbtRed`, `rgbtGreen` y `rgbtBlue` de un píxel son todos números enteros, así que asegúrese de redondear cualquier número de punto flotante al entero más cercano al asignarlos a un valor de píxel.

Pruebas
-------

¡Asegúrese de probar todos sus filtros en los archivos de mapa de bits de muestra proporcionados!

Ejecute lo siguiente para evaluar la corrección de su código utilizando `check50`. Pero asegúrese de compilarlo y probarlo usted mismo también.

    check50 cs50/problems/2023/x/filter/more
    

Ejecute lo siguiente para evaluar el estilo de su código utilizando `style50`.

    style50 helpers.c
    

Cómo enviar
-----------

En su terminal, ejecute lo siguiente para enviar su trabajo.

    submit50 cs50 / problems / 2023 / x / filter / more