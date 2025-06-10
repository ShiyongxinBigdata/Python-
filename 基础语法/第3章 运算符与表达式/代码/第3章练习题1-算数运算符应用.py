"""
第3章练习题1：算数运算符应用

题目：数学计算器
- 用户输入两个数字
- 计算并输出：加法、减法、乘法、除法、整除、取余、幂运算的结果
- 计算复合表达式：(a + b) * (a - b) + a ** 2

输出格式：
请输入第一个数字：8
请输入第二个数字：3
8 + 3 = 11
8 - 3 = 5
8 * 3 = 24
8 / 3 = 2.67
8 // 3 = 2
8 % 3 = 2
8 ** 3 = 512
复合表达式 (8+3)*(8-3)+8² = 119

考查知识点：所有算数运算符、运算优先级、复合表达式
"""

# 数学计算器
# 获取用户输入
a_str = input("请输入第一个数字：")
b_str = input("请输入第二个数字：")

# 类型转换
a = float(a_str)  # 转换为浮点数以支持小数运算
b = float(b_str)

# 基本算数运算
addition = a + b        # 加法
subtraction = a - b     # 减法
multiplication = a * b  # 乘法
division = a / b        # 除法
floor_division = a // b # 整除
modulus = a % b         # 取余
power = a ** b          # 幂运算

# 复合表达式计算
complex_expr = (a + b) * (a - b) + a ** 2

# 输出结果
print("%.0f + %.0f = %.0f" % (a, b, addition))
print("%.0f - %.0f = %.0f" % (a, b, subtraction))
print("%.0f * %.0f = %.0f" % (a, b, multiplication))
print("%.0f / %.0f = %.2f" % (a, b, division))
print("%.0f // %.0f = %.0f" % (a, b, floor_division))
print("%.0f %% %.0f = %.0f" % (a, b, modulus))
print("%.0f ** %.0f = %.0f" % (a, b, power))
print("复合表达式 (%.0f+%.0f)*(%.0f-%.0f)+%.0f² = %.0f" % (a, b, a, b, a, complex_expr)) 