### `índice`

Complete a implementação do `índice` de forma a exibir uma tabela HTML que resume as ações que o usuário atualmente logado possui. A tabela deve apresentar o número total de ações possuídas pelo usuário, o preço atual de cada ação, o valor total de cada ação (ou seja, quantidade de ações vezes o preço) e o saldo atual em dinheiro do usuário. Apresente também o valor total do portfólio do usuário (valor total das ações mais saldo em dinheiro).

- É provável que seja necessário executar múltiplas consultas SELECT. Dependendo de como as tabelas são implementadas, pode ser interessante o uso de [GROUP BY](https://www.google.com/search?q=SQLite+GROUP+BY), [HAVING](https://www.google.com/search?q=SQLite+HAVING), [SUM](https://www.google.com/search?q=SQLite+SUM) e/ou [WHERE](https://www.google.com/search?q=SQLite+WHERE).
- É provável que seja necessário chamar a função `lookup` para cada ação.

### `venda`

Complete a implementação da `venda` de forma a permitir que o usuário venda as ações que possui.

- É preciso exigir que o usuário insira o símbolo da ação que deseja vender, que deve ser apresentado como um selecionador (`select`) com `name` igual a "symbol". Apresente uma mensagem de erro caso o usuário não selecione uma ação ou não possua ações dessa ação.
- Também é preciso exigir que o usuário informe a quantidade de ações que deseja vender, que deve ser apresentada como um campo de texto (`text`) com `name` igual a "shares". Apresente uma mensagem de erro caso o valor inserido não seja um número inteiro positivo ou caso o usuário não possua a quantidade selecionada de ações daquela ação.
- Os dados do usuário devem ser enviados via `POST` para `/sell`.
- Após a conclusão da transação, o usuário deve ser redirecionado para a página principal.
- Não é necessário se preocupar com condições especiais devido a múltiplos acessos simultâneos (ou usar transações).

### `histórico`

Complete a implementação da `histórico` de forma a exibir uma tabela HTML que resume todas as transações de um usuário. A tabela deve listar, linha por linha, todas as compras e vendas realizadas pelo usuário.

- Para cada linha, deve ficar claro se a ação foi comprada ou vendida, deve ser incluído o símbolo da ação, o preço de compra/venda, a quantidade de ações compradas/vendidas e a data/hora em que a transação foi efetuada.
- Pode ser necessário alterar a tabela criada para a implementação da `compra` ou complementá-la com uma tabela adicional. Tente minimizar redundâncias.

### Personalização

Implemente, no mínimo, uma personalização à sua escolha:

- Permita que os usuários alterem suas senhas.
- Permita que os usuários adicionem mais dinheiro em sua conta.
- Permita que os usuários comprem mais ações ou vendam ações que já possuem diretamente pelo `índice`, sem precisar escrever o símbolo da ação manualmente.
- Exija que as senhas dos usuários contenham um número mínimo de letras, números e/ou símbolos.
- Implemente outra funcionalidade de escopo comparável.