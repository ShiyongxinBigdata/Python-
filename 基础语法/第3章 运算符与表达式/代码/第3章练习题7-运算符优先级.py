"""
第3章练习题7：运算符优先级

题目：表达式计算器
- 计算包含多种运算符的复杂表达式
- 演示运算符优先级的影响
- 对比加括号前后的计算结果
- 理解运算符的结合性

表达式示例：
1. 3 + 2 * 4 ** 2 - 1
2. (3 + 2) * 4 ** 2 - 1
3. 3 + 2 * (4 ** 2 - 1)
4. True or False and not True
5. 10 > 5 and 3 < 8 or 2 == 2

考查知识点：运算符优先级、括号的作用、复合表达式计算
"""

# 表达式计算器
print("=== 运算符优先级演示 ===")

# 算数运算符优先级演示
print("--- 算数运算符优先级 ---")

# 表达式1：幂运算 > 乘除 > 加减
expr1 = 3 + 2 * 4 ** 2 - 1
print("3 + 2 * 4 ** 2 - 1 = %d" % expr1)
print("计算过程：3 + 2 * 16 - 1 = 3 + 32 - 1 = 34")

# 表达式2：括号改变优先级
expr2 = (3 + 2) * 4 ** 2 - 1
print("(3 + 2) * 4 ** 2 - 1 = %d" % expr2)
print("计算过程：5 * 16 - 1 = 80 - 1 = 79")

# 表达式3：不同的括号位置
expr3 = 3 + 2 * (4 ** 2 - 1)
print("3 + 2 * (4 ** 2 - 1) = %d" % expr3)
print("计算过程：3 + 2 * (16 - 1) = 3 + 2 * 15 = 3 + 30 = 33")

# 表达式4：完全加括号的版本
expr4 = ((3 + 2) * (4 ** 2)) - 1
print("((3 + 2) * (4 ** 2)) - 1 = %d" % expr4)
print("计算过程：(5 * 16) - 1 = 80 - 1 = 79")

# 逻辑运算符优先级演示
print("\n--- 逻辑运算符优先级 ---")
print("优先级：not > and > or")

# 表达式5：not > and > or
expr5 = True or False and not True
print("True or False and not True = %s" % expr5)
print("计算过程：True or False and False = True or False = True")

# 表达式6：加括号改变优先级
expr6 = (True or False) and not True
print("(True or False) and not True = %s" % expr6)
print("计算过程：True and False = False")

# 表达式7：另一种括号组合
expr7 = True or (False and not True)
print("True or (False and not True) = %s" % expr7)
print("计算过程：True or (False and False) = True or False = True")

# 比较运算符与逻辑运算符混合
print("\n--- 混合运算符优先级 ---")

# 表达式8：比较运算符 > 逻辑运算符
expr8 = 10 > 5 and 3 < 8 or 2 == 2
print("10 > 5 and 3 < 8 or 2 == 2 = %s" % expr8)
print("计算过程：True and True or True = True or True = True")

# 表达式9：加括号改变优先级
expr9 = 10 > 5 and (3 < 8 or 2 == 2)
print("10 > 5 and (3 < 8 or 2 == 2) = %s" % expr9)
print("计算过程：True and (True or True) = True and True = True")

# 表达式10：复杂的混合表达式
expr10 = not 5 > 3 or 2 + 3 == 5 and 10 // 3 > 2
print("not 5 > 3 or 2 + 3 == 5 and 10 // 3 > 2 = %s" % expr10)
print("计算过程：not True or 5 == 5 and 3 > 2 = False or True and True = False or True = True")

# 用户自定义表达式计算
print("\n=== 用户表达式计算 ===")

# 获取用户输入的数值
a = float(input("请输入变量a的值："))
b = float(input("请输入变量b的值："))
c = float(input("请输入变量c的值："))

print("\n使用您输入的值计算以下表达式：")

# 计算各种表达式
result1 = a + b * c
print("a + b * c = %.2f + %.2f * %.2f = %.2f" % (a, b, c, result1))

result2 = (a + b) * c
print("(a + b) * c = (%.2f + %.2f) * %.2f = %.2f" % (a, b, c, result2))

result3 = a ** 2 + b ** 2 + c ** 2
print("a² + b² + c² = %.2f² + %.2f² + %.2f² = %.2f" % (a, b, c, result3))

result4 = (a + b + c) / 3
print("(a + b + c) / 3 = (%.2f + %.2f + %.2f) / 3 = %.2f" % (a, b, c, result4))

# 比较表达式
comparison1 = a > b and b > c
print("a > b and b > c = %.2f > %.2f and %.2f > %.2f = %s" % (a, b, b, c, comparison1))

comparison2 = a > b or b > c
print("a > b or b > c = %.2f > %.2f or %.2f > %.2f = %s" % (a, b, b, c, comparison2)) 