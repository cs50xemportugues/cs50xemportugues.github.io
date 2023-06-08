# Mario
![screenshot de Mario saltando uma pirâmide](pyramids.png)

Implemente um programa que imprima duas meias-pirâmides de altura especificada, conforme abaixo.

```python
$ python mario.py
Altura: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

## Como começar

Faça login em [code.cs50.io](https://code.cs50.io/), clique na janela do terminal e execute `cd` por si só. Você deve ver que o prompt da janela do seu terminal se parece com o abaixo:

```python
$
```

Execute:

```python
wget https://cdn.cs50.net/2022/fall/psets/6/sentimental-mario-more.zip
```

para baixar um arquivo ZIP chamado `sentimental-mario-more.zip` no diretório do código.

Em seguida, execute:

```python
unzip sentimental-mario-more.zip
```

para criar uma pasta chamada `sentimental-mario-more`. Você não precisa mais do arquivo ZIP, portanto, execute:

```python
rm sentimental-mario-more.zip
```

e responda com "y" seguido de "Enter" na janela para remover o arquivo ZIP que você baixou.

Digite:

```python
cd sentimental-mario-more
```

seguido de "Enter" para entrar (ou seja, abrir) esse diretório. Seu prompt deve se parecer com o abaixo:

```python
sentimental-mario-more/ $
```

Execute `ls` sozinho e você verá `mario.py`. Se você tiver qualquer problema, siga essas mesmas etapas novamente e tente determinar onde você errou!

## Especificação

* Escreva um programa em um arquivo chamado `mario.py` que recria essas meias-pirâmides usando hashes (#) para blocos, exatamente como fez em [Problem Set 1](../../../1/), exceto que seu programa desta vez deve ser escrito em Python.
* Para tornar as coisas mais interessantes, solicite primeiro ao usuário através do `get_int` a altura da meia pirâmide, um número inteiro positivo entre `1` e `8`, inclusivo. (A altura das meias-pirâmides retratadas acima ocorre para `4`, com uma largura de meia pirâmide de `4` com uma lacuna de tamanho `2` separando-as).
* Se o usuário não fornecer um número inteiro positivo não superior a `8`, você deve solicitar novamente o mesmo número.
* Em seguida, gere (com a ajuda de `print` e um ou mais loops) as meias-pirâmides desejadas.
* Tome cuidado para alinhar o canto inferior esquerdo de sua pirâmide com a borda esquerda da janela do seu terminal e certifique-se de que existem dois espaços entre as duas pirâmides e que não existem espaços adicionais após o último conjunto de hashes em cada linha.

## Uso

Seu programa deve se comportar conforme o exemplo abaixo.

```python
$ python mario.py
Altura: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

## Teste

Embora o `check50` esteja disponível para este problema, você é encorajado a testar seu código primeiro por conta própria para cada um dos seguintes.

* Execute seu programa como `python mario.py` e espere por uma entrada. Digite `-1` e pressione enter. Seu programa deve rejeitar essa entrada como inválida, ou seja, solicitar novamente ao usuário que digite outro número.
* Execute seu programa como `python mario.py` e espere por uma entrada. Digite `0` e pressione enter. Seu programa deve rejeitar essa entrada como inválida, ou seja, solicitar novamente ao usuário que digite outro número.
* Execute seu programa como `python mario.py` e espere por uma entrada. Digite `1` e pressione enter. Seu programa deve gerar a saída abaixo. Certifique-se de que a pirâmide esteja alinhada no canto inferior esquerdo do terminal e que não haja espaços extras no final de cada linha.

```python
#  #
```

* Execute seu programa como `python mario.py` e espere por uma entrada. Digite `2` e pressione enter. Seu programa deve gerar a saída abaixo. Certifique-se de que a pirâmide esteja alinhada no canto inferior esquerdo do terminal e que não haja espaços extras no final de cada linha.

```python
 #  #
##  ##
```

* Execute seu programa como `python mario.py` e espere por uma entrada. Digite `8` e pressione enter. Seu programa deve gerar a saída abaixo. Certifique-se de que a pirâmide esteja alinhada no canto inferior esquerdo do terminal e que não haja espaços extras no final de cada linha.

```python
       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
  ######  ######
 #######  #######
########  ########
```

* Execute seu programa como `python mario.py` e espere por uma entrada. Digite `9` e pressione enter. Seu programa deve rejeitar essa entrada como inválida, ou seja, solicitar novamente ao usuário que digite outro número. Em seguida, digite `2` e pressione enter. Seu programa deve gerar a saída abaixo. Certifique-se de que a pirâmide esteja alinhada no canto inferior esquerdo do terminal e que não haja espaços extras no final de cada linha.

```python
 #  #
##  ##
```

* Execute seu programa como `python mario.py` e espere por uma entrada. Digite `foo` e pressione enter. .Seu programa deve rejeitar essa entrada como inválida, ou seja, solicitar novamente ao usuário que digite outro número.
* Execute seu programa como `python mario.py` e espere por uma entrada. Não digite nada e pressione enter. Seu programa deve rejeitar essa entrada como inválida, ou seja, solicitar novamente ao usuário que digite outro número.

Execute o abaixo para avaliar a correção do seu código usando o `check50`. Mas certifique-se de compilar e testar a si mesmo também!

```python
check50 cs50/problems/2023/x/sentimental/mario/more
```

Execute o abaixo para avaliar o estilo do seu código usando o `style50`.

```python
style50 mario.py
```

## Como enviar

No seu terminal, execute o abaixo para enviar seu trabalho.

```python
submit50 cs50/problems/2023/x/sentimental/mario/more
```