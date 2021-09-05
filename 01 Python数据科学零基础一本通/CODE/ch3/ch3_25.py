# 使用divmod()函数重新设计ch3_24.py
# ch3_25.py
dist = 384400
speed = 1225
total_hours = dist // speed
days, hours = divmod(total_hours,24)
print("总共需要天数")
print(days)
print("小时数")
print(hours)