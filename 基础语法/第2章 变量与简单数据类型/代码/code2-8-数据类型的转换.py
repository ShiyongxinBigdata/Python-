"""
第2章 变量与简单数据类型 - 数据类型的转换
功能：演示Python中各种数据类型之间的相互转换
重点：int()、float()、bool()、str()函数的使用规则和注意事项
"""

# ==================== 转换为整数int ====================
print("=== 转换为整数int ===")

# 字符串str --> 整数int
# 只有纯数字的字符串才能转换为整数
s = '2024'  # 纯数字字符串
n = int(s)  # 转换为整数
print(type(s), type(n))  # 输出：<class 'str'> <class 'int'>

# 浮点数float --> 整数int（会截断小数部分，不是四舍五入）
s1 = 2.23
print(int(s1))  # 输出：2（直接截断小数部分）

# 布尔bool --> 整数int
s2, s3 = True, False  # 布尔值
print(int(s2), int(s3))  # 输出：1 0（True转为1，False转为0）

a , b , c = 10 , 20 , 30
print(a , b , c)

# ==================== 转换为浮点数float ====================
print("\n=== 转换为浮点数float ===")

# 字符串str --> 浮点数float
s = '324.6'  # 有没有小数点都可以转换
print(float(s))  # 输出：324.6

# 整数int --> 浮点数float
n = 2024
print(float(n))  # 输出：2024.0

# 布尔bool --> 浮点数float
print(float(s2), float(s3))  # 输出：1.0      0.0

# ==================== 转换为布尔bool ====================
print("\n=== 转换为布尔bool ===")

# 字符串str --> 布尔bool
# 规则：空字符串转为False，非空字符串转为True
s = '0'  # 非空字符串（即使内容是'0'）
print(bool(s))  # 输出：True

s1 = ''  #   ' ' 有值字符串   ''  ""  空字符串
print(bool(s1))  # 输出：False

print('*' * 20)


# 整数int --> 布尔bool
# 规则：0转为False，非0数字转为True
n = 0
print(bool(n))  # 输出：False

# 浮点数float --> 布尔bool
# 规则：0.0转为False，非0.0数字转为True
f = 0.0
print(bool(f))  # 输出：False

f = 10
print('---' , bool(f))  # 输出：True    规律：有值  -> true    无值 0 ——》false

# ==================== 转换为字符串str ====================
print("\n=== 转换为字符串str ===")

# 整数int --> 字符串str
n = 5
print(str(n))        # 输出：'5'
print(type(str(n)))  # 输出：<class 'str'>

# 浮点数float --> 字符串str
f = 5.3
print(str(f))        # 输出：'5.3'
print(type(str(f)))  # 输出：<class 'str'>
#
# 布尔bool --> 字符串str
a = True
print(type(a))       # 输出：<class 'bool'>
print(type(str(a)))  # 输出：<class 'str'>
print(str(a))  # 'True'
#
# # ==================== 进制的转换 ====================
#   进制：二进制、八进制、十进制、十六进制
# print("\n=== 进制转换 ===")
#
# # 将16进制字符串转换为10进制整数
# s = '1a'  # 16进制字符串，1a在16进制中等于26
# print(int(s, 16))  # 输出：26（第二个参数16表示原字符串是16进制）