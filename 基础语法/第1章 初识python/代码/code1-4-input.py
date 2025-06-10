"""
    控制台接收用户的键盘输入 ： input() 函数
    1.Python变量值的数据类型：
    （1）str  字符串
    （2）int 整数
    （3）float 小数
    2.数据类型转换：
        （1）int(整数字符串)函数
        （2）str(整数)函数
        （3）float(小数字符串)函数
"""

# 任务1
# args = input() # 输入一个字符串，回车代表输入结束
# print(args)

# 任务2
name = input("请输入你的名字：")  # "请输入你的名字："   友好提示
print(type(name) , name)   # <class 'str'> 马百祥      str  字符串类型

# # 任务3
age = input("请输入你的年龄：")    #   18    ‘18’    abc
# type(age)  : 显示当前变量类型
print(type(age) , age)  # <class 'str'> 18    输入数字，input函数也当做字符串处理

# 数据类型转换
# 给age变量进行重新赋值，新值会覆盖旧值
# int(age) 函数： 将数字字符串转换为整数     ‘18’ -》 18
age = int(age)   # ValueError: invalid literal for int() with base 10: 'abc'   如果输入的不是数字，就会报错
print(type(age) , age) # <class 'int'> 18

score = input("请输入你的分数：")
print(type(score) , score) # <class 'str'> 99.99
# float(score) 函数： 将小数字符串转换为浮点类型（小数类型）
score = float(score)
print(type(score) , score) # <class 'float'> 99.99999

# 变量的算术运算
year = 2024
# print(type(year))
birth = year - age
print("你的出生年份是", birth)
birth = year + age
print("你的出生年份是", birth)
result = age * 10
print(result) # 180
result = age / 2
print(result) # 9.0   除法运算，默认结果为小数类型