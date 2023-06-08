#### Sepia

La mayoría de los programas de edición de imágenes tienen un filtro de "sepia", que le da a las imágenes un aspecto antiguo al hacer que toda la imagen se vea un poco rojizo-marrón.

Una imagen se puede convertir en sepia tomando cada píxel y calculando nuevos valores de rojo, verde y azul en función de los valores originales de los tres.

Existen varios algoritmos para convertir una imagen en sepia, pero para este problema, te pediremos que uses el siguiente algoritmo. Para cada píxel, los valores de color de sepia deben calcularse en función de los valores de color originales según lo indicado a continuación.

      sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue
      sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue
      sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue

Por supuesto, el resultado de cada una de estas fórmulas puede no ser un número entero, pero cada valor se puede redondear al número entero más cercano. También es posible que el resultado de la fórmula sea un número mayor que 255, el valor máximo de un valor de color de 8 bits. En ese caso, los valores de rojo, verde y azul deben estar limitados a 255. Como resultado, podemos garantizar que los valores de rojo, verde y azul resultantes serán números enteros entre 0 y 255, inclusive.

#### Reflexión

Algunos filtros también pueden mover los píxeles. Reflejar una imagen, por ejemplo, es un filtro en el que la imagen resultante es lo que obtendrías colocando la imagen original frente a un espejo. Así, cualquier píxel en el lado izquierdo de la imagen debería estar en el lado derecho, y viceversa.

Ten en cuenta que todos los píxeles originales de la imagen original seguirán presentes en la imagen reflejada, solo que esos píxeles pueden haberse reorganizado para estar en un lugar diferente en la imagen.

#### Difuminado

Existen varias formas de lograr el efecto de difuminado o suavizado de una imagen. Para este problema, usaremos el "difuminado de cuadro", que funciona tomando cada píxel y, para cada valor de color, dándole un nuevo valor promediando los valores de color de los píxeles vecinos.

Considera la siguiente malla de píxeles, donde hemos numerado cada píxel.

![una malla de píxeles](https://cs50.harvard.edu/x/2023/psets/4/filter/less/grid.png)

El nuevo valor de cada píxel sería el promedio de los valores de todos los píxeles que estén dentro de 1 fila y columna del píxel original (formando un cuadrado de 3x3). Por ejemplo, cada uno de los valores de color para el píxel 6 se obtendría promediando los valores de color originales de los píxeles 1, 2, 3, 5, 6, 7, 9, 10 y 11 (note que el píxel 6 en sí mismo está incluido en la promedio). Del mismo modo, los valores de color para el píxel 11 se obtendrían promediando los valores de color de los píxeles 6, 7, 8, 10, 11, 12, 14, 15 y 16.

Para un píxel en el borde o la esquina, como el píxel 15, aún buscaríamos todos los píxeles dentro de 1 fila y columna: en este caso, los píxeles 10, 11, 12, 14, 15 y 16.