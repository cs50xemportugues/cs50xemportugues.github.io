### Filtrado de Imágenes

¿Qué significa filtrar una imagen? Se puede pensar que al filtrar una imagen se toman los píxeles de una imagen original y se modifica cada píxel de tal manera que un efecto particular es evidente en la imagen resultante.

#### Escala de Grises

Un filtro común es el filtro de "escala de grises", en el que tomamos una imagen y queremos convertirla a blanco y negro. ¿Cómo funciona?

Recuerda que si los valores rojo, verde y azul están todos establecidos en `0x00` (hexadecimal para `0`), entonces el píxel es negro. Y si todos los valores están establecidos en `0xff` (hexadecimal para `255`), entonces el píxel es blanco. Mientras los valores de rojo, verde y azul estén iguales, el resultado será tonos de gris que van desde el espectro de blanco a negro, con valores más altos que indican tonos más claros (más cerca del blanco) y valores más bajos que indican tonos más oscuros (más cerca del negro).

Por lo tanto, para convertir un píxel a tono de gris, solo necesitamos asegurarnos de que los valores de rojo, verde y azul sean iguales. Pero, ¿cómo sabemos qué valor darles? Bueno, probablemente es razonable esperar que si los valores de rojo, verde y azul originales eran bastante altos, entonces el nuevo valor también debería ser bastante alto. Y si los valores originales eran bajos, entonces el nuevo valor también debería ser bajo.

De hecho, para garantizar que cada píxel de la nueva imagen tenga el mismo brillo o oscuridad general que la vieja imagen, podemos tomar el promedio de los valores de rojo, verde y azul para determinar qué tono de gris hacer para el nuevo píxel.

Al aplicar eso a cada píxel en la imagen, el resultado será una imagen convertida a escala de grises.

#### Reflejo

Algunos filtros también pueden mover los píxeles. Reflejar una imagen, por ejemplo, es un filtro en el que la imagen resultante es lo que se obtendría al colocar la imagen original frente a un espejo. Así que cualquier píxel en el lado izquierdo de la imagen terminaría en el lado derecho, y viceversa.

Note que todos los píxeles originales de la imagen original seguirán presentes en la imagen reflejada, solo que esos píxeles pueden haberse rearrangeado a otro lugar en la imagen.

#### Difuminado

Hay varias maneras de crear el efecto de difuminado o suavizado en una imagen. Para este problema, usaremos el "difuminado de caja", que funciona tomando cada píxel y, para cada valor de color, dándole un nuevo valor promediando los valores de color de los píxeles adyacentes.

Considera la siguiente cuadrícula de píxeles, donde hemos numerado cada píxel.

![a grid of pixels](https://cs50.harvard.edu/x/2023/psets/4/filter/more/grid.png)

El nuevo valor de cada píxel sería el promedio de los valores de todos los píxeles que están dentro de 1 fila y columna del píxel original (formando una caja 3x3). Por ejemplo, cada uno de los valores de color del píxel 6 se obtendría promediando los valores de color originales de los píxeles 1, 2, 3, 5, 6, 7, 9, 10 y 11 (note que el píxel 6 en sí está incluido en el promedio). De igual manera, los valores de color del píxel 11 se obtendrían promediando los valores de color de los píxeles 6, 7, 8, 10, 11, 12, 14, 15 y 16.

Para un píxel a lo largo del borde o la esquina, como el píxel 15, aún buscaríamos todos los píxeles dentro de 1 fila y columna: en este caso, los píxeles 10, 11, 12, 14, 15 y 16.