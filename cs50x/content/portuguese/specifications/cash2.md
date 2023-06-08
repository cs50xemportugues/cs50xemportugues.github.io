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