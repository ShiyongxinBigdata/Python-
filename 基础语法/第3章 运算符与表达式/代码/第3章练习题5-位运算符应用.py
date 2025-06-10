"""
第3章练习题5：位运算符应用

题目：数字处理工具
- 用户输入两个整数
- 演示所有位运算符的效果
- 显示二进制表示
- 实际应用：判断奇偶数、快速乘除法、权限管理

输出格式：
请输入第一个整数：12
请输入第二个整数：5
12的二进制：1100
5的二进制：101
12 & 5 = 4 (二进制：100)
12 | 5 = 13 (二进制：1101)
12 ^ 5 = 9 (二进制：1001)
~12 = -13
12 << 2 = 48 (相当于12*4)
12 >> 1 = 6 (相当于12/2)

考查知识点：所有位运算符、二进制表示、位运算的实际应用
"""

# 数字处理工具
print("=== 数字处理工具 ===")

# 获取用户输入
num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))

# 显示二进制表示
print("\n=== 二进制表示 ===")
print("%d的二进制：%s" % (num1, bin(num1)[2:]))  # bin()返回'0b'开头的字符串，[2:]去掉前缀
print("%d的二进制：%s" % (num2, bin(num2)[2:]))

# 位运算演示
print("\n=== 位运算结果 ===")

# 按位与运算
and_result = num1 & num2
print("%d & %d = %d (二进制：%s)" % (num1, num2, and_result, bin(and_result)[2:]))

# 按位或运算
or_result = num1 | num2
print("%d | %d = %d (二进制：%s)" % (num1, num2, or_result, bin(or_result)[2:]))

# 按位异或运算
xor_result = num1 ^ num2
print("%d ^ %d = %d (二进制：%s)" % (num1, num2, xor_result, bin(xor_result)[2:]))

# 按位取反运算
not_result1 = ~num1
not_result2 = ~num2
print("~%d = %d" % (num1, not_result1))
print("~%d = %d" % (num2, not_result2))

# 左移运算
left_shift1 = num1 << 2
left_shift2 = num2 << 1
print("%d << 2 = %d (相当于%d*4)" % (num1, left_shift1, num1))
print("%d << 1 = %d (相当于%d*2)" % (num2, left_shift2, num2))

# 右移运算
right_shift1 = num1 >> 1
right_shift2 = num2 >> 2
print("%d >> 1 = %d (相当于%d/2)" % (num1, right_shift1, num1))
print("%d >> 2 = %d (相当于%d/4)" % (num2, right_shift2, num2))

# 位运算的实际应用
print("\n=== 位运算实际应用 ===")

# 1. 判断奇偶数
print("--- 奇偶数判断 ---")
if num1 & 1:
    print("%d是奇数" % num1)
else:
    print("%d是偶数" % num1)

if num2 & 1:
    print("%d是奇数" % num2)
else:
    print("%d是偶数" % num2)

# 2. 快速计算2的幂次方
print("\n--- 快速计算2的幂次方 ---")
power_3 = 1 << 3  # 2^3
power_5 = 1 << 5  # 2^5
print("2³ = %d" % power_3)
print("2⁵ = %d" % power_5)

# 3. 交换两个数（使用异或运算）
print("\n--- 异或交换数值 ---")
a, b = num1, num2
print("交换前：a=%d, b=%d" % (a, b))
a = a ^ b
b = a ^ b
a = a ^ b
print("交换后：a=%d, b=%d" % (a, b))

# 4. 权限管理示例（位掩码）
print("\n--- 权限管理示例 ---")
READ = 1    # 001
WRITE = 2   # 010
EXECUTE = 4 # 100

# 设置权限（使用或运算）
user_permission = READ | WRITE  # 011，有读写权限
print("用户权限：%d (二进制：%s)" % (user_permission, bin(user_permission)[2:]))

# 检查权限（使用与运算）
has_read = bool(user_permission & READ)
has_write = bool(user_permission & WRITE)
has_execute = bool(user_permission & EXECUTE)

print("有读权限：%s" % has_read)
print("有写权限：%s" % has_write)
print("有执行权限：%s" % has_execute) 