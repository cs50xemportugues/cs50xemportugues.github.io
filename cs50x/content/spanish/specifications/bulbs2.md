Detalles de Implementación
--------------------------

Para escribir nuestro programa, primero tenemos que pensar en las **bases**.

### Los fundamentos

La base más simple es la base-1 o _unaria_; para escribir un número, _N_, en base-1, simplemente escribimos _N_ cantidad de `1`s consecutivas. Por lo tanto, el número `4` en base-1 se escribiría como `1111`, y el número `12` como`111111111111`. Piensa en ello como contar en tus dedos o marcar un puntaje con marcas en una pizarra.

Puede entender por qué la base-1 no se usa mucho en la actualidad. (¡Los números se vuelven bastante largos!) En su lugar, una convención común es la base-10 o _decimal_. En base-10, cada _dígito_ se multiplica por alguna potencia de 10, para representar números más grandes. Por ejemplo, `123` es una forma corta de escribir <code>123 = 1 • 10<sup>2</sup> + 2 • 10<sup>1</sup> + 3 • 10<sup>0</sup></code>.

Cambiar de base es tan simple como cambiar el `10` de arriba por un número diferente. Por ejemplo, si escribieras `123` en base-4, el número que realmente estarías escribiendo es <code>123 = 1 • 4<sup>2</sup> + 2 • 4<sup>1</sup> + 3 • 4<sup>0</sup></code>, que es igual al número decimal `27`.

Los ordenadores, por otro lado, usan la base-2 o _binario_. En binario, escribir `123` sería un error, ya que los números binarios solo pueden tener `0`s y `1`s. Pero el proceso de descubrir exactamente qué número decimal representa un número binario es exactamente el mismo. Por ejemplo, el número `10101` en base-2 representa <code>1 • 2<sup>4</sup> + 0 • 2<sup>3</sup> + 1 • 2<sup>2</sup> + 0 • 2<sup>1</sup> + 1 • 2<sup>0</sup></code>, que es igual al número decimal `21`.

### Codificando un Mensaje

Las bombillas solo pueden estar encendidas o apagadas. En otras palabras, las bombillas representan dos estados posibles; o la bombilla está encendida, o la bombilla está apagada, así como los números binarios son 1 o 0. Tendremos que encontrar una forma de codificar texto como una secuencia de números binarios.

Escribamos un programa llamado `bulbs` que tome un mensaje y lo convierta en un conjunto de bombillas que podríamos mostrar a una audiencia desprevenida. Lo haremos en dos pasos:

*   El primer paso consiste en convertir el texto en números decimales. Digamos que queremos codificar el mensaje `HI!`. Por suerte, ya tenemos una convención en su lugar sobre cómo hacer esto, [ASCII](https://asciichart.com/). Observe que `H` se representa por el número decimal `72`, `I` por `73` y `!` por `33`.
*   El siguiente paso implica tomar nuestros números decimales (como `72`, `73` y `33`) y convertirlos en números binarios equivalentes que solo usan 0s y 1s. Para tener una cantidad consistente de bits en cada uno de nuestros números binarios, asumamos que cada número decimal se representa con 8 bits. `72` es `01001000`, `73` es `01001001` y `33` es `00100001`.

Por último, interpretaremos estos números binarios como instrucciones para las bombillas en el escenario; 0 está apagado, 1 está encendido. (En el archivo `bulbs.c` se incluye una función `print_bulb` que se ha implementado para ti, que toma un `0` o `1` y emite un emoji que representa bombillas.)

Aquí hay un ejemplo de cómo podría funcionar el programa completo. A diferencia del escenario de Sanders, imprimiremos un byte por línea para mayor claridad.

    # ./bulbs
    Mensaje: HI!
    ⚫🟡⚫⚫🟡⚫⚫⚫
    ⚫🟡⚫⚫🟡⚫⚫🟡
    ⚫⚫🟡⚫⚫⚫⚫🟡
    

Para verificar nuestro trabajo, podemos leer una bombilla que está encendida (🟡) como un `1` y una bombilla que está apagada (⚫) como un `0`. Entonces `HI!` se convirtió en

    01001000
    01001001
    00100001
    

que es precisamente lo que esperaríamos.

Otro ejemplo:

    # ./bulbs
    Mensaje: HI MOM
    ⚫🟡⚫⚫🟡⚫⚫⚫
    ⚫🟡⚫⚫🟡⚫⚫🟡
    ⚫⚫🟡⚫⚫⚫⚫⚫
    ⚫🟡⚫⚫🟡🟡⚫🟡
    ⚫🟡⚫⚫🟡🟡🟡🟡
    ⚫🟡⚫⚫🟡🟡⚫🟡
    

Observe que se incluyen todos los caracteres en las instrucciones de las bombillas, incluidos los caracteres no alfabéticos como los espacios (`00100000`).