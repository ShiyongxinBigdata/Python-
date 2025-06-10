"""
第2章练习题5：浮点数处理

题目：圆形面积计算与取整
- 定义圆周率π = 3.14159
- 用户输入圆的半径
- 计算圆的面积（π * r²）
- 分别输出：原始面积、四舍五入到2位小数、向上取整、向下取整

输出格式：
请输入圆的半径：5.5
原始面积：94.985
四舍五入面积：94.99
向上取整面积：95
向下取整面积：94

考查知识点：浮点数运算、round()函数、math.ceil()、math.floor()
"""

import math

# 圆形面积计算与取整
# 定义圆周率
pi = 3.14159

# 获取用户输入的半径
radius_str = input("请输入圆的半径：")
radius = float(radius_str)  # 转换为浮点数

# 计算圆的面积：π * r²
area = pi * radius * radius

# 不同的取整处理
rounded_area = round(area, 2)        # 四舍五入到2位小数
ceil_area = math.ceil(area)          # 向上取整
floor_area = math.floor(area)        # 向下取整

# 输出结果
print("原始面积：%.3f" % area)
print("四舍五入面积：%.2f" % rounded_area)
print("向上取整面积：%d" % ceil_area)
print("向下取整面积：%d" % floor_area) 