import csv
import json
from urllib.request import urlopen

# 1. 從API抓取資料
url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
response = urlopen(url)
data = response.read().decode("utf-8")

# 2. 將JSON格式資料轉換為Python資料結構
json_obj = json.loads(data)

# 3. 從Python資料結構中取出資料
attraction_data = []
mrt_data = {}

for item in json_obj['result']['results']:

    # 景點名稱
    stitle = item['stitle']

    # 區域
    address = item['address'].split()[1][0:3]

    # 經度
    longitude = item['longitude']

    # 緯度
    latitude = item['latitude']

    # 第一張圖檔網址
    img = 'https' + item['file'].split('https')[1]

    # 捷運站
    mrt = item['MRT']

    # 景點名稱
    stitle = item['stitle']

    # 確保"MRT"的值不是null
    if mrt is not None:
        if mrt not in mrt_data:
            mrt_data[mrt] = []

        mrt_data[mrt].append(stitle)

    attraction_data.append([stitle, address, longitude, latitude, img])

# 4. 將 attraction 寫入CSV檔
with open('attraction.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for data in attraction_data:
        writer.writerow(data)

# 5. 將 mrt 寫入 CSV 檔
with open('mrt.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for mrt, attractions in mrt_data.items():
        writer.writerow([mrt] + attractions)
