import time
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

# 儲存資料的列表
data_list = []
def fetch_data(url):
    response = requests.get(url, headers=headers)
    # 傳入BeautifulSoup 用html解析 parser:解析器
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all("div", class_="r-ent")

    # 取出文章標題人氣時間
    for a in articles:
        # 將每一筆資料存城字典的格式
        data = {}
        title = a.find("div", class_="title")
        if title and title.a:
            title = title.a.text
        else:
            title = "none"
        data["標題"] = title
        popular = a.find("div", class_="nrec")
        if popular and popular.span:
            popular = popular.span.text
        else:
            popular = "N/A"
        data["人氣"] = popular

        date = a.find("div", class_="date")
        if date:
            date = date.text
        else:
            date = "N/A"
        data["日期"] = date
        # 將資料加入列表
        data_list.append(data)
        # print(f"標題:{title} 人氣:{popular} 日期:{date}")
    # 自行設定一個終止網頁 不然爬不完
    url_end = "/bbs/NBA/index6495.html"
    next_pages = soup.find_all("a", class_="btn wide")
    for next_page in next_pages:
        if next_page and next_page.text == "‹ 上頁":
            next_url = next_page.get("href")
            if next_url ==url_end:
                break
            print(f"正在爬取：{next_url}")
            time.sleep(3)
            fetch_data("https://www.ptt.cc"+next_url)


url = "https://www.ptt.cc/bbs/NBA/index6500.html"
# 模仿使用者發出一個請求到伺服器
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
fetch_data(url)

# 將資料儲存城json格式
with open("ptt_nbadata.json", 'w', encoding="utf-8") as fout:
    # 轉換資料 indent:縮排
    json.dump(data_list, fout, ensure_ascii=False, indent=4)
print("資料已成功存成json")

# 將資料轉城excel
df = pd.DataFrame(data_list)
df.to_excel("ptt_nba.xlsx", index=False, engine="openpyxl") # 檔名 , index=False excel, 套件
print("成功將資料存成excel")

# 檢查輸入的網址是否正確
# if response.status_code == 200:
#     # 將爬取的資料存城html檔
#     with open("output.html", 'w', encoding="utf-8") as f:
#         f.write(response.text)
#     print("寫入html"
#           "成功")
#
# else:
#     print("找不到網頁")

