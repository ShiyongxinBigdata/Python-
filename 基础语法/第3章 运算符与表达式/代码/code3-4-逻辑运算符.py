"""
第3章 运算符与表达式 - 逻辑运算符
功能：演示逻辑运算符and、or、not的使用和短路运算特性
重点：逻辑与、逻辑或、逻辑非、短路运算、运算优先级
"""

# ==================== 逻辑与运算符 and ====================
print("=== 逻辑与运算符 and ===")

# 基本的and运算（两个操作数都为True时结果才为True）
print(True and False)  # 输出：False，有一个为False，结果为False
print(True and True)   # 输出：True，两个都为True，结果为True

# 多个and运算（所有操作数都为True时结果才为True）
print(True and False and True)  # 输出：False，有False存在，结果为False

# 混合表达式的and运算
print(1 == 1 and True and 2 < 3)  # 输出：True，所有条件都为True

# and的短路运算特性（返回第一个假值或最后一个真值）
print('hello' and 'hi')  # 输出：'hi'，两个都为真值，返回最后一个
print('' and 'hi')       # 输出：''，空字符串为假值，短路返回第一个假值
print(False and 'hi')    # 输出：False，False为假值，短路返回False
print(0 and 1)           # 输出：0，0为假值，短路返回0

# ==================== 逻辑或运算符 or ====================
print("\n=== 逻辑或运算符 or ===")

# 基本的or运算（有一个操作数为True时结果就为True）
print(True or False)   # 输出：True，有一个为True，结果为True
print(False or False or True)  # 输出：True，有一个为True，结果为True

# or的短路运算特性（返回第一个真值或最后一个假值）
print(1 or 0)          # 输出：1，1为真值，短路返回第一个真值
print(2024 or 2025 or 0)  # 输出：2024，2024为真值，短路返回第一个真值
print(0 or '' or 888)  # 输出：888，前两个都为假值，返回第一个真值

# ==================== 逻辑非运算符 not ====================
print("\n=== 逻辑非运算符 not ===")

# not运算符（取反操作）
print(not True)   # 输出：False，True的反面是False
print(not 1)      # 输出：False，1为真值，取反为False
print(not '')     # 输出：True，空字符串为假值，取反为True

# ==================== 运算优先级 ====================
print("\n=== 运算优先级：not > and > or ===")

# 优先级演示：not > and > or
print(True and False and not False)  # 输出：False，先算not False=True，再算True and False and True=False
print(True or False and True or False)  # 输出：True，先算False and True=False，再算True or False or False=True