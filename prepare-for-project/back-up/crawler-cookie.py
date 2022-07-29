# 抓取網頁原始碼
from logging import root
import urllib.request as req
def getData(url):
    # 建立一個 Request 物件, 附加 Request Headers 的資訊
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    # print(data)

    # 解析原始碼, 取得文章標題
    # 在終端機安裝 beautifulsoup4 (輸入: pip install beautifulsoup4)
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    # print(root.title.string)
    # titles=root.find("div", class_="title") # 尋找 class="title" 的 div 標籤
    # print(titles)
    # print(titles.a.string)
    titles=root.find_all("div", class_="title") # 尋找 class="title" 的 div 標籤
    for title in titles:
        if title.a != None:
            print(title.a.string)
    # 抓取上一頁的網址
    nextLink=root.find("a", string="‹ 上頁") # 尋找內文是 ‹ 上頁 的 a 標籤
    # print(nextLink["href"]) # 過濾出標籤的 href 屬性
    return(nextLink["href"])

# 抓取一個頁面的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1