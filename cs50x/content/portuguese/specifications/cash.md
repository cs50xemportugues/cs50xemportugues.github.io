# Dinheiro

## Começando

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da janela do seu terminal e, em seguida, execute `cd` sozinho. Você deve ver que o "prompt" é parecido com o abaixo.

```
$
```

Clique dentro da janela do terminal novamente e execute

```
wget https://cdn.cs50.net/2022/fall/psets/1/cash.zip
```

seguido de Enter para baixar um arquivo ZIP chamado `cash.zip` em sua área de trabalho. Certifique-se de não esquecer do espaço entre "wget" e a URL a seguir, ou qualquer outro caractere, por assim dizer!

Agora execute

```
unzip cash.zip
```

para criar uma pasta chamada "cash". Você não precisa mais do arquivo ZIP, então execute o seguinte comando para remover o arquivo:

```
rm cash.zip
```

e responda com "y" seguido de Enter para remover o arquivo ZIP que você baixou.

Agora digite

```
cd cash
```

seguido de Enter para se mover para dentro (abrir) desse diretório. O prompt deve exibir:

```
cash/ $
```

Se tudo estiver correto, execute

```
ls
```

e você deve ver um arquivo chamado `cash.c`. Executar `code cash.c` abrirá o arquivo onde você digitará seu código para este conjunto de problemas. Caso contrário, refaça seus passos e verifique se consegue determinar onde você errou!

## Algoritmos gananciosos

