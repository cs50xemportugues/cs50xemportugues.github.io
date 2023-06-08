# C$50 Finance

<div class="alert" data-alert="warning" role="alert">
    <p>Le code de distribution de cet ensemble de problèmes a récemment été modifié. Si vous avez téléchargé le code de distribution avant le <a data-local="2022-12-01T00:00:00+00:00" href="https://time.cs50.io/20221201T000000Z">1er décembre 2022 à 00:00:00 UTC</a>, exécutez les commandes terminales suivantes dans votre répertoire <code class="language-plaintext highlighter-rouge">finance</code> pour télécharger la dernière version du code de distribution.</p>
 
 <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ rm helpers.py
 $ wget https://cdn.cs50.net/2022/fall/psets/9/finance/helpers.py
 </code></pre></div></div>
</div>


Implémentez un site web via lequel les utilisateurs peuvent "acheter" et "vendre" des actions, de la même manière que ci-dessous.

![C$50 Finance](https://cs50.harvard.edu/x/2023/psets/9/finance/finance.png)

## Contexte

Si vous n'êtes pas tout à fait sûr de ce que cela signifie d'acheter et de vendre des actions (c'est-à-dire des actions d'une entreprise), rendez-vous [ici](https://www.investopedia.com/articles/basics/06/invest1000.asp) pour un tutoriel.

Vous êtes sur le point de mettre en œuvre C$50 Finance, une application web via laquelle vous pouvez gérer des portefeuilles d'actions. Non seulement cet outil vous permettra de vérifier les cours réels des actions et les valeurs des portefeuilles, mais il vous permettra également d'acheter (ok, "acheter") et de vendre (ok, "vendre") des actions en interrogeant [IEX](https://iextrading.com/developer/) pour connaître les prix des actions.

En effet, IEX vous permet de télécharger les citations d'actions via leur API (interface de programmation d'applications) en utilisant des URL comme `https://api.iex.cloud/v1/data/core/quote/nflx?token=API_KEY`. Remarquez comment le symbole Netflix (NFLX) est intégré dans cette URL ; c'est ainsi que IEX sait de quelles données il s'agit. Ce lien ne renverra en réalité aucune donnée car IEX vous demande d'utiliser une clé API (nous en parlerons un peu plus loin), mais si tel était le cas, vous verriez une réponse au format JSON (JavaScript Object Notation) comme celle-ci :

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
      "highSource": "cours retardé de 15 minutes",
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
      "latestSource": "Clôturer",
      "latestTime": "4 novembre 2022",
      "latestUpdate": 1667592000924,
      "latestVolume": 11124694,
      "low": 255.32,
      "lowSource": "cours retardé de 15 minutes",
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
      "isUSMarketOpen": False
    }

Remarquez comment, entre les accolades, il y a une liste de paires clé-valeur séparées par des virgules, avec deux points séparant chaque clé de sa valeur.

Tournons maintenant notre attention vers l'obtention du code de distribution de ce problème !