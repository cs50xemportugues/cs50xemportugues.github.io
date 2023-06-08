## Especificação

### `register`

Complete a implementação do `register` de tal forma que permita que um usuário faça o registro de uma conta através de um formulário.

- Exija que o usuário insira um nome de usuário, implementado como um campo de texto cujo o `name` é `username`. Renderize um pedido de desculpas se o usuário deixar o campo em branco ou se o nome de usuário já existir.
- Exija que o usuário insira uma senha, implementado como um campo de texto cujo o `name` é `password`, e depois que repita a mesma senha, implementado como um campo de texto cujo o `name` é `confirmation`. Renderize um pedido de desculpas se qualquer um dos campos estiver em branco ou se as senhas não correspondem.
- Submeta o input do usuário via `POST` para `/register`.
- Insira o novo usuário em `users`, armazenando o hash da senha do usuário, e não a senha em si. Hasheie a senha do usuário com [`generate_password_hash`](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#werkzeug.security.generate_password_hash). É bem provável que você irá precisar criar um template novo (e.g., `register.html`) que seja bem similar ao `login.html`.

Após implementar o `register` corretamente, você deverá ser capaz de registrar uma conta e fazer login (já que `login` e `logout` já funcionam)! E você deverá ser capaz de ver as suas linhas via phpLiteAdmin ou `sqlite3`.

### `quote`

Complete a implementação de `quote` de tal forma que permita que um usuário pesquise o preço atual de uma ação.

- Exija que o usuário insira o símbolo da ação, implementado como um campo de texto cujo o `name` é `symbol`.
- Submeta o input do usuário via `POST` para `/quote`.
- É bem provável que você irá precisar criar dois templates novos (e.g., `quote.html` e `quoted.html`). Quando o usuário visitar `/quote` via GET, renderize um desses templates, dentro dele deverá existir um formulário HTML que será submetido à `/quote` via POST. Em resposta ao POST, `quote` pode renderizar o segundo template, incorporando um ou mais valores de `lookup`.

### `buy`

Complete a implementação do `buy` de tal forma que permita que um usuário compre ações.

- Exija que o usuário insira o símbolo da ação, implementado como um campo de texto cujo o `name` é `symbol`. Renderize um pedido de desculpas se o campo estiver em branco ou se o símbolo não existir (de acordo com o valor de retorno de `lookup`).
- Exija que o usuário insira um número de ações, implementado como um campo de texto cujo o `name` é `shares`. Renderize um pedido de desculpas se o input não for um inteiro positivo.
- Submeta o input do usuário via `POST` para `/buy`.
- Após conclusão, redirecione o usuário para a página principal.
- É bem provável que você irá precisar chamara o `lookup` para buscar o preço atual de uma ação.
- É bem provável que você irá precisar fazer uma `SELECT` para descobrir quanto de dinheiro o usuário tem em `users`.
- Adicione uma ou mais tabelas novas ao `finance.db` por onde possa rastrear a compra. Armazene informação suficiente para saber quem comprou, o quê comprou, por qual preço e quando.
  - Utilize tipos SQLite apropriados.
  - Defina índices `UNIQUE` em campos que precisarem ser únicos.
  - Defina índices (não-`UNIQUE`) em campos pelos quais você irá realizar pesquisas (por exemplo, via `SELECT` com `WHERE`).
- Renderize um pedido de desculpas, sem completar a compra, caso o usuário não consiga pagar pelo número de ações no preço atual.
- Você não precisa se preocupar com condições de corrida (ou utilizar transações).

Após implementar o `buy` corretamente, você deverá ser capaz de ver as compras dos usuários em sua(s) nova(s) tabela(s) via phpLiteAdmin ou `sqlite3`.