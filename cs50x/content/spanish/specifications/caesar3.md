## Especificación

Diseña e implementa un programa, `caesar`, que cifre mensajes usando el cifrado de César.

- Implementa tu programa en un archivo llamado `caesar.c` dentro de un directorio llamado `caesar`.
- Tu programa debe aceptar un solo argumento de línea de comandos, un número entero no negativo. Llamémosle `k` por conveniencia.
- Si tu programa se ejecuta sin argumentos de línea de comandos o con más de un argumento de línea de comandos, tu programa debe imprimir un mensaje de error de tu elección (con `printf`) y salir de `main` devolviendo un valor de `1` (que indica un error) inmediatamente.
- Si alguno de los caracteres del argumento de línea de comandos no es un dígito decimal, tu programa debe imprimir el mensaje `Uso: ./caesar key` y salir de `main` devolviendo un valor de `1`.
- No asumas que `k` será menor o igual que 26. Tu programa debe funcionar para todos los valores enteros no negativos de `k` menores que <code>2<sup>31</sup> - 26</code>. En otras palabras, no es necesario que te preocupes si tu programa eventualmente falla si el usuario elige un valor para `k` que sea demasiado grande o casi demasiado grande para caber en un `int`. (Recuerda que un `int` puede desbordarse.) Pero incluso si `k` es mayor que `26`, los caracteres alfabéticos de la entrada de tu programa deben seguir siendo caracteres alfabéticos en la salida de tu programa. Por ejemplo, si `k` es `27`, `A` no debe convertirse en `\` aunque `\` esté a `27` posiciones de `A` en ASCII, según [asciitable.com](https://www.asciitable.com/); `A` debe convertirse en `B`, ya que `B` está a `27` posiciones de `A`, siempre y cuando se haga la vuelta a `Z` a `A`.
- Tu programa debe imprimir `plaintext:` (con dos espacios pero sin un salto de línea) y luego solicitar al usuario una `cadena` de texto sin formato (utilizando `get_string`).
- Tu programa debe imprimir `ciphertext:` (con un espacio pero sin un salto de línea) seguido del cifrado correspondiente de la cadena sin formato, con cada carácter alfabético de la cadena sin formato "rotado" por _k_ posiciones; los caracteres no alfabéticos deben imprimirse sin cambios.
- Tu programa debe preservar el uso del mayúsculas: las letras mayúsculas, aunque rotadas, deben seguir siendo letras mayúsculas; las letras minúsculas, aunque rotadas, deben seguir siendo letras minúsculas.
- Después de imprimir el cifrado, debes imprimir un salto de línea. Tu programa debe salir devolviendo `0` de `main`.

## Consejos

¿Cómo empezar? Abordemos este problema paso a paso.

### Pseudocódigo

Primero, intenta escribir una función `main` en `caesar.c` que implemente el programa utilizando solo pseudocódigo, incluso si no estás (¡todavía!) seguro de cómo escribirlo en código real.

<details><summary>Pista</summary><p>Hay más de una manera de hacer esto, aquí hay solo una!</p>

    int main(void)
    {
        // Asegúrate de que el programa se haya ejecutado con un solo argumento de línea de comandos

        // Asegúrate de que cada carácter en argv[1] sea un dígito

        // Convierte argv[1] de una `cadena` a un `int`

        // Solicita al usuario el texto en claro

        // Para cada carácter en el texto plano:

            // Rota el carácter si es una letra
    }

<p>Está bien editar tu propio pseudocódigo después de ver el nuestro aquí, ¡pero no copies y pegues el nuestro en el tuyo!</p></details>