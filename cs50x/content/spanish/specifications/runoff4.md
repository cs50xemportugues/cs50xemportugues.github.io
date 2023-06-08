Paseo
------


<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/-Vc5aGywKxo?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


Uso
---

Su programa debería comportarse como se muestra en el siguiente ejemplo:

    ./runoff Alice Bob Charlie
    Número de votantes: 5
    Rango 1: Alice
    Rango 2: Charlie
    Rango 3: Bob
    
    Rango 1: Alice
    Rango 2: Charlie
    Rango 3: Bob
    
    Rango 1: Bob
    Rango 2: Charlie
    Rango 3: Alice
    
    Rango 1: Bob
    Rango 2: Charlie
    Rango 3: Alice
    
    Rango 1: Charlie
    Rango 2: Alice
    Rango 3: Bob
    
    Alice
    

Prueba
------

Asegúrese de probar su código para asegurarse de que maneja...

*  Una elección con cualquier número de candidatos (hasta un máximo de "9" )
*   Votación por nombre de candidato
*   Votos inválidos para candidatos que no están en la boleta
*   Imprimir al ganador de la elección si hay solamente uno
*   No eliminar a nadie en caso de un empate entre todos los candidatos restantes

Ejecute el siguiente comando para evaluar la exactitud de su código utilizando "check50". Pero asegúrese de compilarlo y probarlo usted mismo también!

    check50 cs50/problems/2023/x/runoff
    

Ejecute el siguiente comando para evaluar el estilo de su código utilizando "style50".

    style50 runoff.c
    

Cómo enviar
-----------

En su terminal, ejecute el siguiente comando para enviar su trabajo.

    submit50 cs50/problems/2023/x/runoff"