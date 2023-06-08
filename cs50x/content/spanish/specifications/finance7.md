## Tutorial

<div class = "ratio ratio-16x9" data-video = ""> <iframe allow = "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen = "" class = "border" data-video = "" src = "https://www.youtube.com/embed/7wPTAwT-6bA?modestbranding = 0 & rel = 0 & showinfo = 0"> </iframe> </div>

## Pruebas

Asegúrate de probar manualmente tu aplicación web, como por ejemplo

- registrando un nuevo usuario y verificando que su página de cartera cargue con la información correcta,
- solicitar una cotización utilizando un símbolo de stock válido,
- comprar una acción varias veces, verificando que la cartera muestre los totales correctos,
- vender todas o algunas de las acciones, volviendo a verificar la cartera, y 
- verificando que tu página de historial muestre todas las transacciones para el usuario registrado.

También prueba algunos usos inesperados, como por ejemplo

- ingresar cadenas alfabéticas en los formularios cuando solo se esperan números,
- ingresar cero o números negativos en los formularios cuando solo se esperan números positivos,
- ingresar valores de punto flotante en los formularios cuando solo se esperan números enteros,
- intentar gastar más dinero del que tiene el usuario,
- intentar vender más acciones de las que tiene el usuario,
- ingresar un símbolo de stock inválido, y
- incluyendo caracteres potencialmente peligrosos como `'` y `;` en consultas de SQL.

Una vez satisfecho, para probar tu código con `check50`, ejecuta lo siguiente:

    check50 cs50/problems/2023/x/finance

<div class="alert" data-alert="warning" role="alert"><p>Ten en cuenta que <code class="language-plaintext highlighter-rouge">check50</code> probará todo el programa en su conjunto. Si lo ejecutas <strong>antes</strong> de completar todas las funciones requeridas, puede informar errores en funciones que en realidad son correctas pero dependen de otras funciones. </p> </div>

Ejecuta lo siguiente para evaluar el estilo de tus archivos de Python usando `style50`.

    style50 *. py

## Solución del personal

Eres libre de estilizar tu aplicación como desees, pero aquí te mostramos cómo luce la solución del personal!

[https://finance.cs50.net/](https://finance.cs50.net/)

Siéntete libre de registrarte para obtener una cuenta y jugar con ella. **No** utilices una contraseña que uses en otros sitios.

Es **razonable** ver el HTML y CSS del personal.