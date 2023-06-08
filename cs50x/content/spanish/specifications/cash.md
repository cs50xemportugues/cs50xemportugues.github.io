# Cash

## Empezando

Abre [VS Code](https://code.cs50.io/).


Comienza haciendo clic dentro de la ventana de tu terminal y luego ejecuta `cd` por sí solo. Deberías encontrar que su "indicador" se parece al siguiente.

```
$
```

Haz clic dentro de esa ventana de terminal y luego ejecuta 

```
wget https://cdn.cs50.net/2022/fall/psets/1/cash.zip
```

seguido de Enter para descargar un archivo ZIP llamado `cash.zip` en tu espacio de código. ¡Ten cuidado de no omitir el espacio entre `wget` y la siguiente URL, o cualquier otro carácter en cuestión!

Ahora ejecuta

```
unzip cash.zip
```

para crear una carpeta llamada `cash`. Ya no necesitas el archivo ZIP, por lo que puedes ejecutar

```
rm cash.zip
```

y responde con "y" seguido de Enter en el indicador para eliminar el archivo ZIP que descargaste.

Ahora escribe

```
cd cash
```

seguido de Enter para moverte a esa carpeta (es decir, abrirla). Tu indicador debería parecerse al siguiente.

```
cash/ $
```

Si todo fue exitoso, deberías ejecutar

```
ls
```

y ver un archivo llamado `cash.c`. Ejecutar `code cash.c` debería abrir el archivo donde escribirás tu código para este problema. Si no es así, retrocede tus pasos y trata de determinar dónde te equivocaste.

## Algoritmos Voraces

![Monedas estadounidenses](https://cs50.harvard.edu/x/2023/psets/1/cash/coins.jpg)

Al hacer cambio, es probable que desees minimizar el número de monedas que entregas a cada cliente, para evitar quedarte sin dinero (o molestar al cliente). Afortunadamente, la informática ha brindado a los cajeros maneras de minimizar la cantidad de monedas que se entregan: algoritmos voraces.

Según el Instituto Nacional de Estándares y Tecnología (NIST), un algoritmo voraz es aquel que "siempre toma la mejor solución inmediata o local mientras encuentra una respuesta. Los algoritmos voraces encuentran la solución óptima global o general para algunos problemas de optimización, pero pueden encontrar soluciones menos óptimas para algunas instancias de otros problemas".

¿Qué significa todo esto? Bien, supongamos que un cajero le debe un cambio a un cliente, y en el cajón del cajero hay cuartos (25¢), dieces (10¢), níqueles (5¢) y centavos (1¢). El problema por resolver es decidir qué monedas y cuántas de cada una deben entregarse al cliente. Piensa en un cajero "voraz" como alguien que quiere resolver el problema de la manera más efectiva posible con cada moneda que saca del cajón. Por ejemplo, si un cliente debe 41¢, la mayor "mordida" o porción que se puede tomar primero (es decir, la mejor inmediata o local) es de 25¢. (Esa mordida es la "mejor" en cuanto a que nos acerca más rápido a 0¢ que cualquier otra moneda). Ten en cuenta que una mordida de este tamaño reduciría lo que era un problema de 41¢ a un problema de 16¢, ya que 41 - 25 = 16. Es decir, el residuo es un problema similar pero más pequeño. No hace falta decir que otra mordida de 25 ¢ sería demasiado grande (suponiendo que el cajero no prefiere perder dinero), así que nuestro cajero voraz pasaría a una mordida de tamaño 10¢, dejándolo con un problema de 6¢. En ese punto, la avaricia demanda una mordida de 5 centavos seguida de una mordida de 1 centavo, momento en el cual el problema queda resuelto. El cliente recibe un cuarto de dólar, un diez centavos, un níquel y un centavo: cuatro monedas en total.

Resulta que este enfoque (es decir, algoritmo) voraz no solo es localmente óptimo, sino también globalmente óptimo para la moneda de Estados Unidos (y también para la Unión Europea). Es decir, siempre y cuando el cajero tenga suficientes de cada moneda, este enfoque de mayor a menor tamaño dará como resultado la menor cantidad de monedas posibles. ¿Qué tan pocos? ¡Bueno, tú nos dices!

## Detalles de Implementación

En `cash.c` hemos implementado la mayor parte (¡pero no todo!) de un programa que le pide al usuario la cantidad de centavos que se le deben a un cliente y luego imprime la menor cantidad de monedas con la cual se puede hacer el cambio. De hecho, `main` ya está implementado para ti. ¡Pero nota cómo `main` llama a varias funciones que aún no se han implementado! Una de esas funciones, `get_cents`, no recibe argumentos (como indica `void`) y devuelve un `int`. El resto de las funciones también reciben un argumento, un `int`, y también devuelven un `int`. Todas ellas regresan `0` actualmente para que el código se compile. Pero querrás reemplazar cada `TODO` y `return 0;` con tu propio código. Específicamente, completa la implementación de esas funciones de la siguiente manera:

- Implementa `get_cents` de tal manera que la función le pida al usuario un número de centavos usando `get_int` y luego devuelva ese número como un `int`. Si el usuario ingresa un número negativo, tu código debe pedirle al usuario de nuevo (Pero no necesitas preocuparte por el usuario ingresando, por ejemplo, una `cadena`, ya que `get_int` se encargará de eso por ti.) Lo más probable es que encuentres un bucle `do while` útil, como en [`mario.c`](https://cdn.cs50.net/2022/fall/lectures/1/src1/mario8.c?highlight)!
- Implementa `calculate_quarters` de tal manera que la función calcule (y devuelva como un `int`) cuántos cuartos debe recibir un cliente si le deben una cierta cantidad de centavos. Por ejemplo, si `cents` es `25`, entonces `calculate_quarters` debe devolver `1`. Si `cents` es `26` o `49` (o cualquier cosa en medio), entonces `calculate_quarters` también debe devolver `1`. Si `cents` es `50` o `74` (o cualquier cosa en medio), entonces `calculate_quarters` debe devolver `2`. Y así sucesivamente.
- Implementa `calculate_dimes` de tal manera que la función calcule lo mismo para los dimes.
- Implementa `calculate_nickels` de tal manera que la función calcule lo mismo para los níqueles.
- Implementa `calculate_pennies` de tal manera que la función calcule lo mismo para los peniques.

¡Ten en cuenta que, a diferencia de las funciones que solo tienen efectos secundarios, las funciones que devuelven un valor deben hacerlo explícitamente con `return`! ¡Asegúrate de no modificar el código de distribución en sí, solo reemplaza el `TODO` dado y el valor de `return` siguiente! También ten en cuenta que, recordando la idea de abstracción, cada una de tus funciones de cálculo debería aceptar cualquier valor de `cents`, no solo aquellos valores que el algoritmo voraz podría sugerir. Si `cents` es 85, por ejemplo, `calculate_dimes` debería devolver 8.

<details><summary>Pista</summary><ul>
  <li data-marker="*">Recuerda que hay varios programas de ejemplo en el <a href="https://cdn.cs50.net/2022/fall/lectures/1/src1/">Código Fuente</a> de la Semana 1 que ilustran cómo las funciones pueden devolver un valor.</li>
</ul></details>

Tu programa debería comportarse de acuerdo a los siguientes ejemplos.

```
$ ./cash
Change owed: 41
4
```

```
$ ./cash
Change owed: -41
Change owed: foo
Change owed: 41
4
```

### Cómo probar tu código

Para este programa, intenta probar tu código manualmente, es una buena práctica:

- Si ingresas `-1`, ¿tu programa te pide de nuevo?
- Si ingresas `0`, ¿tu programa muestra `0`?
- Si ingresas `1`, ¿tu programa muestra `1` (es decir, un centavo)?
- Si ingresas `4`, ¿tu programa muestra `4` (es decir, cuatro centavos)?
- Si ingresas `5`, ¿tu programa muestra `1` (es decir, un níquel)?
- Si ingresas `24`, ¿tu programa muestra `6` (es decir, dos dimes y cuatro centavos)?
- Si ingresas `25`, ¿tu programa muestra `1` (es decir, un cuarto)?
- Si ingresas `26`, ¿tu programa muestra `2` (es decir, un cuarto y un centavo)?
- Si ingresas `99`, ¿tu programa muestra `9` (es decir, tres cuartos, dos dimes y cuatro centavos)?

También puedes ejecutar lo siguiente para evaluar la corrección de tu código utilizando `check50`. ¡Pero asegúrate también de compilar y probarlo por ti mismo!

```
check50 cs50/problems/2023/x/cash
```

<details><summary>¿Está fallando <code>check50</code> al compilar tu código?</summary><p>Asegúrate de haber modificado solo aquellas partes del programa marcadas como <code class="language-plaintext highlighter-rouge">TODO</code>. Si modificas la función <code class="language-plaintext highlighter-rouge">main</code> o agregas alguna variable global, por ejemplo, tu código puede <strong>fallar al compilar</strong>. <code class="language-plaintext highlighter-rouge">check50</code> probará tus cinco funciones de forma independiente, más allá de verificar solo la respuesta final.</p></details>

Y ejecuta lo siguiente para evaluar el estilo de tu código utilizando `style50`.

```
style50 cash.c
```

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

```
submit50 cs50/problems/2023/x/cash
```

