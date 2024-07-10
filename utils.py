import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from stock_indicators.indicators.common.quote import Quote


def get_driver():
    options = Options()
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument(r'--user-data-dir=/Users/vitaly/Library/Application Support/Google/Chrome/Default')
    # chromedriver can be downloaded from: https://googlechromelabs.github.io/chrome-for-testing/
    try:
        service = Service(executable_path=r'/Users/vitaly/Downloads/chromedriver-mac-arm64/chromedriver')
        driver = webdriver.Chrome(options=options, service=service)
    except Exception as e:
        service = Service()
        driver = webdriver.Chrome(options=options, service=service)

    return driver


def get_quotes(candles):
    quotes = []
    for candle in candles:
        open = candle[1]
        close = candle[2]
        high = candle[3]
        low = candle[4]
        if os.name == 'nt':  # windows
            quotes.append(Quote(
                date=datetime.fromtimestamp(candle[0]),
                open=str(open).replace('.', ','),
                high=str(high).replace('.', ','),
                low=str(low).replace('.', ','),
                close=str(close).replace('.', ','),
                volume=None))
        else:
             quotes.append(Quote(
                date=datetime.fromtimestamp(candle[0]),
                open=open,
                high=high,
                low=low,
                close=close,
                volume=None))
    return quotes


companies = {
    'Apple OTC': '#AAPL_otc',
    'American Express OTC': '#AXP_otc',
    'Boeing Company OTC': '#BA_otc',
    'Johnson & Johnson OTC': '#JNJ_otc',
    "McDonald's OTC": '#MCD_otc',
    'Tesla OTC': '#TSLA_otc',
    'Amazon OTC': 'AMZN_otc',
    'VISA OTC': 'VISA_otc',
    'Netflix OTC': 'NFLX_otc',
    'Alibaba OTC': 'BABA_otc',
    'ExxonMobil OTC': '#XOM_otc',
    'FedEx OTC': 'FDX_otc',
    'FACEBOOK INC OTC': '#FB_otc',
    'Pfizer Inc OTC': '#PFE_otc',
    'Intel OTC': '#INTC_otc',
    'TWITTER OTC': 'TWITTER_otc',
    'Microsoft OTC': '#MSFT_otc',
    'Cisco OTC': '#CSCO_otc',
    'Citigroup Inc OTC': 'CITI_otc',
}