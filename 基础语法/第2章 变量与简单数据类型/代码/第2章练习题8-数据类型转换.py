"""
第2章练习题8：数据类型转换

题目：学生成绩处理系统
- 用户输入学生姓名（字符串）
- 用户输入数学成绩（需转换为浮点数）
- 用户输入英语成绩（需转换为浮点数）
- 计算平均分
- 判断是否及格（平均分>=60为True，否则为False）
- 将平均分转换为整数（截断小数）
- 将所有信息转换为字符串并输出

输出格式：
请输入学生姓名：张三
请输入数学成绩：85.5
请输入英语成绩：92.0
学生姓名：张三
数学成绩：85.5分
英语成绩：92.0分
平均分：88.75分
是否及格：True
平均分（整数）：88分

考查知识点：input()、float()、int()、bool()、str()转换
"""

# 学生成绩处理系统
# 获取用户输入
name = input("请输入学生姓名：")           # 字符串，无需转换
math_score_str = input("请输入数学成绩：")  # 字符串，需转换为浮点数
english_score_str = input("请输入英语成绩：") # 字符串，需转换为浮点数

# 类型转换：字符串转浮点数
math_score = float(math_score_str)
english_score = float(english_score_str)

# 计算平均分
average_score = (math_score + english_score) / 2

# 判断是否及格（转换为布尔值）
is_passed = average_score >= 60

# 将平均分转换为整数（截断小数部分）
average_int = int(average_score)

# 输出结果（演示各种类型转换）
print("学生姓名：%s" % name)
print("数学成绩：%.1f分" % math_score)
print("英语成绩：%.1f分" % english_score)
print("平均分：%.2f分" % average_score)
print("是否及格：%s" % str(is_passed))  # 布尔值转字符串
print("平均分（整数）：%d分" % average_int) 