Detalhes da implementação
----------------------

Complete a implementação do `tournament.py`, de modo que simule vários torneios e mostre a probabilidade de vitória de cada equipe.

Primeiro, em `main`, leia os dados da equipe a partir do arquivo CSV para a memória do seu programa, e adicione cada equipe na lista `teams`.

*   O arquivo a ser usado será fornecido como argumento da linha de comando. Você pode acessar o nome do arquivo com `sys.argv[1]`.
*   Lembre-se que você pode abrir um arquivo com `open(filename)`, em que `filename` é uma variável que armazena o nome do arquivo.
*   Depois de ter um arquivo `f`, use `csv.DictReader(f)` para criar um "leitor": um objeto em Python que pode ser utilizado em um loop para ler o arquivo, uma linha de cada vez, tratando cada linha como um dicionário.
*   Por padrão, todos os valores lidos do arquivo serão strings. Por isso, certifique-se de converter o `rating` da equipe em um `int` (você pode usar a função `int` do Python para isso).
*   Por fim, adicione cada dicionário de equipe em `teams`. A chamada de função `teams.append (x)` adicionará `x` na lista de equipes `teams`.
*   Lembre-se que cada equipe deve ser um dicionário com o nome da `equipe` e um `rating`.

Em seguida, implemente a função `simulate_tournament`. Esta função deve aceitar como entrada uma lista de equipes e deve simular repetidamente as rodadas até restar apenas uma equipe. A função deve retornar o nome desta equipe.

*   Você pode chamar a função `simulate_round`, que simula uma única rodada, aceitando uma lista de equipes como entrada e retornando uma lista com todos os vencedores.
*   Lembre-se que se `x` é uma lista, você pode usar `len(x)` para determinar o comprimento da lista.
*   Não se deve assumir o número de equipes no torneio, embora possa ser assumido que seja uma potência de 2.

Finalmente, na função `main`, execute `N` simulações de torneio, e mantenha o controle de quantas vezes cada equipe vence na contagem de dicionários `counts`.

*   Por exemplo, se o Uruguai venceu 2 torneios e Portugal venceu 3 torneios, então seu dicionário `counts` deve ser `{"Uruguai": 2, "Portugal": 3}`.
*   Você deve usar sua função `simulate_tournament` para simular cada torneio e determinar o vencedor.
*   Lembre-se que, se `counts` é um dicionário, a sintaxe como `counts [nome_da_equipe] = x` associará a chave armazenada em `nome_da_equipe` com o valor armazenado em `x`.
*   Pode-se usar a palavra-chave `in` em Python para verificar se um dicionário já tem uma chave específica. Por exemplo,`if "Portugal" in counts:` verificará se `"Portugal"` já tem um valor existente no dicionário `counts`.