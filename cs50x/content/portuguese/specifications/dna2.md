Background
----------

O DNA, o portador de informações genéticas nos seres vivos, tem sido utilizado na justiça criminal por décadas. Mas como exatamente funciona o perfil de DNA? Dada uma sequência de DNA, como os investigadores forenses podem identificar a quem pertence?

Bem, o DNA é realmente apenas uma sequência de moléculas chamadas nucleotídeos, organizados em uma forma particular (uma dupla hélice). Cada célula humana tem bilhões de nucleotídeos organizados em sequência. Cada nucleotídeo do DNA contém uma das quatro bases diferentes: adenina (A), citosina (C), guanina (G) ou timina (T). Algumas partes dessa sequência (ou seja, genoma) são iguais ou pelo menos muito semelhantes em quase todos os humanos, mas outras partes da sequência têm uma diversidade genética mais alta e, portanto, variam mais na população.

Um lugar onde o DNA tende a ter uma alta diversidade genética é em Repetições em Tandem Curtas (STRs). Um STR é uma sequência curta de bases de DNA que tende a se repetir consecutivamente inúmeras vezes em locais específicos dentro do DNA de uma pessoa. O número de vezes que um determinado STR é repetido varia muito entre os indivíduos. Nas amostras de DNA abaixo, por exemplo, Alice tem o STR `AGAT` repetido quatro vezes em seu DNA, enquanto Bob tem o mesmo STR repetido cinco vezes.

![Sample STRs](https://cs50.harvard.edu/x/2023/psets/6/dna/strs.png)

Usar vários STRs, em vez de apenas um, pode melhorar a precisão do perfil de DNA. Se a probabilidade de duas pessoas terem o mesmo número de repetições para um único STR é de 5%, e o analista examina 10 STRs diferentes, então a probabilidade de que duas amostras de DNA correspondam por pura coincidência é de cerca de 1 em 1 quatrilhão (assumindo que todos os STRs são independentes entre si). Então, se as duas amostras de DNA tiverem o mesmo número de repetições para cada um dos STRs, o analista pode ter bastante confiança de que elas vieram da mesma pessoa. CODIS, o banco de dados de DNA do FBI, usa 20 STRs diferentes como parte de seu processo de perfil de DNA.

Como seria um banco de dados de DNA? Bem, em sua forma mais simples, você poderia imaginar formatar um banco de dados de DNA como um arquivo CSV, em que cada linha corresponde a um indivíduo e cada coluna corresponde a um STR específico.

    name,AGAT,AATG,TATC
    Alice,28,42,14
    Bob,17,22,19
    Charlie,36,18,25

Os dados do arquivo acima sugeririam que Alice tem a sequência `AGAT` repetida 28 vezes consecutivamente em algum lugar de seu DNA, a sequência `AATG` repetida 42 vezes e `TATC` repetida 14 vezes. Bob, por sua vez, tem os mesmos três STRs repetidos 17, 22 e 19 vezes, respectivamente. E Charlie tem os mesmos três STRs repetidos 36, 18 e 25 vezes, respectivamente.

Então, dada uma sequência de DNA, como você poderia identificar a quem ela pertence? Bem, imagine que você procurou na sequência de DNA a sequência consecutiva mais longa de `AGAT`s repetidos e descobriu que a sequência mais longa tem 17 repetições. Se você então descobrisse que a sequência mais longa de `AATG` tem 22 repetições e a sequência mais longa de `TATC` tem 19 repetições, isso forneceria uma evidência bastante boa de que o DNA pertence a Bob. Claro, é também possível que, uma vez que você tenha as contagens para cada um dos STRs, ela não coincida com ninguém em seu banco de dados de DNA, nesse caso, não haveria correspondência.

Na prática, como os analistas sabem em qual cromossomo e em qual localização do DNA um STR será encontrado, eles podem localizar sua busca apenas em uma seção estreita de DNA. Mas ignoraremos esse detalhe para este problema.

Sua tarefa é escrever um programa que aceite uma sequência de DNA e um arquivo CSV contendo contagens de STR para uma lista de indivíduos e, em seguida, produza a quem pertence esse DNA (provavelmente).