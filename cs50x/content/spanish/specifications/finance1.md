# Finanzas de C$50

<div class = "alert" data-alert = "warning" role = "alert"> <p> El código de distribución de este conjunto de problemas ha cambiado recientemente. Si descargó el código de distribución antes del<a data-local="2022-12-01T00:00:00+00:00" href="https://time.cs50.io/20221201T000000Z"> 2022-12-01T00:00:00+00:00 </a>, ejecute los siguientes comandos del terminal en su directorio de <code class = "language-plaintext highlighter-rouge "> finanzas </code> para descargar la última versión del código de distribución.</p>

<div class = "language-plaintext highlighter-rouge"> <div class = "highlight"> <pre class = "highlight"> <code> $ rm helpers.py
$ wget https://cdn.cs50.net/2022/fall/psets/9/finance/helpers.py

</code> </pre> </div> </div> </div>


Implementa un sitio web a través del cual los usuarios puedan "comprar" y "vender" acciones, como en la imagen a continuación.

![Finanzas de C$50](https://cs50.harvard.edu/x/2023/psets/9/finance/finance.png)

## Antecedentes

Si no estás seguro de lo que significa comprar y vender acciones (es decir, acciones de una empresa), dirígete [aquí](https://www.investopedia.com/articles/basics/06/invest1000.asp) para un tutorial.

Estás a punto de implementar C$50 Finanzas, una aplicación web a través de la cual puedes administrar carteras de acciones. No solo te permitirá verificar los precios reales de las acciones y el valor de las carteras, sino que también te permitirá "comprar" (bueno, "comprar") y "vender" (bueno, "vender") acciones mediante la consulta de [IEX](https://iextrading.com/developer/) por los precios de las acciones.

De hecho, IEX te permite descargar cotizaciones de acciones a través de su API (interfaz de programación de aplicaciones) utilizando URL como `https://api.iex.cloud/v1/data/core/quote/nflx?token=API_KEY`. Observa cómo el símbolo de Netflix (NFLX) está incrustado en esta URL; así es como IEX sabe a quién devolver los datos. Ese enlace no devolverá realmente ningún dato porque IEX requiere que uses una clave de API (más sobre eso en un momento), pero si lo hiciera, verías una respuesta en formato JSON (Notación de Objeto de JavaScript) como esta:

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
      "latestTime": "November 4, 2022",
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
      "isUSMarketOpen": False
    }

Observa cómo, entre las llaves, hay una lista de pares clave-valor separados por comas, con dos puntos separando cada clave de su valor.

¡Ahora centrémonos en obtener el código de distribución de este conjunto de problemas!