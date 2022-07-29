# 抓取網頁原始碼
from logging import root
import urllib.request as req
url="https://www.kkday.com/zh-tw/product/ajax_productlist/?country=&city=&keyword=&availstartdate=&availenddate=&cat=TAG_6_1&time=&glang=&sort=popularity&page=1&row=10&fprice=*&eprice=*&precurrency=TWD&csrf_token_name=4207e196ac65b5b708c2156ae809bb69"
# 建立一個 Request 物件, 附加 Request Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") # 取得 JSON 格式的資料

# 解析 JSON 格式的資料, 取得文章標題
import json
data=json.loads(data) # 將原始資料解析成字典/列表形式
prod_group=data["data"]
for num in prod_group:
    print(num["name"])