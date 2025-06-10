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

# 获取用户输入
num1_str = input("请输入第一个数字：")
num2_str = input("请输入第二个数字：")
# 数据类型转换
num1 = int(num1_str)
num2 = int(num2_str)
# 算术运算
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2  # 除法默认结果是小数
# 格式化输出
# 字符串拼接
print(str(num1) + " + " +str( num2) + " = " + str(add))
print("%d + %d = %d" % (num1, num2, add))
print("%d - %d = %d" % (num1, num2, sub))
print("%d * %d = %d" % (num1, num2, mul))
print("%d / %d = %.3f" % (num1, num2, div))

