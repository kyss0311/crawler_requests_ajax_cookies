import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

def fetch_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('div', class_="SoaBEf")
    for title in titles:
        name = title.find("div", class_="n0jPhd ynAwRc MBeuO nDgy9d")
        print(name.text)
    # print(soup)


url = "https://www.google.com/search?q=nba+%E9%A6%AC%E5%88%BA&sca_esv=7d4dc610cbe5f3b5&rlz=1C1ONGR_zh-TWTW997TW997&biw=1745&bih=859&tbm=nws&sxsrf=ADLYWII8UB8wq2u1GJ5CyKAi1QLMxZCZog%3A1736664431494&ei=b2WDZ6PuHaHP2roPs9fX2QY&ved=0ahUKEwjj4aGUy--KAxWhp1YBHbPrNWsQ4dUDCA4&uact=5&oq=nba+%E9%A6%AC%E5%88%BA&gs_lp=Egxnd3Mtd2l6LW5ld3MiCm5iYSDppqzliLoyChAAGIAEGEMYigUyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBBAAGB4yBBAAGB4yBBAAGB5ItxRQmwdYuxFwAHgAkAEAmAFAoAHiAqoBATe4AQPIAQD4AQGYAgegAvACwgILEAAYgAQYsQMYgwHCAgQQABgDwgIQEAAYgAQYsQMYQxiDARiKBcICCBAAGIAEGLEDwgIOEAAYgAQYsQMYgwEYigXCAgYQABgIGB7CAggQABgIGAoYHsICCBAAGIAEGKIEwgIFEAAY7wWYAwCIBgGSBwE3oAfFEg&sclient=gws-wiz-news"
# 模仿使用者發出一個請求到伺服器
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

fetch_data(url)


