Distribuição
------------

### Compreensão

Teoricamente, em uma entrada de tamanho _n_, um algoritmo com tempo de execução _n_ é "assintoticamente equivalente", em termos de _O_, a um algoritmo com tempo de execução de _2n_. Na verdade, ao descrever o tempo de execução de um algoritmo, normalmente nos concentramos no termo dominante (ou seja, mais impactante) (ou seja, _n_ neste caso, já que _n_ pode ser muito maior do que 2). No mundo real, no entanto, a verdade é que _2n_ parece duas vezes mais lento que _n_.

O desafio à sua frente é implementar o verificador ortográfico mais rápido que puder! Mas quando dizemos "o mais rápido", estamos falando de tempo "real", não assintótico.

Em `speller.c `, criamos um programa projetado para verificar a ortografia de um arquivo após carregar um dicionário de palavras do disco na memória. Esse dicionário, enquanto isso, é implementado em um arquivo chamado `dictionary.c`. (Poderia ser implementado em` speller.c`, mas à medida que os programas se tornam mais complexos, geralmente é conveniente dividi-los em vários arquivos.) Os protótipos das funções do arquivo, enquanto isso, não são definidos em `dictionary.c` em si, mas sim em `dictionary.h`. Dessa forma, tanto `speller.c` quanto `dictionary.c` podem incluir o arquivo. Infelizmente, não conseguimos implementar a parte de carregamento. Nem a parte de verificação. Ambos (e um pouco mais) deixamos com você! Mas primeiro, uma turnê.

#### `dictionary.h`

Abra o arquivo `dictionary.h` e você verá alguma nova sintaxe, incluindo algumas linhas que menciona `DICTIONARY_H`. Não se preocupe com isso, mas, se curioso, essas linhas apenas garantem que, mesmo que `dictionary.c` e `speller.c`(que você verá em um momento) incluam este arquivo, o `clang` o compilará apenas uma vez.

A seguir, observe como incluímos um arquivo chamado `stdbool.h`. Esse é o arquivo no qual `bool` é definido. Você não precisou dele antes, já que a Biblioteca CS50 o incluia para você.

Observe também nosso uso de `#define`, uma "diretiva de pré-processador" que define uma "constante" chamada `LENGTH` que tem um valor de `45`. É uma constante no sentido de que você não pode (acidentalmente) alterá-la em seu próprio código. De fato, o `clang` substituirá qualquer menção a `LENGTH` em seu próprio código por, literalmente, `45`. Em outras palavras, não é uma variável, apenas um truque de encontrar e substituir.

Finalmente, observe os protótipos de cinco funções: `check`, `hash`, `load`, `size` e `unload`. Observe como três deles recebem um ponteiro como argumento, de acordo com o `*`:

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">bool</span> <span class="nf">check</span><span class="p">(</span><span class="k">const</span> <span class="kt">char</span> <span class="o">*</span><span class="n">word</span><span class="p">);</span>
<span class="kt">unsigned</span> <span class="kt">int</span> <span class="nf">hash</span><span class="p">(</span><span class="k">const</span> <span class="kt">char</span> <span class="o">*</span><span class="n">word</span><span class="p">);</span>
<span class="n">bool</span> <span class="nf">load</span><span class="p">(</span><span class="k">const</span> <span class="kt">char</span> <span class="o">*</span><span class="n">dictionary</span><span class="p">);</span>
</code></pre></div></div>

Lembre-se de que `char *` é o que costumávamos chamar de `string`. Portanto, esses três protótipos são essencialmente:

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">bool</span> <span class="nf">check</span><span class="p">(</span><span class="k">const</span> <span class="n">string</span> <span class="n">word</span><span class="p">);</span>
<span class="kt">unsigned</span> <span class="kt">int</span> <span class="nf">hash</span><span class="p">(</span><span class="k">const</span> <span class="n">string</span> <span class="n">word</span><span class="p">);</span>
<span class="n">bool</span> <span class="nf">load</span><span class="p">(</span><span class="k">const</span> <span class="n">string</span> <span class="n">dictionary</span><span class="p">);</span>
</code></pre></div></div>

E, enquanto isso, `const` apenas diz que essas strings, quando passadas como argumentos, devem permanecer constantes; você não poderá alterá-las, acidentalmente ou não!