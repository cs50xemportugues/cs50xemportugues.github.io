# C$50 Finance

<div class="alert" data-alert="warning" role="alert"><p>This problem set’s distribution code has recently changed. If you downloaded the distribution code prior to <a data-local="2022-12-01T00:00:00+00:00" href="https://time.cs50.io/20221201T000000Z">2022-12-01T00:00:00+00:00</a>, run the following terminal commands in your <code class="language-plaintext highlighter-rouge">finance</code> directory to download the latest version of the distribution code.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ rm helpers.py
$ wget https://cdn.cs50.net/2022/fall/psets/9/finance/helpers.py

</code></pre></div></div></div>


Implement a website via which users can “buy” and “sell” stocks, a la the below.

![C$50 Finance](https://cs50.harvard.edu/x/2023/psets/9/finance/finance.png)

## Background

If you’re not quite sure what it means to buy and sell stocks (i.e., shares of a company), head [here](https://www.investopedia.com/articles/basics/06/invest1000.asp) for a tutorial.

You’re about to implement C$50 Finance, a web app via which you can manage portfolios of stocks. Not only will this tool allow you to check real stocks’ actual prices and portfolios’ values, it will also let you buy (okay, “buy”) and sell (okay, “sell”) stocks by querying [IEX](https://iextrading.com/developer/) for stocks’ prices.

Indeed, IEX lets you download stock quotes via their API (application programming interface) using URLs like `https://api.iex.cloud/v1/data/core/quote/nflx?token=API_KEY`. Notice how Netflix’s symbol (NFLX) is embedded in this URL; that’s how IEX knows whose data to return. That link won’t actually return any data because IEX requires you to use an API key (more about that in a bit), but if it did, you’d see a response in JSON (JavaScript Object Notation) format like this:

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

Notice how, between the curly braces, there’s a comma-separated list of key-value pairs, with a colon separating each key from its value.

Let’s turn our attention now to getting this problem’s distribution code!
