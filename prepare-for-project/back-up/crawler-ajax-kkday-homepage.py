# 抓取網頁原始碼
from logging import root
import urllib.request as req
url="https://www.kkday.com/zh-tw/home/ajax_get_homepage_setting?csrf_token_name=f33efcd4068721d3795dffb5d9824cdc"
# 建立一個 Request 物件, 附加 Request Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") # 取得 JSON 格式的資料

# 解析 JSON 格式的資料, 取得文章標題
import json
data=json.loads(data) # 將原始資料解析成字典/列表形式
# prod_group=data["data"]["homepage_product_group"][0]["prod_list"][0]["name"]

# prod_group=data["data"]["homepage_product_group"][0]["prod_list"]
# for prod in prod_group:
#     print(prod["name"])

prod_group=data["data"]["homepage_product_group"]
for prod_list in prod_group:
    prod_num=prod_list["prod_list"]
    for prod in prod_num:
        print(prod["name"])