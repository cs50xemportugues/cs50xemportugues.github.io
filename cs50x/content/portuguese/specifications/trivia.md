Laboratório 8: Trivia
=============

Você pode colaborar com um ou dois colegas neste laboratório, embora seja esperado que cada aluno em qualquer grupo contribua igualmente para o laboratório.

Escreva uma página da web que permita aos usuários responder perguntas de trivia.

![captura de tela de perguntas de trivia](https://cs50.harvard.edu/x/2023/labs/8/questions.png)

Introdução
---------------

Começou o CS50x em 2021 ou antes e precisa migrar seu trabalho do CS50 IDE para o novo espaço de código VS? Certifique-se de verificar nossas instruções sobre como [migrar](../../new/) seus arquivos!

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da janela do terminal e, em seguida, execute `cd` sozinho. Verifique se sua "marcação" é semelhante à abaixo.

    $
    

Clique dentro da janela do terminal e, em seguida, execute

    wget https://cdn.cs50.net/2022/fall/labs/8/trivia.zip
    

seguido de Enter para baixar um arquivo ZIP chamado `trivia.zip` no seu space de código. Tome cuidado para não ignorar o espaço entre `wget` e a seguinte URL, ou qualquer outro caractere!

Agora, execute

    unzip trivia.zip
    

para criar uma pasta chamada `trivia`. Você não precisa mais do arquivo ZIP, então execute

    rm trivia.zip
    

e responda com "y", seguido de Enter na solicitação para remover o arquivo ZIP que você baixou.

Agora digite

    cd trivia
    

seguido de Enter para mover-se para (ou seja, abrir) esse diretório. Seu prompt deve agora se parecer com o abaixo.

    trivia/ $
    

Se tudo correu bem, você deve executar

    ls
    

e deverá ver um arquivo `index.html` e um arquivo `styles.css`.

Se você tiver algum problema, siga essas mesmas etapas novamente e veja se pode determinar onde errou!

Detalhes de implementação
----------------------

Projete uma página da web usando HTML, CSS e JavaScript para permitir que os usuários respondam a perguntas de trivia.

* Em `index.html`, adicione abaixo de "Parte 1" uma pergunta de trivia de múltipla escolha de sua escolha com HTML.
      * Você deve usar um cabeçalho `h3` para o texto de sua pergunta.
      * Você deve ter um `botão` para cada uma das possíveis opções de resposta. Deve haver pelo menos três opções de resposta, das quais exatamente uma deve ser correta.
* Usando JavaScript, adicione lógica para que os botões mudem de cor quando um usuário clicar neles.
      * Se um usuário clicar em um botão com uma resposta incorreta, o botão deve ficar vermelho e texto deve aparecer abaixo da pergunta que diz "Incorreto".
      * Se um usuário clicar em um botão com a resposta correta, o botão deve ficar verde e texto deve aparecer abaixo da pergunta que diz "Correto!”.
* Em `index.html`, adicione abaixo de "Parte 2" uma pergunta de resposta livre baseada em texto de sua escolha com HTML.
      * Você deve usar um cabeçalho `h3` para o texto da sua pergunta.
      * Você deve usar um campo `input` para permitir que o usuário digite uma resposta.
      * Você deve usar um `botão` para permitir que o usuário confirme sua resposta.
* Usando JavaScript, adicione lógica para que o campo de texto mude de cor quando um usuário confirmar sua resposta.
      * Se o usuário digitar uma resposta incorreta e pressionar o botão de confirmação, o campo de texto deve ficar vermelho e o texto deve aparecer abaixo da pergunta que diz "Incorreto".
      * Se o usuário digitar a resposta correta e pressionar o botão de confirmação, o campo de entrada deve ficar verde e o texto deve aparecer abaixo da pergunta que diz "Correto!".

Opcionalmente, você também pode:

* Editar `styles.css` para alterar o CSS da sua página da web!
* Adicione perguntas de trivia adicionais ao seu questionário de trivia, se desejar!

### Passo a passo

Este vídeo foi gravado quando o curso ainda usava o CS50 IDE para escrever código. Embora a interface possa parecer diferente do seu space de código, o comportamento dos dois ambientes deve ser bastante semelhante!

### Dicas

* Use [`document.querySelector`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) para consultar um único elemento HTML.
* Use [`document.querySelectorAll`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll) para consultar vários elementos HTML que correspondem a uma consulta. A função retorna uma matriz de todos os elementos correspondentes.

Não sabe como resolver?

### Testando

Não há `check50` para este laboratório, já que as implementações variam com base em suas perguntas! Mas verifique tanto as respostas incorretas quanto as corretas para cada uma de suas perguntas para garantir que sua página da web responda adequadamente.

Execute `http-server` em seu terminal enquanto estiver em seu diretório `lab8` para iniciar um servidor da web que serve sua página da web.

Como enviar
-------------

Em seu terminal, execute o abaixo para enviar seu trabalho.

    submit50 cs50/labs/2023/x/trivia"