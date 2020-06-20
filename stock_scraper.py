from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from datetime import datetime
from datetime import date
import time
import requests 
import string

# Find the company name
def findCompany(stock):
    # Insert ticker symbol of stock here and then it retrieves its current price from Yahoo Finance
    url = 'https://finance.yahoo.com/quote/' + stock + '?p=' + stock + '&.tsrc=fin-srch'

    # Taken from https://dev.to/kashaziz/web-scraping-with-python-beautifulsoup-and-requests-2n71
    # prepare headers
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    # fetching the url, raising error if operation fails
    try:
        content = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        exit()
    # End of part taken

    # Create BeautifulSoup object from url
    page_soup = soup(content.text, 'html.parser')

    # Grabs current stock price from Yahoo Finance
    text = 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'
    company = page_soup.findAll("div", {"class": text})[0].find('h1').text
    companyName = company.split('(')[0].strip()

    # Taking out any commas in company name
    return companyName.replace(","," ").strip()

# Find the current price at this very moment of a stock (to be inserted in the form of a string)
def findCurrentPrice(stock):
    # Insert ticker symbol of stock here and then it retrieves its current price from Yahoo Finance
    url = 'https://finance.yahoo.com/quote/' + stock + '?p=' + stock + '&.tsrc=fin-srch'

    # prepare headers
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    # fetching the url, raising error if operation fails
    try:
        content = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        exit()

    # Create BeautifulSoup object from url
    page_soup = soup(content.text, 'html.parser')

    # Grabs current stock price from Yahoo Finance
    curr_price = page_soup.findAll("div", {"class": "My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text

    # Taken from https://www.programiz.com/python-programming/datetime/current-datetime#:~:text=Example%201%3A%20Python%20get%20today's%20date&text=today()%20method%20to%20get,representing%20date%20in%20different%20formats.

    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")

    # Returns current price with time and date (mostly useful if trying to keep track of minute to minute changes)
    #return curr_price + " " + '@' + " " + str(dt_string)
    
    # Takes the original, removes commas and then removes spaces between digits
    currPriceSpaced = curr_price.replace(","," ").strip()
    return currPriceSpaced.translate({ord(c): None for c in string.whitespace})

# Find the current change in a stock 
def findCurrentChange(stock):
    # Insert ticker symbol of stock here and then it retrieves its current price from Yahoo Finance
    url = 'https://finance.yahoo.com/quote/' + stock + '?p=' + stock + '&.tsrc=fin-srch'

    # prepare headers
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    # fetching the url, raising error if operation fails
    try:
        content = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        exit()

    # Create BeautifulSoup object from url
    page_soup = soup(content.text, 'html.parser')

    # Grabs current stock price from Yahoo Finance
    curr_change = page_soup.findAll("div", {"class": "My(6px) Pos(r) smartphone_Mt(6px)"})[0].find_all('span',limit = 3)[1].text 

    # Taken from https://www.programiz.com/python-programming/datetime/current-datetime#:~:text=Example%201%3A%20Python%20get%20today's%20date&text=today()%20method%20to%20get,representing%20date%20in%20different%20formats.

    # datetime object containing current date and time
    #now = datetime.now()

    # dd/mm/YY H:M:S
    #dt_string = now.strftime("%m/%d/%Y %H:%M:%S")

    #return curr_change + " " + '@' + " " + str(dt_string)
    
    # Takes the original, removes commas and then removes spaces between digits
    currChangeSpaced = curr_change.replace(","," ").strip()
    return currChangeSpaced.translate({ord(c): None for c in string.whitespace})


# Find the where a stock price was at market open
def findOpen(stock):
    # Insert ticker symbol of stock here and then it retrieves its current price from Yahoo Finance
    url = 'https://finance.yahoo.com/quote/' + stock + '?p=' + stock + '&.tsrc=fin-srch'

    # prepare headers
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    # fetching the url, raising error if operation fails
    try:
        content = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        exit()

    # Create BeautifulSoup object from url
    page_soup = soup(content.text, 'html.parser')

    # Grabs current stock price from Yahoo Finance
    text = "D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)"
    open = page_soup.findAll("div", {"class": text})[0].findAll("td", {"class": "Ta(end) Fw(600) Lh(14px)"})[1].text

    # Takes the original, removes commas and then removes spaces between digits
    openSpaced = open.replace(","," ").strip()
    return openSpaced.translate({ord(c): None for c in string.whitespace})

# Find the previous close of a certain stock
def findPreviousClose(stock):
    # Insert ticker symbol of stock here and then it retrieves its current price from Yahoo Finance
    url = 'https://finance.yahoo.com/quote/' + stock + '?p=' + stock + '&.tsrc=fin-srch'

    # prepare headers
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    # fetching the url, raising error if operation fails
    try:
        content = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        exit()

    # Create BeautifulSoup object from url
    page_soup = soup(content.text, 'html.parser')

    # Grabs previous close from Yahoo Finance
    text = "D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)"
    close = page_soup.findAll("div", {"class": text})[0].findAll("td", {"class": "Ta(end) Fw(600) Lh(14px)"})[0].find('span').text

    # Takes the original, removes commas and then removes spaces between digits
    closeSpaced = close.replace(","," ").strip()
    return closeSpaced.translate({ord(c): None for c in string.whitespace})

# Find the current day's range of a stock
def findRange(stock):
    # Insert ticker symbol of stock here and then it retrieves its current price from Yahoo Finance
    url = 'https://finance.yahoo.com/quote/' + stock + '?p=' + stock + '&.tsrc=fin-srch'

    # prepare headers
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    # fetching the url, raising error if operation fails
    try:
        content = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        exit()

    # Create BeautifulSoup object from url
    page_soup = soup(content.text, 'html.parser')

    # Grabs previous range from Yahoo Finance
    text = "D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)"
    range = page_soup.findAll("div", {"class": text})[0].findAll("td", {"class": "Ta(end) Fw(600) Lh(14px)"})[4].text

    # Takes the original, removes commas and then removes spaces between digits
    rangeSpaced = range.replace(","," ").strip()
    return rangeSpaced.translate({ord(c): None for c in string.whitespace})

# Find the 52 week range of a stock
def find52Range(stock):
    # Insert ticker symbol of stock here and then it retrieves its current price from Yahoo Finance
    url = 'https://finance.yahoo.com/quote/' + stock + '?p=' + stock + '&.tsrc=fin-srch'

    # prepare headers
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    # fetching the url, raising error if operation fails
    try:
        content = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        exit()

    # Create BeautifulSoup object from url
    page_soup = soup(content.text, 'html.parser')

    # Grabs previous range from Yahoo Finance
    text = "D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)"
    range = page_soup.findAll("div", {"class": text})[0].findAll("td", {"class": "Ta(end) Fw(600) Lh(14px)"})[5].text

    # Takes the original, removes commas and then removes spaces between digits
    rangeSpaced = range.replace(","," ").strip()
    return rangeSpaced.translate({ord(c): None for c in string.whitespace})

# Find the PE Ratio of a stock
def findPERatio(stock):
    # Insert ticker symbol of stock here and then it retrieves its current price from Yahoo Finance
    url = 'https://finance.yahoo.com/quote/' + stock + '?p=' + stock + '&.tsrc=fin-srch'

    # prepare headers
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    # fetching the url, raising error if operation fails
    try:
        content = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        exit()

    # Create BeautifulSoup object from url
    page_soup = soup(content.text, 'html.parser')

    # Grabs previous range from Yahoo Finance
    text = "D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)"
    ratio = page_soup.findAll("div", {"class": text})[0].findAll("td", {"class": "Ta(end) Fw(600) Lh(14px)"})[2].text

    # Takes the original, removes commas and then removes spaces between digits
    ratioSpaced = ratio.replace(","," ").strip()
    return ratioSpaced.translate({ord(c): None for c in string.whitespace})

# Find the volume of a stock
def findVolume(stock):
    # Insert ticker symbol of stock here and then it retrieves its current price from Yahoo Finance
    url = 'https://finance.yahoo.com/quote/' + stock + '?p=' + stock + '&.tsrc=fin-srch'

    # prepare headers
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    # fetching the url, raising error if operation fails
    try:
        content = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        exit()

    # Create BeautifulSoup object from url
    page_soup = soup(content.text, 'html.parser')

    # Grabs volume from Yahoo Finance
    text = "D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)"
    vol = page_soup.findAll("div", {"class": text})[0].findAll("td", {"class": "Ta(end) Fw(600) Lh(14px)"})[6].text

    # Takes the original, removes commas and then removes spaces between digits
    volSpaced = vol.replace(","," ").strip()
    return volSpaced.translate({ord(c): None for c in string.whitespace})

# Find top trending tickers from S&P 500 on Wikipedia (taken from https://pythonprogramming.net/sp500-company-list-python-programming-for-finance/ and modified slightly)
def save_sp500_tickers():
    url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

    # prepare headers
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    # fetching the url, raising error if operation fails
    try:
        content = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        exit()

    page_soup = soup(content.text, 'html.parser')
    table = page_soup.find('table', {'class': 'wikitable sortable'})
    
    tickers = []
    sanitized = []
    
    # Returns all ticker symbols with a newline character at the end
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)
    
    # Taking out the newline character and having just ticker symbols as string
    for i in tickers:
        j = i.replace("\n","")
        sanitized.append(j)
        
    return sanitized

tickers = save_sp500_tickers()

# opens file, and writes headers
f = open("stocks.csv", "w")
f.write("Company, Symbol, Current Value, Current Change, Open, Previous Close, Day's Range, 52 Week Range, P/E Ratio, Volume \n")

# writes the dataset to file
for i in range(0,len(tickers) - 1):
    f.write(findCompany(tickers[i]) + ", " + tickers[i] + ", " + findCurrentPrice(tickers[i]) + ", " + findCurrentChange(tickers[i]) + ", " + findOpen(tickers[i]) + ", " + findPreviousClose(tickers[i]) + ", " + findRange(tickers[i]) + ", " + find52Range(tickers[i]) + ", " + findPERatio(tickers[i]) + ", " + findVolume(tickers[i]) + "\n")

# Closes and saves changes to CSV file 
f.close()