![US coins](https://cs50.harvard.edu/x/2023/psets/1/cash/coins.jpg)

Ao fazer troco, é provável que você queira minimizar o número de moedas que está entregando para cada cliente, para não ficar sem moedas (ou incomodar o cliente!). Felizmente, a ciência da computação deu aos caixas de todo o mundo maneiras de minimizar o número de moedas: algoritmos gananciosos.

De acordo com o Instituto Nacional de Padrões e Tecnologia (NIST), um algoritmo ganancioso é aquele "que sempre toma a melhor solução imediata ou local enquanto encontra uma resposta. Algoritmos gananciosos encontram soluções ótimas globais ou globais para alguns problemas de otimização, mas podem encontrar soluções menos que ótimas para algumas instâncias de outros problemas".

O que tudo isso significa? Bem, suponha que um caixa deve dar troco a um cliente e que na gaveta do caixa há moedas de vinte e cinco centavos (25¢), dez centavos (10¢), cinco centavos (5¢) e um centavo (1¢). O problema a ser resolvido é decidir quais moedas e quantas de cada uma entregar ao cliente. Pense em um caixa "ganancioso" como aquele que quer tirar o maior pedaço possível desse problema com cada moeda que ele tira da gaveta. Por exemplo, se um cliente deve R$0,41, a maior "mordida" (ou solução imediata ou local) que pode ser tomada é de R$0,25. (Essa mordida é a "melhor" porque nos aproxima de R$0 mais rapidamente do que qualquer outra moeda.) Observe que uma mordida desse tamanho reduziria o problema de R$0,41 para R$0,16, já que 41 - 25 = 16. Ou seja, o restante é um problema semelhante, mas menor. Não é preciso dizer que outra mordida de R$0,25 seria muito grande (supondo que o caixa prefira não perder dinheiro), então o caixa ganancioso passaria para uma mordida de tamanho 10 centavos, deixando-o com um problema de 6 centavos. Nesse ponto, a ganância exige uma mordida de 5 centavos, seguida por uma mordida de 1 centavo, momento em que o problema é resolvido. O cliente recebe uma moeda de vinte e cinco centavos, uma de dez centavos, uma de cinco centavos e uma de um centavo: quatro moedas no total.

Acontece que essa abordagem gananciosa (ou seja, algoritmo) não é apenas localmente ótima, mas também globalmente ótima para a moeda americana (e também para a União Europeia). Ou seja, desde que um caixa tenha o suficiente de cada moeda, essa abordagem de maior a menor resultará nas menos moedas possíveis. Quantas vezes? Bem, você nos diz!

## Detalhes da Implementação

Em `cash.c`, nós implementamos a maior parte (mas não toda!) de um programa que solicita ao usuário a quantidade de centavos que um cliente deve e depois imprime o menor número de moedas com as quais a mudança pode ser feita. De fato, `main` já está implementado para você. Mas observe como `main` chama várias funções que ainda não estão implementadas! Uma dessas funções, `get_cents`, não recebe argumentos (como indicado por `void`) e retorna um `int`. O restante das funções também recebe um argumento, um `int`, e também retorna um `int`. Todos eles atualmente retornam `0` para que o código compile. Mas você vai querer substituir todos os `TODO` e `return 0;` pelo seu próprio código. Especificamente, conclua a implementação dessas funções da seguinte forma:

- Implemente `get_cents` de tal forma que a função solicite ao usuário um número de centavos usando `get_int` e então retorne esse número como um `int`. Se o usuário inserir um `int` negativo, o seu código deve solicitar ao usuário que insira novamente. (Mas você não precisa se preocupar com o usuário inserindo, por exemplo, uma `string`, já que `get_int` cuidará disso para você). Provavelmente, você encontrará um loop `do while`, como em [`mario.c`](https://cdn.cs50.net/2022/fall/lectures/1/src1/mario8.c?highlight), útil!
- Implemente `calculate_quarters` de tal forma que a função calcule (e retorne como um `int`) quantos trimestres um cliente deve receber se ele receber alguns centavos. Por exemplo, se `cents` for `25`, então `calculate_quarters` deve retornar `1`. Se `cents` for `26` ou `49` (ou qualquer coisa entre eles), então `calculate_quarters` também deve retornar `1`. Se `cents` for `50` ou `74` (ou qualquer coisa entre eles), então `calculate_quarters` deve retornar `2`. E assim por diante.
- Implemente `calculate_dimes` de tal forma que a função calcule o mesmo para moedas de dez centavos.
- Implemente `calculate_nickels` de tal forma que a função calcule o mesmo para moedas de cinco centavos.
- Implemente `calculate_pennies` de tal forma que a função calcule o mesmo para moedas de um centavo.

Observe que, ao contrário de funções que possuem apenas efeitos colaterais, as funções que retornam um valor devem fazê-lo explicitamente com `return`! Tome cuidado para não modificar o código de distribuição em si, apenas substitua os `TODO`s e o valor `return` subsequente! Observe também que, recordando a ideia de abstração, cada uma de suas funções de cálculo deve aceitar qualquer valor de `cents`, não apenas aqueles valores que o algoritmo ávido pode sugerir. Se `cents` for 85, por exemplo, `calculate_dimes` deve retornar 8.

<details><summary>Dica</summary><ul>
  <li data-marker="*">Lembre-se de que existem vários programas de exemplo no <a href="https://cdn.cs50.net/2022/fall/lectures/1/src1/">código-fonte</a> da Semana 1, que ilustram como as funções podem retornar um valor.</li>
</ul></details>

Seu programa deve se comportar conforme os exemplos abaixo.

```
$ ./cash
O valor do troco é: 41
4
```
```
$ ./cash
O valor do troco é: -41
O valor do troco é: foo
O valor do troco é: 41
4
```

### Como Testar Seu Código

Para este programa, tente testar seu código manualmente, é uma boa prática:

- Se você inserir `-1`, o seu programa solicita que você insira novamente?
- Se você inserir `0`, o seu programa exibe `0`?
- Se você inserir `1`, o seu programa exibe `1` (ou seja, uma moeda de um centavo)?
- Se você inserir `4`, o seu programa exibe `4` (ou seja, quatro moedas de um centavo)?
- Se você inserir `5`, o seu programa exibe `1` (ou seja, uma moeda de cinco centavos)?
- Se você inserir `24`, o seu programa exibe `6` (ou seja, duas moedas de dez centavos e quatro moedas de um centavo)?
- Se você inserir `25`, o seu programa exibe `1` (ou seja, uma moeda de vinte e cinco centavos)?
- Se você inserir `26`, o seu programa exibe `2` (ou seja, uma moeda de vinte e cinco centavos e uma moeda de um centavo)?
- Se você inserir `99`, o seu programa exibe `9` (ou seja, três moedas de vinte e cinco centavos, duas moedas de dez centavos e quatro moedas de um centavo)?

Você também pode executar o comando abaixo para avaliar a precisão do seu código usando `check50`. Mas lembre-se de compilar e testá-lo sozinho também!

```
check50 cs50/problems/2023/x/cash
```

<details><summary>O <code>check50</code> não está compilando o seu código corretamente?</summary><p>Certifique-se de ter modificado apenas as partes do programa marcadas como <code class="language-plaintext highlighter-rouge">TODO</code>. Se você modificar a função <code class="language-plaintext highlighter-rouge">main</code> ou adicionar quaisquer variáveis globais, por exemplo, seu código pode <strong>não ser compilado</strong>. O `check50testará` suas cinco funções independentemente, para além de verificar apenas a resposta final.</p></details>

E execute o comando abaixo para avaliar o estilo do seu código usando `style50`.

```
style50 cash.c
```

## Como Enviar

No terminal, execute o comando abaixo para enviar seu trabalho.

```
submit50 cs50/problems/2023/x/cash
```

