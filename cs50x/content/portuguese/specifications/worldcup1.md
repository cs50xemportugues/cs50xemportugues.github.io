Laboratório 6: Copa do Mundo
================

Você pode colaborar com um ou dois colegas neste laboratório, mas é esperado que todos os alunos em tal grupo contribuam igualmente para o laboratório.

Escreva um programa para executar simulações da Copa do Mundo da FIFA.

    $ python tournament.py 2018m.csv
    Bélgica: 20,9% de chance de ganhar
    Brasil: 20,3% de chance de ganhar
    Portugal: 14,5% de chance de ganhar
    Espanha: 13,6% de chance de ganhar
    Suíça: 10,5% de chance de ganhar
    Argentina: 6,5% de chance de ganhar
    Inglaterra: 3,7% de chance de ganhar
    França: 3,3% de chance de ganhar
    Dinamarca: 2,2% de chance de ganhar
    Croácia: 2,0% de chance de ganhar
    Colômbia: 1,8% de chance de ganhar
    Suécia: 0,5% de chance de ganhar
    Uruguai: 0,1% de chance de ganhar
    México: 0,1% de chance de ganhar
    

Contexto
----------

Na Copa do Mundo de futebol, a fase eliminatória é composta por 16 equipes. Em cada rodada, cada equipe joga contra outra equipe e as equipes que perdem são eliminadas. Quando restam apenas duas equipes, a equipe vencedora da partida final é campeã.

No futebol, as equipes recebem [FIFA Ratings] (https://en.wikipedia.org/wiki/FIFA_World_Rankings#Current_calculation_method), que são valores numéricos que representam o nível de habilidade relativa de cada equipe. FIFA Ratings mais altos indicam melhores resultados de jogos anteriores e, dado os FIFA Ratings de duas equipes, é possível estimar a probabilidade de que qualquer equipe vença um jogo com base em suas classificações atuais. As FIFA Ratings de duas Copas do Mundo anteriores estão disponíveis como o [May 2018 Men’s FIFA Ratings] e [March 2019 Women’s FIFA Ratings].

Usando essa informação, podemos simular todo o torneio, simulando repetidamente as rodadas até que reste apenas uma equipe. E se quisermos estimar a probabilidade de que qualquer equipe dada vença o torneio, podemos simular o torneio muitas vezes (por exemplo, 1000 simulações) e contar quantas vezes cada equipe ganha um torneio simulado. 1000 simulações podem parecer muitas, mas com o poder de computação de hoje podemos realizar essas simulações em questão de milissegundos. No final deste laboratório, experimentaremos o quão valioso pode ser aumentar o número de simulações que executamos, dada a troca de tempo de execução.

Sua tarefa neste laboratório é fazer isso usando Python!