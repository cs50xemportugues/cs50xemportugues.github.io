# C$50 Finance

<div class="alert" data-alert="warning" role="alert"><p>O código de distribuição desse conjunto de problemas foi recentemente alterado. Se você baixou o código de distribuição antes de <a data-local="2022-12-01T00:00:00+00:00" href="https://time.cs50.io/20221201T000000Z">2022-12-01T00:00:00+00:00</a>, execute os seguintes comandos no terminal no diretório <code class="language-plaintext highlighter-rouge">finance</code> para baixar a última versão do código de distribuição.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ rm helpers.py
$ wget https://cdn.cs50.net/2022/fall/psets/9/finance/helpers.py

</code></pre></div></div></div>

Implemente um site através do qual os usuários possam "comprar" e "vender" ações, como abaixo.

![C$50 Finance](https://cs50.harvard.edu/x/2023/psets/9/finance/finance.png)

## Contexto

Se você não tem certeza do que significa comprar e vender ações (ou seja, ações de uma empresa), vá [aqui](https://www.investopedia.com/articles/basics/06/invest1000.asp) para um tutorial.

Você está prestes a implementar o C$50 Finance, um aplicativo web através do qual você pode gerenciar portfólios de ações. Essa ferramenta não só permitirá que você verifique os preços reais das ações e os valores de portfólio, mas também permitirá que você compre (ok, "compre") e venda (ok, "venda") ações pesquisando [IEX](https://iextrading.com/developer/) para os preços das ações.

De fato, a IEX permite que você baixe cotações de ações por meio de sua API (interface de programação de aplicativos) usando URLs como `https://api.iex.cloud/v1/data/core/quote/nflx?token=API_KEY`. Observe como o símbolo da Netflix (NFLX) está incorporado a este URL; é assim que a IEX sabe de quem dados retornar. Esse link não retornará nenhum dado porque a IEX exige que você use uma chave API (mais sobre isso daqui a pouco), mas se retornasse, você veria uma resposta no formato JSON (JavaScript Object Notation) como este:

    {
      "avgTotalVolume": 15918066,
      "calculationPrice": "close",
      "change": -8.27,
      "changePercent": -0.03074,
      "close": 260.79,
      "closeSource": "official",
      "closeTime": 1667592000924,
      "companyName": "Netflix Inc.",
      "currency": "USD",
      "delayedPrice": 260.81,
      "delayedPriceTime": 1667591988947,
      "extendedChange": 0.21,
      "extendedChangePercent": 0.00081,
      "extendedPrice": 261,
      "extendedPriceTime": 1667606392772,
      "high": 274.97,
      "highSource": "15 minute delayed price",
      "highTime": 1667592000831,
      "iexAskPrice": None,
      "iexAskSize": None,
      "iexBidPrice": None,
      "iexBidSize": None,
      "iexClose": 260.85,
      "iexCloseTime": 1667591999754,
      "iexLastUpdated": None,
      "iexMarketPercent": None,
      "iexOpen": 271.67,
      "iexOpenTime": 1667568602197,
      "iexRealtimePrice": None,
      "iexRealtimeSize": None,
      "iexVolume": None,
      "lastTradeTime": 1667591999820,
      "latestPrice": 260.79,
      "latestSource": "Close",
      "latestTime": "Nov 4, 2022",
      "latestUpdate": 1667592000924,
      "latestVolume": 11124694,
      "low": 255.32,
      "lowSource": "15 minute delayed price",
      "lowTime": 1667584872696,
      "marketCap": 115215720136,
      "oddLotDelayedPrice": 260.81,
      "oddLotDelayedPriceTime": 1667591988947,
      "open": 271.9,
      "openTime": 1667568601785,
      "openSource": "official",
      "peRatio": 23.39,
      "previousClose": 269.06,
      "previousVolume": 7057350,
      "primaryExchange": "NASDAQ",
      "symbol": "NFLX",
      "volume": 11124694,
      "week52High": 700.99,
      "week52Low": 162.71,
      "ytdChange": -0.5978504176349512,
      "isUSMarketOpen": false
    }

Observe como, entre as chaves, há uma lista separada por vírgulas de pares chave-valor, com dois pontos separando cada chave de seu valor.

Vamos agora direcionar nossa atenção para obter o código de distribuição deste problema!