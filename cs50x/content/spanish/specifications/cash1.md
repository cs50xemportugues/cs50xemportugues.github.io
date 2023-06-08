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