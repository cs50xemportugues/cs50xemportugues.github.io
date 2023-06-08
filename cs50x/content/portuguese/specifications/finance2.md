## Começando

Faça login em [code.cs50.io](https://code.cs50.io/), clique na sua janela de terminal e execute `cd` por si só. Você deverá ver que o prompt da sua janela de terminal se parece com o abaixo:

     $

Em seguida, execute

    wget https://cdn.cs50.net/2022/fall/psets/9/finance.zip

para baixar um ZIP chamado `finance.zip` para o seu espaço de códigos.

Depois execute

     unzip finance.zip

para criar uma pasta chamada `finance`. Você não precisa mais do arquivo ZIP, por isso você pode executar

     rm finance.zip

e responda com "y" seguido de Enter para remover o arquivo ZIP que você baixou.

Agora digite

    cd finance

seguido de Enter para se mover para dentro (ou seja, abrir) desse diretório. Seu prompt deverá se parecer com o abaixo.

    finance/ $

Execute `ls` por si só e você deverá ver alguns arquivos e pastas:

    app.py  finance.db  helpers.py  requirements.txt  static/  templates/

Se você tiver algum problema, siga essas mesmas etapas novamente e veja se você pode determinar onde errou!

### Configurando

Antes de começar nesta tarefa, você precisará se registrar em uma chave de API para poder consultar os dados da IEX. Para fazer isso, siga estas etapas:

- Visite [iexcloud.io/cloud-login#/register/](https://iexcloud.io/cloud-login#/register/).
- Selecione o tipo de conta “Individual”, insira seu nome, endereço de e-mail e uma senha e clique em "Criar conta".
- Depois de registrada, role para baixo até “Comece de graça” e clique em “Selecionar plano inicial” para escolher o plano gratuito. _Observe que este plano só funciona por 30 dias a partir do dia em que você cria sua conta._ Mantenha isso em mente se você pretende usar esta mesma API para o seu projeto final!
- Depois de confirmar sua conta por meio de um email de confirmação, visite [https://iexcloud.io/console/tokens](https://iexcloud.io/console/tokens).
- Copie a chave que aparece na coluna _Token_ (deve começar com `pk_`).
- Na sua janela de terminal, execute:

<pre>
$ export API_KEY=value
</pre>

onde `value` é o valor colado, sem nenhum espaço imediatamente antes ou depois do `=`. Você também pode querer colar esse valor em um documento de texto em algum lugar, caso precise dele novamente mais tarde.