Uso
---

Su programa debe comportarse como se muestra en el ejemplo a continuación:

    ./tideman Alice Bob Charlie
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
    
    Charlie
    

Prueba
------

Asegúrese de probar su código para verificar que maneje...

*   Una elección con cualquier número de candidatos (hasta un máximo de `9`)
*   Votar por un candidato por su nombre
*   Votos inválidos por candidatos que no están en la lista
*   Imprimir el ganador de la elección

Ejecute lo siguiente para evaluar la corrección de su código usando `check50`. ¡Pero asegúrese de compilarlo y probarlo también!

    check50 cs50/problems/2023/x/tideman
    

Ejecute lo siguiente para evaluar el estilo de su código usando `style50`.

    style50 tideman.c
    

Cómo enviar
-----------

En la terminal, ejecute lo siguiente para enviar su trabajo.

    submit50 cs50/problems/2023/x/tideman