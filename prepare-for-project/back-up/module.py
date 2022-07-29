# # 載入模組
# import sys
# # 使用模組
# print(sys.platform)
# print(sys.maxsize)

# # 載入模組
# import sys as s
# # 使用模組
# print(s.platform)
# print(s.maxsize)

# # 自訂義模組
# import geometry
# result=geometry.distance(1,1,5,5)
# print(result)
# result=geometry.slope(1,2,5,6)
# print(result)

# 調整搜尋模組的路徑
import sys
# print(sys.path) #印出模組的搜尋路徑
sys.path.append("modules") # 在模組的搜尋路徑列表中[新增路徑]
import geometry
result=geometry.distance(1,1,5,5)
print(result)
result=geometry.slope(1,2,5,6)
print(result)