#### `helpers.py`

Em seguida, dê uma olhada no arquivo `helpers.py`. Ah, lá está a implementação do `apology`. Note como ele, em última instância, renderiza um modelo, o `apology.html`. Ele também define, dentro de si mesmo, outra função, `escape`, que é simplesmente usada para substituir caracteres especiais em desculpas. Definindo `escape` dentro de `apology`, limitamos o seu escopo apenas a este último; nenhuma outra função poderá chamar (ou precisará chamar) essa função.

Em seguida, no arquivo, há o `login_required`. Sem problemas se este for um pouco criptico para você, mas se você já se perguntou como uma função pode retornar outra função, aqui está um exemplo!

Em seguida, temos o `lookup`, uma função que, dada um símbolo (por exemplo, NFLX), retorna uma cotação de ações para uma determinada empresa na forma de um dicionário com três chaves: `name`, cujo valor é uma `str`, o nome da empresa; `price`, cujo valor é um `float` e `symbol`, cujo valor é uma `str`, uma versão canônica (em maiúsculas) do símbolo da ação, independentemente de como esse símbolo foi capitalizado quando passado para `lookup`.

Finalmente, no final do arquivo, temos a função `usd`, uma pequena função que simplesmente formata um número do tipo `float` como USD (por exemplo, `1234.56` é formatado como `$ 1,234.56`).

#### `requirements.txt`

Em seguida, dê uma rápida olhada em `requirements.txt`. Esse arquivo simplesmente fornece as dependências de pacotes necessárias para a aplicação.

#### `static/`

Olhe também para a pasta `static/`, onde se encontra o arquivo `styles.css`. Ali está onde fica o CSS inicial. Você pode alterá-lo como achar melhor.

#### `templates/`

Agora, dê uma olhada na pasta de templates `templates/`. No arquivo `login.html`, essencialmente, há apenas um formulário HTML, estilizado com [Bootstrap](https://getbootstrap.com/). Já em `apology.html`, há um modelo para um pedido de desculpas. Lembre-se de que o `apology` em `helpers.py` tem dois argumentos: `message`, que foi passado para `render_template` como o valor de `bottom`, e, opcionalmente, `code`, que foi passado para `render_template` como o valor de `top`. Veja como esses valores são usados ​​no arquivo `apology.html`! E [aqui está o porquê](https://github.com/jacebrowning/memegen) 0:-)

Por fim, temos o arquivo `layout.html`. Ele é um pouco maior do que o usual, mas isso ocorre principalmente porque ele vem com uma barra de navegação móvel-chique, baseada no Bootstrap. Observe como ele define um bloco chamado `main`, dentro de qual os modelos (incluindo `apology.html` e` login.html`) devem ser incluídos. Ele também inclui suporte para o recurso de mensagens intermitentes do Flask [message flashing](https://flask.palletsprojects.com/en/1.1.x/quickstart/#message-flashing), para que você possa passar mensagens de uma rota para outra para o usuário ver.