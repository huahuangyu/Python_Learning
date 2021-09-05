# 计算地月距离
# ch3_24.py
dist = 384400
speed = 1225
total_hours = dist // speed
days = total_hours // 24
hours = total_hours % 24
print("总共需要天数")
print(days)
print("小时数")
print(hours)