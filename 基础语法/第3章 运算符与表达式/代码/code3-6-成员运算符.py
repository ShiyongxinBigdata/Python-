"""
第3章 运算符与表达式 - 成员运算符
功能：演示成员运算符和身份运算符的使用
重点：in、not in（成员关系）、is、is not（身份比较）
"""

# ==================== 成员运算符 in 和 not in ====================
print("=== 成员运算符 in 和 not in ===")

# in 运算符：检查某个元素是否存在于序列中
print('12' in '123')  # 输出：True，字符串'12'包含在字符串'123'中

# not in 运算符：检查某个元素是否不存在于序列中
print('hi' not in 'hello')  # 输出：True，字符串'hi'不包含在字符串'hello'中

# ==================== 身份运算符 is 和 is not ====================
print("\n=== 身份运算符 is 和 is not ===")

# 创建两个变量
a = 1  # 小整数，Python会缓存
b = 2  # 小整数，Python会缓存

# is 运算符：检查两个变量是否指向同一个对象（比较内存地址）
print(a is b)  # 输出：False，a和b指向不同的对象

# is not 运算符：检查两个变量是否不指向同一个对象
print(a is not b)  # 输出：True，a和b确实不指向同一个对象

# ==================== is 与 == 的区别 ====================
print("\n=== is 与 == 的区别 ===")

# 创建两个相同内容的列表
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(f"list1 == list2: {list1 == list2}")  # 输出：True，内容相同
print(f"list1 is list2: {list1 is list2}")  # 输出：False，不是同一个对象

# 让两个变量指向同一个对象
list3 = list1
print(f"list1 is list3: {list1 is list3}")  # 输出：True，指向同一个对象

# ==================== 特殊情况：小整数缓存 ====================
print("\n=== 特殊情况：小整数缓存 ===")

# Python会缓存-5到256之间的整数
x = 100
y = 100
print(f"x is y: {x is y}")  # 输出：True，小整数被缓存，指向同一个对象

# 大整数不会被缓存
big_x = 1000
big_y = 1000
print(f"big_x is big_y: {big_x is big_y}")  # 输出：False（在某些情况下可能为True）