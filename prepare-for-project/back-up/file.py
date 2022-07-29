# 儲存檔案
# 1
# file=open("data.txt", mode="w", encoding="utf-8") # 中文: encoding="utf-8"
# file.write("中文\nSecond Line")
# file.close()

# 2
# with open("data.txt", mode="w",  encoding="utf-8") as file:
#     file.write("5\n3")

# 讀取檔案
# sum=0
# with open("data.txt", mode="r",  encoding="utf-8") as file:
#     # data=file.read() 全部讀取
#     for line in file:
#         sum+=int(line)
# print(sum)

# 使用 JSON 格式讀取, 複寫檔案
import json
# 讀取檔案, 把資把資料放入變數(data)中
with open("config.json", mode="r") as file:
    data=json.load(file)
print(data) # 字典dictionary data type
# print("name", data["name"])
# print("version: ", data["version"])

data["name"]="New Name" # 修改變數中的資料
# 把最新的資料複寫(copy)回檔案中
with open("config.json", mode="w") as file:
    json.dump(data, file)