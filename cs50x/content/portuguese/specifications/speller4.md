Especificação
-------------

Tudo bem, o desafio agora para você é implementar, em ordem, `load`, `hash`, `size`, `check` e `unload` da maneira mais eficiente possível usando uma tabela hash, de tal forma que `TIME IN load`, `TIME IN check`, `TIME IN size` e `TIME IN unload` sejam minimizados. Certamente, não é óbvio o que significa ser minimizado, já que essas referências certamente variarão à medida que você alimentar o `speller` com diferentes valores para `dictionary` e para `text`. Mas aí está o desafio, se não a diversão, desse problema. Este problema é sua chance de projetar. Embora convidemos você a minimizar o espaço, o seu inimigo final é o tempo. Mas antes de começar, algumas especificações de nossa parte.

*   Você não pode alterar `speller.c` ou `Makefile`.
*   Você pode alterar `dictionary.c` (e, de fato, deve fazê-lo para concluir as implementações de `load`, `hash`, `size`, `check` e `unload`), mas não pode alterar as declarações (ou seja, protótipos) de `load`, `hash`, `size`, `check` ou `unload`. Você pode, no entanto, adicionar novas funções e variáveis (locais ou globais) a `dictionary.c`.
*   Você pode alterar o valor de `N` em `dictionary.c`, para que sua tabela hash possa ter mais buckets.
*   Você pode alterar `dictionary.h`, mas não pode alterar as declarações de `load`, `hash`, `size`, `check` ou `unload`.
*   Sua implementação de `check` deve ser insensível a maiúsculas e minúsculas. Em outras palavras, se `foo` estiver no dicionário, então `check` deve retornar verdadeiro para qualquer capitalização do mesmo; nenhum dos `foo`, `foO`, `fOo`, `fOO`, `fOO`, `Foo`, `FoO`, `FOo` e `FOO` devem ser considerados como ignorados.
*   Com relação à capitalização, sua implementação de `check` só deve retornar `true` para as palavras que realmente estiverem no `dictionary`. Tenha cuidado para não codificar palavras comuns (por exemplo, `a`), para que não venhamos a passar para sua implementação um `dictionary` sem essas mesmas palavras. Além disso, somente os possessivos permitidos são aqueles que realmente estão no `dictionary`. Em outras palavras, mesmo que `foo` esteja no `dictionary`, `check` deve retornar `false` para `foo's` se `foo's` também não estiver no `dictionary`.
*   Você pode pressupor que qualquer `dictionary` passado para o seu programa terá a mesma estrutura que a nossa, classificada em ordem alfabética de cima para baixo com uma palavra por linha, cada uma das quais termina com `\n`. Você também pode assumir que o `dictionary` conterá pelo menos uma palavra, que nenhuma palavra terá mais de `LENGTH` (uma constante definida em `dictionary.h`) caracteres, que nenhuma palavra aparecerá mais de uma vez, que cada palavra conterá apenas caracteres alfabéticos minúsculos e possivelmente apostrofes, e que nenhuma palavra começará com um apóstrofo.
*   Você pode pressupor que o `check` só receberá palavras que contenham caracteres alfabéticos (maiúsculos ou minúsculos) e possivelmente apostrofes.
*   Seu corretor ortográfico pode somente receber `text` e, opcionalmente, `dictionary` como entrada. Embora você possa estar inclinado (particularmente se é mais experiente) a “pre-processar” nosso dicionário padrão para derivar uma “função hash ideal” para ele, você não pode salvar a saída de qualquer pré-processamento em disco com o intuito de carregá-la novamente na memória em execuções subsequentes do verificador ortográfico para ganhar uma vantagem.
*   Seu corretor ortográfico não deve vazar memória. Certifique-se de verificar vazamentos com `valgrind`.
*   **A função hash que você escreve deve ser sua, não aquela que você procura online.** Há muitas maneiras de implementar uma função hash além de usar o primeiro caractere (ou caracteres) de uma palavra. Considere uma função hash que usa a soma dos valores ASCII ou o comprimento de uma palavra. Uma boa função hash tende a reduzir as “colisões” e tem uma distribuição bastante uniforme em “buckets” da tabela hash.

Ok, prontos para começar?

*   Implemente `load`.
*   Implemente `hash`.
*   Implemente `size`.
*   Implemente `check`.
*   Implemente `unload`.

Guias
------------

Observe que há 6 vídeos na playlist abaixo.


<div class="alert" data-alert="danger" role="alert"><p>Embora o guia de Speller indique que é razoável usar uma função hash encontrada on-line, este vídeo é de uma versão anterior do problema em que permitimos isso. Conforme a especificação acima, a função hash que você escrever deve ser sua; você <strong>não pode</strong> usar uma função hash que encontrar on-line. Certifique-se de citar quaisquer fontes externas que você tenha referenciado ao escrever sua função hash.</p></div>

<div class="ratio ratio-16x9" data-video=""><iframe allow="acelerômetro; autoplay; encrypted-media; giroscópio; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/_z57x5PGF4w?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T382T4b6jjwX_qbU23E_Unwcz"></iframe></div>