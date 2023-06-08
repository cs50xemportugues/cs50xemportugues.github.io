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