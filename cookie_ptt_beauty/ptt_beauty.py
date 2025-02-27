import requests
from bs4 import BeautifulSoup
import os  # 加入可以建立資料夾的套件


def download_img(url, save_path):  # 連結, 檔名
    print(f"正在下載圖片: {url}")
    response = requests.get(url)
    with open(save_path, 'wb') as file:  # wb表示寫入二進位的檔案
        file.write(response.content)
        print("-"*30)


def main():
    url = "https://www.ptt.cc/bbs/Beauty/M.1736256885.A.D90.html"
    # 通過over18的cookie
    hearders = {"Cookie": "over18=1"}
    response = requests.get(url, headers=hearders)
    soup = BeautifulSoup(response.text, "html.parser")


    spans = soup.find_all("span", class_="article-meta-value")
    # 我們要的標題index=2
    title = spans[2].text

    # 建立可以存放圖片的資料夾 如果資料夾已經存在就不要創建新的
    dir_name = f"images/{title}"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    allow_file_name = ["jpg", "png", "jpeg", "gif"]  # 允許的檔案格式
    # 找到網頁中所有連結
    links = soup.find_all("a")
    for link in links:
        href = link.get("href")
        # 判斷是否為連結
        if not href:
            continue
        file_name = href.split("/")[-1]
        # 找出檔案中以.來分割的最後一段字 轉成小寫
        extension = href.split(".")[-1].lower()
        if extension in allow_file_name:
            print(f"file type:{extension}")
            print(f"url: {href}")
            download_img(href, f"{dir_name}/{file_name}")


# 如果
if __name__ == "__main__":
    main()
