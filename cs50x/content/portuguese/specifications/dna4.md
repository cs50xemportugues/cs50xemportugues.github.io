Dicas
-----

*   Você pode achar o módulo [`csv`](https://docs.python.org/pt-br/3/library/csv.html) do Python útil para ler arquivos CSV na memória. Você pode querer aproveitar [`csv.reader`](https://docs.python.org/pt-br/3/library/csv.html#csv.reader) ou [`csv.DictReader`](https://docs.python.org/pt-br/3/library/csv.html#csv.DictReader).
*   As funções [`open`](https://docs.python.org/pt-br/3.3/tutorial/inputoutput.html#reading-and-writing-files) e [`read`](https://docs.python.org/pt-br/3.3/tutorial/inputoutput.html#methods-of-file-objects) podem ser úteis para ler arquivos de texto na memória.
*   Considere quais estruturas de dados podem ser úteis para manter o controle da informação em seu programa. Uma [`list`](https://docs.python.org/pt-br/3/tutorial/introduction.html#lists) ou um [`dict`](https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries) podem ser úteis.
*   Lembre-se de que definimos uma função (`longest_match`) que, em dado uma sequência de DNA e um STR como entrada, retorna o número máximo de vezes que o STR se repete. Você pode usar essa função em outras partes do seu programa!

Testando
-------

Embora o `check50` esteja disponível para este problema, você é incentivado a testar o seu código por conta própria para cada um dos seguintes items.

*   Execute o seu programa como `python dna.py databases/small.csv sequences/1.txt`. Seu programa deve produzir a saída `Bob`.
*   Execute o seu programa como `python dna.py databases/small.csv sequences/2.txt`. Seu programa deve produzir a saída `No match`.
*   Execute o seu programa como `python dna.py databases/small.csv sequences/3.txt`. Seu programa deve produzir a saída `No match`.
*   Execute o seu programa como `python dna.py databases/small.csv sequences/4.txt`. Seu programa deve produzir a saída `Alice`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/5.txt`. Seu programa deve produzir a saída `Lavender`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/6.txt`. Seu programa deve produzir a saída `Luna`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/7.txt`. Seu programa deve produzir a saída `Ron`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/8.txt`. Seu programa deve produzir a saída `Ginny`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/9.txt`. Seu programa deve produzir a saída `Draco`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/10.txt`. Seu programa deve produzir a saída `Albus`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/11.txt`. Seu programa deve produzir a saída `Hermione`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/12.txt`. Seu programa deve produzir a saída `Lily`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/13.txt`. Seu programa deve produzir a saída `No match`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/14.txt`. Seu programa deve produzir a saída `Severus`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/15.txt`. Seu programa deve produzir a saída `Sirius`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/16.txt`. Seu programa deve produzir a saída `No match`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/17.txt`. Seu programa deve produzir a saída `Harry`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/18.txt`. Seu programa deve produzir a saída `No match`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/19.txt`. Seu programa deve produzir a saída `Fred`.
*   Execute o seu programa como `python dna.py databases/large.csv sequences/20.txt`. Seu programa deve produzir a saída `No match`.

Execute o comando abaixo para avaliar a correção do seu código usando o `check50`. Mas não se esqueça de compilá-lo e testá-lo sozinho também!

    check50 cs50/problems/2023/x/dna
    

Execute o comando abaixo para avaliar o estilo do seu código usando o `style50`.

    style50 dna.py
    

Como Submeter
-------------

No seu terminal, execute o comando abaixo para enviar o seu trabalho.

    submit50 cs50/problems/2023/x/dna"