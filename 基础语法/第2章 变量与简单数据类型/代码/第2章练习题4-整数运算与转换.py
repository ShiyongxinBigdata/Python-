"""
第2章练习题4：整数运算与转换

题目：用户输入两个数字进行计算
- 提示用户输入第一个数字
- 提示用户输入第二个数字
- 将输入的字符串转换为整数
- 计算两数的加法、减法、乘法、除法
- 输出所有计算结果

输出格式：
请输入第一个数字：10
请输入第二个数字：3
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.33

考查知识点：input()函数、int()类型转换、整数运算、格式化输出
"""

# 用户输入与整数运算
# 获取用户输入
num1_str = input("请输入第一个数字：")
num2_str = input("请输入第二个数字：")

# 类型转换：将字符串转换为整数
num1 = int(num1_str)
num2 = int(num2_str)

# 进行各种数学运算
addition = num1 + num2      # 加法
subtraction = num1 - num2   # 减法
multiplication = num1 * num2 # 乘法
division = num1 / num2      # 除法（结果为浮点数）

# 输出计算结果
print("%d + %d = %d" % (num1, num2, addition))
print("%d - %d = %d" % (num1, num2, subtraction))
print("%d * %d = %d" % (num1, num2, multiplication))
print("%d / %d = %.2f" % (num1, num2, division)) 