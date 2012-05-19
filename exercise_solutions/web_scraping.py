# import the required libraries
import requests
import bs4

# define a generic function that will get the quote price for any stock symbol
def get_quote(symbol):
    # make the reqest to google finance and store the response
    response = requests.get('http://finance.google.com/finance?q=' + symbol)
    # parse the response text with beautiful soup so we can select the quote
    soup = bs4.BeautifulSoup(response.text)
    # select the quote
    quote = soup.select('.pr span')[0].text
    # return the quote
    return quote

# now you can get the stock quote for any symbol
print 'FB: $' + get_quote('FB')

# or loop over a list of symbols
symbols = [
    'IBM',
    'MSFT',
    'AAPL',
    'GOOG',
    'ORCL',
]
for symbol in symbols:
    print symbol + ': $' + get_quote(symbol)
