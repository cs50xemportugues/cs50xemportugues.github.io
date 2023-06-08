## Passo a Passo


<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/7wPTAwT-6bA?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


## Testes

Certifique-se de testar manualmente o seu aplicativo da web, por exemplo:

- registrando um novo usuário e verificando se sua página de portfólio carrega com as informações corretas,
- solicitando uma cotação usando um símbolo de ações válido,
- comprando uma ação várias vezes, verificando se o portfólio exibe totais corretos,
- vendendo tudo ou parte de uma ação, verificando novamente o portfólio, e
- verificando se a página de histórico mostra todas as transações para o usuário que está logado.

Também teste alguns usos inesperados, por exemplo:

- inserindo cadeias alfabéticas em formulários quando apenas números são esperados,
- inserindo números zero ou negativos em formulários quando apenas números positivos são esperados,
- inserindo valores de ponto flutuante em formulários quando apenas inteiros são esperados,
- tentando gastar mais dinheiro do que um usuário tem,
- tentando vender mais ações do que um usuário tem,
- inserindo um símbolo de ação inválido e
- incluindo caracteres potencialmente perigosos como `'` e `;` em consultas SQL.

Uma vez satisfeito, para testar seu código com `check50`, execute o seguinte.

    check50 cs50/problems/2023/x/finance

<div class="alert" data-alert="warning" role="alert"><p>Esteja ciente de que <code class="language-plaintext highlighter-rouge">check50</code> testará todo o seu programa como um todo. Se você executá-lo <strong>antes</strong> de concluir todas as funções necessárias, ele poderá relatar erros em funções que estão corretas, mas dependem de outras funções.</p></div>


Execute o seguinte para avaliar o estilo de seus arquivos Python usando `style50`.

    style50 *.py

## Solução da Equipe

Você pode estilizar seu próprio aplicativo de forma diferente, mas aqui está como é a solução da equipe!

[https://finance.cs50.net/](https://finance.cs50.net/)

Sinta-se à vontade para criar uma conta e mexer no aplicativo. Não use uma senha que você use em outros sites.

É **razoável** olhar o HTML e CSS da equipe.