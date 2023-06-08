# Crédito

## Empezando

Abre [VS Code](https://code.cs50.io/).

Comienza haciendo clic dentro de la ventana de tu terminal, luego escribe `cd` por sí solo. Deberías encontrarte con que su "prompt" se parece al siguiente.

```
$
```

Haz clic dentro de esa ventana de terminal y luego escribe

```
wget https://cdn.cs50.net/2022/fall/psets/1/credit.zip
```

seguido de "Enter" para descargar un archivo ZIP llamado "credit.zip" en tu espacio de códigos. ¡Ten cuidado de no dejar pasar el espacio entre `wget` y la URL siguiente, o cualquier otro carácter por ese caso!

Ahora escribe

```
unzip credit.zip
```

para crear una carpeta llamada `credit`. Ya no necesitas el archivo ZIP, así que escribe

```
rm credit.zip
```

y responde con "y", seguido de "Enter" en el prompt para eliminar el archivo ZIP que descargaste.

Escribe ahora:

```
cd credit
```

seguido de "Enter" para moverte dentro (es decir, abrir) ese directorio. Ahora, tu prompt debe parecerse al siguiente.

```
credit/ $
```

Si todo fue exitoso, debes escribir

```
ls
```

y ver un archivo llamado `credit.c`. Al ejecutar `code credit.c`, se abre el archivo donde escribirás el código para este conjunto de problemas. Si no, retrocede tus pasos y ve si puedes determinar dónde te equivocaste.

## Tarjetas de crédito

Una tarjeta de crédito (o débito), por supuesto, es una tarjeta de plástico con la que puedes pagar bienes y servicios. Impreso en esa tarjeta hay un número que también se almacena en una base de datos en algún lugar, para que cuando alguien utilice tu tarjeta para comprar algo, el acreedor sepa a quién facturar. Hay muchas personas con tarjetas de crédito en este mundo, por lo que esos números son bastante largos: American Express utiliza números de 15 dígitos, MasterCard utiliza números de 16 dígitos; y Visa, números de 13 y 16 dígitos. Y esos son números decimales (de 0 a 9), no binarios, lo que significa, por ejemplo, que American Express podría imprimir hasta 10^15 = 1,000,000,000,000,000 tarjetas únicas! (Eso es, eh, un cuatrillón).

De hecho, eso es un poco exagerado, porque los números de las tarjetas de crédito tienen cierta estructura. Todos los números de American Express comienzan con 34 o 37; la mayoría de los números de MasterCard comienzan con 51, 52, 53, 54 o 55 (también tienen algunos otros números de inicio potenciales con los que no nos preocuparemos por este problema); y todos los números de Visa comienzan con 4. Pero los números de las tarjetas de crédito también tienen una "suma de verificación" incorporada en ellos, una relación matemática entre al menos un número y otros. Esa suma de verificación permite que las computadoras (o las personas que aman las matemáticas) detecten errores tipográficos (por ejemplo, transposiciones), si no números fraudulentos, sin tener que consultar una base de datos, lo que puede ser lento. Por supuesto, un matemático deshonesto podría ciertamente crear un número falso que, no obstante, respete la restricción matemática, por lo que todavía es necesario una consulta de base de datos para controles más rigurosos.

## Algoritmo de Luhn

Entonces, ¿cuál es la fórmula secreta? Bueno, la mayoría de las tarjetas utilizan un algoritmo inventado por Hans Peter Luhn de IBM. Según el algoritmo de Luhn, puedes determinar si un número de tarjeta de crédito es (sintácticamente) válido de la siguiente manera:

1. Multiplica por 2 cada otro dígito, empezando por el segundo a último dígito del número; luego, suma juntos los dígitos de esos productos.
2. Agrega la suma total a la suma de los dígitos que no se multiplicaron por 2.
3. Si el último dígito del total es 0 (o, expresado más formalmente, si el total módulo 10 es congruente a 0), ¡el número es válido!

Es un poco confuso, así que intentemos un ejemplo con la Visa de David: 4003600000000014.

1. Para efectos de discusión, subrayemos cada otro dígito, empezando por el segundo a último dígito del número:

    <p><u>4</u>0<u>0</u>3<u>6</u>0<u>0</u>0<u>0</u>0<u>0</u>0<u>0</u>0<u>1</u>4</p>

    Listo, multipliquemos cada uno de los dígitos subrayados por 2:

    1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2

    Eso nos da:

    2 + 0 + 0 + 0 + 0 + 12 + 0 + 8

    Ahora, agreguemos juntos los dígitos de esos productos (es decir, no los productos en sí):

    2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13

2. Ahora, agreguemos esa suma (13) a la suma de los dígitos que no se multiplicaron por 2 (a partir de la cuenta regresiva):

    13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20

3. Sí, el último dígito en esa suma (20) es 0, ¡así que la tarjeta de David es legítima!

Entonces, validar los números de tarjetas de crédito no es difícil, pero sí es un poco tedioso hacerlo a mano. ¡Escribamos un programa!

## Detalles de la implementación

En el archivo llamado `credit.c` en el directorio `credit`, escribe un programa que solicite al usuario un número de tarjeta de crédito y luego informe (a través de `printf`) si es un número de tarjeta American Express, MasterCard o Visa válido, según las definiciones de cada formato aquí. Para que podamos automatizar algunas pruebas de tu código, pedimos que la última línea de salida de tu programa sea `AMEX\n` o `MASTERCARD\n` o `VISA\n` o `INVALID\n`, nada más, nada menos. Para simplificar, puedes asumir que la entrada del usuario será totalmente numérica (es decir, sin guiones, como podría imprimirse en una tarjeta real) y que no tendrá ceros a la izquierda. Pero no asumas que la entrada del usuario cabrá en un `int`! Lo mejor es usar `get_long` de la biblioteca de CS50 para obtener la entrada del usuario. (¿Por qué?)

Considera que lo siguiente es representativo de cómo debe comportarse tu propio programa cuando se le entrega un número de tarjeta de crédito válido (sin guiones).

```
$ ./credit
Number: 4003600000000014
VISA
```

Ahora, `get_long` en sí mismo rechazará los guiones (y más) de todos modos:

```
$ ./credit
Number: 4003-6000-0000-0014
Number: foo
Number: 4003600000000014
VISA
```

Pero depende de ti atrapar las entradas que no sean números de tarjetas de crédito (por ejemplo, un número de teléfono), incluso si son numéricas:

```
$ ./credit
Number: 6176292929
INVALID
```

Prueba tu programa con un montón de entradas, tanto válidas como inválidas. (¡Ciertamente nosotros lo haremos!) Aquí están algunos [números de tarjeta](https://developer.paypal.com/api/nvp-soap/payflow/integration-guide/test-transactions/#standard-test-cards) que PayPal recomienda para pruebas.

Si el programa se comporta de manera incorrecta con algunas entradas (o no se puede compilar en absoluto), es hora de depurar.

### Pasos

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/dF7wNjsRBjI?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

### Cómo probar tu código

También puedes ejecutar lo siguiente para evaluar la corrección de tu código con `check50`. ¡Pero asegúrate de compilar y probarlo por ti mismo también!

```
check50 cs50/problems/2023/x/credit
```

Para evaluar el estilo de tu código usando `style50`, ejecuta lo siguiente.

```
style50 credit.c
```

## Cómo enviar tu trabajo

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

```
submit50 cs50/problems/2023/x/credit
```