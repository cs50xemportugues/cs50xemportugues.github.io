Passo a Passo
--------------

<div class="ratio ratio-16x9" data-video=""><iframe allow="acelerômetro; autoplay; criptografia-mídia; giroscópio; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/ooL0r_8N9ms?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

Uso
---

Seu programa deve se comportar conforme os exemplos abaixo.

    $ ./recover
    Uso: ./recover IMAGEM

onde `IMAGEM` é o nome da imagem forense. Por exemplo:

    $ ./recover card.raw
    
Dicas
-----

Lembre-se de que você pode abrir `card.raw` programaticamente com o `fopen`, como abaixo, desde que `argv [1]` exista.

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kt">ARQUIVO</span> <span class="o">*</span><span class="n">arquivo</span> <span class="o">=</span> <span class="n">fopen</span><span class="p">(</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="s">"r"</span><span class="p">);</span>
</code></pre></div></div>
    

Quando executado, seu programa deve recuperar cada um dos JPEGs de `card.raw`, armazenando cada um como um arquivo separado no diretório de trabalho atual. Seu programa deve numerar os arquivos que ela produz, nomeando cada um como `###.jpg`, onde `###` é um número decimal de três dígitos a partir de `000`. Use a função [`sprintf`](https://man.cs50.io/3/sprintf) e note que ela armazena uma string formatada em uma localização na memória. Dado o formato prescrito `###.jpg` para o nome do arquivo JPEG, quantos bytes você deve alocar para essa string? (Não se esqueça do caractere NUL!)

Você não precisa tentar recuperar os nomes originais dos JPEGs. Para verificar se os JPEGs que seu programa gerou estão corretos, basta clicar duas vezes e dar uma olhada! Se cada foto parecer intacta, provavelmente sua operação foi um sucesso!

É provável, no entanto, que a primeira versão do código que seu programa gera não esteja correta. (Se você os abrir e não vir nada, eles provavelmente não estão corretos!) Execute o comando abaixo para excluir todos os arquivos JPEG do seu diretório de trabalho atual.

    $ rm *.jpg
    
Se você não quiser ter que confirmar cada exclusão, execute o comando abaixo.

    $ rm -f *.jpg
    

Tenha cuidado com a opção `-f`, porque ela força a exclusão sem pedir confirmação.

Se você gostaria de criar um novo tipo para armazenar um byte de dados, você pode fazer isso usando o código abaixo, que define um novo tipo chamado `BYTE` como `uint8_t` (um tipo definido em `stdint.h`, representando um inteiro não assinado de 8 bits).

    typedef uint8_t BYTE;
    

Lembre-se também de que você pode ler dados de um arquivo usando a função [`fread`](https://man.cs50.io/3/fread), que lerá dados de um arquivo para uma localização na memória. Conforme sua [página do manual](https://man.cs50.io/3/fread), `fread` retorna o número de bytes que ela leu, o que significa que ela deve retornar `512` ou `0`, dado que `card.raw` contém algum número de blocos de 512 bytes. Para ler cada bloco de `card.raw`, após abri-lo com `fopen`, deve ser suficiente usar um loop como:

   
<pre class="highlight">
<span class="k">while</span> (fread(buffer, <span class="mi">1</span>, BLOCK_SIZE, arquivo_raw) == BLOCK_SIZE)
{


}
</pre>
Dessa forma, assim que `fread` retornar `0` (o que efetivamente é `false`), seu loop será encerrado.

Testando
-------

Digite o código abaixo para avaliar a correção do seu código usando `check50`. Mas não se esqueça de compilá-lo, testá-lo você mesmo também!

    check50 cs50/problems/2023/x/recover
    

Digite o código abaixo para avaliar o estilo do seu código usando `style50`.

    style50 recover.c
    

Como Enviar
---------------

Em seu terminal, execute o código abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/recover"