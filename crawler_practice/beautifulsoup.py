# 印出ptt網站中的所有標題
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"
# 建立一個 request headers 的資訊
# 因為很多網站不希望自己的資料背爬蟲讀取 所以要到網站 用開發人員工具 找到 User-Agent

request = req.Request(url, headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

# 解析資料
import bs4
root = bs4.BeautifulSoup(data, "html.parser")
# print(root.title.string)

# 出html中要的資訊的資料特色 ex標題都會被a標籤包住 外面再包一成div標籤
titles = root.find_all("div", class_="my-2 text-sm text-nord4 truncate")
for title in titles:
    if title.a != None:  # 如果標題有a標籤就印出來
        print(title.a.string)
