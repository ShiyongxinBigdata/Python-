"""
第2章 变量与简单数据类型 - 变量的数据类型
功能：演示如何查看和检查变量的数据类型
重点：type()函数和isinstance()函数的使用
"""

# 创建一个包含字母和数字的字符串变量
a = '1234asd'  # 字符串类型，包含数字和字母
a = "1234asd"

# 使用type()函数查看变量的数据类型
print(type(a))  # 输出：<class 'str'>，表示a是字符串类型

# 使用isinstance()函数检查变量是否为指定类型
# isinstance(变量, 类型) 返回True或False
is_flag = isinstance(a , int)
#print(is_flag)  # 输出：False，因为a不是整数类型而是字符串类型
# 函数嵌套：从里往外分析，从外往里书写
print(isinstance(a , int))