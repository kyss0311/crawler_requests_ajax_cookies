import requests
import pandas as pd

url = "https://api.hahow.in/api/products/search?category=COURSE&filter=PUBLISHED&limit=24&page=0&sort=TRENDING"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
# 檢查網址
if response.status_code == 200:
    data = response.json()
    products = data['data']['courseData']['products']
    # 將資料存進列表
    course_list = []
    for product in products:
        course_data = [
            product['title'],
            product['price'],
            product['averageRating'],
            product['numSoldTickets']
        ]
        if product['averageRating'] > 4 and product['numSoldTickets'] > 2000:
            course_list.append(course_data)

    # 用pandas將列表轉城excel
    df = pd.DataFrame(course_list, columns=['title', 'price', 'averageRating', 'numSoldTickets' ])
    df.to_excel('courses.xlsx', index=False, engine="openpyxl")

else:
    print("找不到網頁")
