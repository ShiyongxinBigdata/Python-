"""
第2章练习题3：数据类型检查

题目：创建不同类型的变量并检查其数据类型
- 创建一个整数变量：age = 18
- 创建一个浮点数变量：height = 175.5
- 创建一个字符串变量：name = "张三"
- 创建一个布尔变量：is_student = True
- 使用type()函数输出每个变量的数据类型
- 使用isinstance()函数检查每个变量是否为指定类型

输出格式：
age的类型是：<class 'int'>
age是整数类型：True
height的类型是：<class 'float'>
height是浮点数类型：True
... (以此类推)

考查知识点：type()函数、isinstance()函数、数据类型判断
"""
# 声明变量
#age = 18 + 'abc'  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
age = 18
height = 175.5
name = "张三"
is_student = True
# 输出类型
print("age的类型是：" , type(age))
# 判断类型
print("age类型是不是int类型 ： "  , isinstance(age, int))
