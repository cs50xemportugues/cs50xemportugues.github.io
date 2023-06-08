## Sugestões

- Para formatar um valor como valor de dólar americano (com centavos listados com duas casas decimais), você pode usar o filtro 'usd' em seus modelos Jinja (imprimindo valores como `{{ valor | usd }}` em vez de `{{ valor }}`) .
- Dentro de `cs50.SQL` existe um método `execute`, cujo primeiro argumento deve ser uma `str` de SQL. Se essa `str` contiver parâmetros de ponto de interrogação aos quais os valores devem ser vinculados, esses valores podem ser fornecidos como parâmetros nomeados adicionais para `execute`. Veja a implementação de `login` para um exemplo desses. O valor de retorno de `execute` é o seguinte:

   - Se a `str` for um `SELECT`, então `execute` retorna uma lista de zero ou mais objetos `dict`, dentro dos quais existem chaves e valores representando os campos e células de uma tabela, respectivamente.
   - Se a `str` for um `INSERT`, e a tabela na qual os dados foram inseridos contiver uma `PRIMARY KEY` autoincrementável, então `execute` retorna o valor da chave primária da linha recém-inserida.
   - Se a `str` for um `DELETE` ou um `UPDATE`, então `execute` retorna o número de linhas excluídas ou atualizadas por `str`.

- Lembre-se de que `cs50.SQL` registrará em sua janela de terminal quaisquer consultas que você executar por meio de `execute` (para que você possa confirmar se elas estão como pretendido).
- Certifique-se de usar parâmetros vinculados a ponto de interrogação (ou seja, um [paramstyle](https://www.python.org/dev/peps/pep-0249/#paramstyle) de `named`) ao chamar o método `execute` do CS50, como` WHERE?`. Não use f-string, [`format`](https://docs.python.org/3.6/library/functions.html#format) ou `+` (ou seja, concatenação), para não correr o risco de sofrer um ataque de injeção SQL.
- Se (e somente se) já se sentir confortável com o SQL, você pode utilizar o [SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/index.html) ou o [Flask-SQLAlchemy](https://flask-sqlalchemy.pocoo.org/) (ou seja, [SQLAlchemy ORM] (https://docs.sqlalchemy.org/en/latest/index.html)) em vez do `cs50.SQL`.
- Você pode adicionar arquivos estáticos adicionais a `static /`.
- É provável que você deseje consultar a documentação do [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) ao implementar seus modelos.
- É **razoável** pedir a outras pessoas para experimentar (e tentar provocar erros em) seu site.
- Você é bem-vindo para alterar a estética do site, como através de
  - [bootswatch.com] (https://bootswatch.com/),
  - [getbootstrap.com/docs/5.1/content] (https://getbootstrap.com/docs/5.1/content/),
  - [getbootstrap.com/docs/5.1/components] (https://getbootstrap.com/docs/5.1/components/) e / ou
  - [memegen.link] (https://memegen.link/).
- Você pode achar a documentação do [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) e do [Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/) úteis!

## Perguntas frequentes

### ImportError: No module named ‘application’

Por padrão, o `flask` procura um arquivo chamado `app.py` em seu diretório de trabalho atual (porque configuramos o valor de` FLASK_APP`, uma variável de ambiente, para ser `app.py`). Se você vir esse erro, provavelmente executou o `flask` no diretório errado!

### OSError: \ [Errno 98 \] Endereço já em uso

Se, ao executar o `flask`, você vir este erro, é provável que você (ainda) tenha o `flask` em execução em outra guia. Certifique-se de interromper esse outro processo, como com ctrl-c, antes de iniciar o `flask` novamente. Se você não tiver nenhuma outra guia, execute `fuser -k 8080/tcp` para encerrar os processos que ainda estão ouvindo na porta TCP 8080.

## Como enviar

Em seu terminal, execute o que segue para enviar seu trabalho.

    submit50 cs50/problems/2023/x/finance
"