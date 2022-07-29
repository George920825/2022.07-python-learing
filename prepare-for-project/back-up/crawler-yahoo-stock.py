# 抓取網頁原始碼
from logging import root
import urllib.request as req
url="https://tw.stock.yahoo.com/rank/change-up?exchange=TAI"
# 建立一個 Request 物件, 附加 Request Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# print(data)

# 解析原始碼, 取得文章標題
# 在終端機安裝 beautifulsoup4 (輸入: pip install beautifulsoup4)
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
comps=root.find_all("div", class_="Lh(20px) Fw(600) Fz(16px) Ell")
for comp in comps:
    print(comp.string)

# print(root.title.string)
# titles=root.find("div", class_="title") # 尋找 class="title" 的 div 標籤
# print(titles)
# print(titles.a.string)
# titles=root.find_all("div", class_="title") # 尋找 class="title" 的 div 標籤
# for title in titles:
#     if title.a != None:
#         print(title.a.string)