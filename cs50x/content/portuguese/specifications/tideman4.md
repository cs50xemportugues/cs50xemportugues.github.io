Uso
---

Seu programa deve se comportar como no exemplo abaixo:

    ./tideman Alice Bob Charlie
    Número de eleitores: 5
    Classificação 1: Alice
    Classificação 2: Charlie
    Classificação 3: Bob
    
    Classificação 1: Alice
    Classificação 2: Charlie
    Classificação 3: Bob
    
    Classificação 1: Bob
    Classificação 2: Charlie
    Classificação 3: Alice
    
    Classificação 1: Bob
    Classificação 2: Charlie
    Classificação 3: Alice
    
    Classificação 1: Charlie
    Classificação 2: Alice
    Classificação 3: Bob
    
    Charlie
    

Testando
--------

Certifique-se de testar seu código para verificar se ele lida com...

*   uma eleição com qualquer número de candidatos (até o `MAX` de `9`)
*   votar em um candidato pelo nome
*   votos inválidos para candidatos que não estão na cédula
*   imprimir o vencedor da eleição

Execute o seguinte para avaliar a correção do seu código usando `check50`. Mas certifique-se de compilar e testar por conta própria também!

    check50 cs50/problems/2023/x/tideman
    

Execute o seguinte para avaliar o estilo do seu código usando `style50`.

    style50 tideman.c
    

Como Enviar
-----------

Em seu terminal, execute o seguinte para enviar seu trabalho.

    submit50 cs50/problems/2023/x/tideman"