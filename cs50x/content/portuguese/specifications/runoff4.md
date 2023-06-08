Passo a passo
------------

<div class="ratio ratio-16x9" data-video=""><iframe allow="acelerômetro; autoplay; encrypted-media; giroscópio; imagem em imagem" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/-Vc5aGywKxo?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


Uso
---

Seu programa deve se comportar como no exemplo abaixo:

    ./runoff Alice Bob Charlie
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
    
    Alice
    

Teste
-----

Certifique-se de testar seu código para verificar se ele lida com ...

*   Uma eleição com qualquer número de candidatos (até o `MAX` de `9`)
*   Votando em um candidato pelo nome
*   Votos inválidos para candidatos que não estão na cédula
*   Imprimir o vencedor da eleição se houver apenas um
*   Não eliminar ninguém no caso de um empate entre todos os candidatos restantes

Execute o seguinte para avaliar a correção do seu código usando `check50`. Mas certifique-se de compilar e testá-lo por si mesmo também!

    check50 cs50/problems/2023/x/runoff
    

Execute o abaixo para avaliar o estilo do seu código usando `style50`.

    style50 runoff.c
    

Como Enviar
-----------

No seu terminal, execute o abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/runoff