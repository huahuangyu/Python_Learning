# 将一个语句分成多行
# ch2_4.py
a = b = c = 10
x = a + b + c + 12
print(x)
# 续行方法1
y = a + \
    b + \
    c + \
    12
print(y)
# 续行方法2
z = (a +        # 此处可以加上注释
     b +
     c +
     12 )
print(z)