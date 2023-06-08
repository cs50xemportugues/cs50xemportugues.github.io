Especificação
-------------

* Escreva, em um arquivo chamado `readability.py`, um programa que primeiro solicita ao usuário que digite algum texto e, em seguida, apresente o nível de leitura do texto de acordo com a fórmula Coleman-Liau, exatamente como fez no [Problem Set 2](../../ 2 /), exceto que desta vez o programa deve ser escrito em Python.
   * Lembre-se de que o índice Coleman-Liau é calculado como `0.0588 * L - 0.296 * S - 15.8`, onde `L` é o número médio de letras por 100 palavras no texto e` S` é o número médio de frases por 100 palavras no texto.
* Use o `get_string` da biblioteca CS50 para obter a entrada do usuário e `print` para exibir a resposta.
* Seu programa deve contar o número de letras, palavras e frases no texto. Você pode supor que uma letra é qualquer caractere minúsculo de `a` a `z` ou qualquer caractere maiúsculo de `A` a `Z`, qualquer sequência de caracteres separados por espaços deve contar como uma palavra e que qualquer ocorrência de um ponto, ponto de exclamação ou ponto de interrogação indica o final de uma frase.
* Seu programa deve imprimir como saída `"Grade X"` onde `X` é o nível de leitura calculado pela fórmula Coleman-Liau, arredondado para o inteiro mais próximo.
* Se o índice resultante for 16 ou superior (equivalente ou superior a um nível de leitura de graduação sênior), seu programa deve apresentar a mensagem `"Grade 16+"` em vez de fornecer o índice exato. Se o índice for inferior a 1, seu programa deve apresentar a mensagem `"Before Grade 1"`.

Uso
-----

Seu programa deve se comportar como o exemplo abaixo.

    $ python readability.py
    Text: Parabéns! Hoje é o seu dia. Você está a caminho de lugares incríveis! Está indo embora!
    Grade 3
