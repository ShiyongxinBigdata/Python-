"""
第2章练习题10：进阶综合应用

题目：个人信息管理系统
- 用户输入个人信息：姓名、年龄、身高、体重
- 计算BMI指数（体重/身高²）
- 根据年龄判断是否成年
- 创建个人档案字符串
- 使用字符串切片提取姓氏
- 将所有数值信息进行格式化输出

输出格式：
请输入您的姓名：王小明
请输入您的年龄：25
请输入您的身高（米）：1.75
请输入您的体重（公斤）：70.5

************ 个人档案 ************
姓名：王小明
姓氏：王
年龄：25岁
身高：1.75米
体重：70.5公斤
BMI指数：23.02
是否成年：是
健康状态：正常体重
*********************************

考查知识点：综合运用所有第2章知识点
"""

# 个人信息管理系统
# 获取用户输入
name = input("请输入您的姓名：")
age_str = input("请输入您的年龄：")
height_str = input("请输入您的身高（米）：")
weight_str = input("请输入您的体重（公斤）：")

# 类型转换
age = int(age_str)
height = float(height_str)
weight = float(weight_str)

# 计算BMI指数
bmi = weight / (height * height)

# 判断是否成年
is_adult = age >= 18

# 使用字符串切片提取姓氏（第一个字符）
surname = name[0]

# 根据BMI判断健康状态
if bmi < 18.5:
    health_status = "偏瘦"
elif bmi < 24:
    health_status = "正常体重"
elif bmi < 28:
    health_status = "超重"
else:
    health_status = "肥胖"

# 将布尔值转换为中文
adult_status = "是" if is_adult else "否"

# 输出个人档案
print()  # 空行
print("*" * 12 + " 个人档案 " + "*" * 12)
print("姓名：%s" % name)
print("姓氏：%s" % surname)
print("年龄：%d岁" % age)
print("身高：%.2f米" % height)
print("体重：%.1f公斤" % weight)
print("BMI指数：%.2f" % bmi)
print("是否成年：%s" % adult_status)
print("健康状态：%s" % health_status)
print("*" * 33) 