### Sentenças

A última informação que a fórmula Coleman-Liau se preocupa, além do número de letras e palavras, é o número de sentenças. Determinar o número de sentenças pode ser surpreendentemente complicado. Você pode imaginar que uma sentença é apenas qualquer sequência de caracteres que termina com um ponto, mas é claro que as sentenças também podem terminar com um ponto de exclamação ou uma interrogação. Mas é claro, nem todos os pontos necessariamente significam que a sentença acabou. Por exemplo, considere a sentença abaixo.

    Sr. e Sra. Dursley, do número quatro da Rua dos Alfeneiros, estavam orgulhosos por dizer que eram perfeitamente normais, muito obrigado.

Essa é apenas uma única sentença, mas existem três pontos! Para este problema, pediremos para você ignorar essa sutileza: você deve considerar qualquer sequência de caracteres que termine com `.` ou `!` ou `?` como uma sentença (então para a "sentença" acima, você deve considerar três sentenças). Na prática, a detecção de limite de sentença precisa ser um pouco mais inteligente para lidar com esses casos, mas não se preocupe com isso por enquanto.

Adicione ao arquivo `readability.c`, abaixo do `main`, uma função chamada `count_sentences` que recebe um argumento, uma `string` de texto, e que retorna um `int`, o número de sentenças naquele texto. Certifique-se de adicionar o protótipo da função também no topo do arquivo, para que o `main` saiba como chamá-lo. (Deixamos o protótipo da função para você definir!)

Então, chame essa função no `main` para que o seu programa também imprima o número de sentenças no texto.

O programa agora deve se comportar conforme o abaixo.

    $ ./readability
    Texto: Quando ele tinha quase treze anos, meu irmão Jem quebrou o braço gravemente no cotovelo. Quando sarou, e os medos de Jem de nunca mais poder jogar futebol foram acalmados, ele raramente se mostrou autoconsciente sobre sua lesão. Seu braço esquerdo era um pouco mais curto do que o direito; quando ele ficava em pé ou caminhava, o dorso de sua mão ficava em ângulo reto com o corpo, o polegar paralelo à coxa.
    295 letras
    70 palavras
    3 sentenças

### Colocando Tudo Junto

Agora é hora de juntar todas as peças! Lembre-se de que o índice Coleman-Liau é calculado usando a fórmula:

    índice = 0.0588 * L - 0.296 * S - 15.8

onde `L` é o número médio de letras por 100 palavras no texto e `S` é o número médio de sentenças por 100 palavras no texto.

Modifique o `main` em `readability.c` para que, em vez de imprimir o número de letras, palavras e sentenças, ele imprima (apenas) o nível de grau conforme definido pelo índice Coleman-Liau (por exemplo, `"Grau 2"` ou `"Grau 8"` ou similar). Certifique-se de arredondar o número do índice resultante para o número inteiro mais próximo!

<details><summary>Dicas</summary><ul>
  <li data-marker="*">Lembre-se de que `round` é declarado em `math.h`, de acordo com o <a href="https://manual.cs50.io/">manual.cs50.io</a>!</li>
  <li data-marker="*">Lembre-se de que, ao dividir valores do tipo `int` em C, o resultado também será um `int`, com qualquer resto (ou seja, dígitos após a vírgula decimal) descartados. Em outras palavras, o resultado será "truncado". Você pode querer converter um ou mais valores em `float` antes de fazer a divisão ao calcular `L` e `S`!</li>
</ul></details>

Se o número do índice resultante for 16 ou maior (equivalente ou superior a um nível de leitura de graduação superior), seu programa deve imprimir `"Grau 16+"` em vez de imprimir um número de índice exato. Se o número do índice for menor que 1, seu programa deve imprimir `"Antes do Grau 1"`.