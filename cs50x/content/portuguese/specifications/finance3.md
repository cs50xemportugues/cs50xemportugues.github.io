### Execução

Inicie o servidor web incorporado do Flask (dentro do diretório `finance/`):

    $ flask run

Visite a URL retornada pelo `flask` para ver o código de distribuição em ação. No entanto, ainda não é possível fazer login ou se registrar!

Dentro do diretório `finance/`, execute `sqlite3 finance.db` para abrir o arquivo `finance.db` com o `sqlite3`. Se você executar o comando `.schema` no prompt do SQLite, notará que `finance.db` vem com uma tabela chamada `users`. Dê uma olhada na estrutura (ou seja, esquema) dela. Note que, por padrão, novos usuários receberão $ 10.000 em dinheiro. Mas se você executar `SELECT * FROM users;`, ainda não haverá (ou seja, linhas) nenhum usuário para navegar.

Outra maneira de visualizar `finance.db` é com um programa chamado phpLiteAdmin. Clique em `finance.db` no navegador de arquivos do seu espaço de codificação e, em seguida, clique no link mostrado abaixo do texto “Please visit the following link to authorize GitHub Preview”. Você deve ver informações sobre o banco de dados em si, bem como uma tabela, `users`, assim como você viu no prompt `sqlite3` com `.schema`.

### Compreensão

#### `app.py`

Abra o arquivo `app.py`. No topo do arquivo, há um monte de importações, entre elas o módulo SQL da CS50 e algumas funções auxiliares. Mais sobre isso em breve.

Após configurar o [Flask](https://flask.pocoo.org/), note como este arquivo desativa o cache de respostas (desde que esteja no modo de depuração, que é o caso por padrão no seu espaço de codificação do code50), para evitar o caso de fazer uma alteração em algum arquivo, mas o navegador não perceber. Observe a seguir como ele configura o [Jinja](https://jinja.pocoo.org/) com um “filtro” personalizado, `usd`, uma função (definida em `helpers.py`) que facilitará a formatação dos valores como dólares americanos (USD). Em seguida, ele configura ainda mais o Flask para armazenar [sessões](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions) no sistema de arquivos local (ou seja, disco) em vez de armazená-los dentro de cookies (assinados digitalmente), que é o padrão do Flask. O arquivo, em seguida, configura o módulo SQL da CS50 para usar `finance.db`.

Depois disso, há um monte de rotas, apenas duas das quais estão totalmente implementadas: `login` e `logout`. Leia a implementação do `login` primeiro. Observe como ele usa o `db.execute` (da biblioteca CS50) para consultar o `finance.db`. E observe como ele usa o `check_password_hash` para comparar os hashes das senhas dos usuários. Observe também como o `login` “lembra” que um usuário está logado, armazenando seu `user_id`, um INTEIRO, na `session`. Dessa forma, qualquer rota deste arquivo pode verificar qual usuário, se houver algum, está logado. Por fim, observe como, uma vez que o usuário tenha feito login com sucesso, o `login` redirecionará para `"/"`, levando o usuário à sua página inicial. Enquanto isso, observe como o `logout` simplesmente limpa a `session`, efetivamente fazendo logout do usuário.

Observe como a maioria das rotas é “decorada” com `@ login_required` (uma função definida em `helpers.py` também). Esse decorador garante que, se um usuário tentar visitar qualquer uma dessas rotas, ele ou ela será redirecionado primeiro para `login` para fazer login.

Observe também como a maioria das rotas suporta GET e POST. Mesmo assim, a maioria deles (por enquanto!) simplesmente retorna um "pedido de desculpas", uma vez que eles ainda não foram implementados.