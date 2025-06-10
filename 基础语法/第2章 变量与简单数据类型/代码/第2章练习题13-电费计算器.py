"""
第2章练习题13：电费计算器

题目：家庭电费阶梯计算系统
- 用户输入户主姓名、电表号、本月用电量
- 定义阶梯电价：200度以内0.52元/度，200-400度0.62元/度，400度以上0.88元/度
- 根据用电量计算电费
- 判断是否为高耗电用户（用电量>400度为True）
- 从电表号中提取区域代码（前2位）和用户编号（后6位）
- 计算日均耗电量
- 输出详细的电费账单

输出格式：
请输入户主姓名：陈建国
请输入电表号：AB12345678
请输入本月用电量（度）：520

************ 电费账单 ************
户主姓名：陈建国
户主姓氏：陈
电表号：AB12345678
区域代码：AB
用户编号：345678
本月用电量：520度
第一阶梯费用：104.00元
第二阶梯费用：124.00元
第三阶梯费用：105.60元
总计电费：333.60元
是否高耗电用户：是
日均耗电量：17.33度
*********************************

考查知识点：用户输入、类型转换、条件分支计算、字符串切片、数学运算、格式化输出
"""

# 电费计算器
print("欢迎使用家庭电费计算器")
print()

# 获取用户输入
owner_name = input("请输入户主姓名：")
meter_number = input("请输入电表号：")
electricity_usage_str = input("请输入本月用电量（度）：")

# 类型转换
electricity_usage = float(electricity_usage_str)

# 定义阶梯电价
tier1_price = 0.52  # 200度以内
tier2_price = 0.62  # 200-400度
tier3_price = 0.88  # 400度以上

# 计算各阶梯费用
if electricity_usage <= 200:
    # 第一阶梯
    tier1_fee = electricity_usage * tier1_price
    tier2_fee = 0.0
    tier3_fee = 0.0
elif electricity_usage <= 400:
    # 第一、二阶梯
    tier1_fee = 200 * tier1_price
    tier2_fee = (electricity_usage - 200) * tier2_price
    tier3_fee = 0.0
else:
    # 三个阶梯都有
    tier1_fee = 200 * tier1_price
    tier2_fee = 200 * tier2_price
    tier3_fee = (electricity_usage - 400) * tier3_price

# 计算总电费
total_fee = tier1_fee + tier2_fee + tier3_fee

# 判断是否为高耗电用户
is_high_consumer = electricity_usage > 400

# 从电表号中提取信息
area_code = meter_number[0:2]     # 前2位区域代码
user_code = meter_number[-6:]     # 后6位用户编号

# 提取户主姓氏
owner_surname = owner_name[0]

# 计算日均耗电量（按30天计算）
daily_usage = electricity_usage / 30

# 将布尔值转换为中文
high_consumer_status = "是" if is_high_consumer else "否"

# 输出电费账单
print()
print("*" * 12 + " 电费账单 " + "*" * 12)
print("户主姓名：%s" % owner_name)
print("户主姓氏：%s" % owner_surname)
print("电表号：%s" % meter_number)
print("区域代码：%s" % area_code)
print("用户编号：%s" % user_code)
print("本月用电量：%.0f度" % electricity_usage)
print("第一阶梯费用：%.2f元" % tier1_fee)
print("第二阶梯费用：%.2f元" % tier2_fee)
print("第三阶梯费用：%.2f元" % tier3_fee)
print("总计电费：%.2f元" % total_fee)
print("是否高耗电用户：%s" % high_consumer_status)
print("日均耗电量：%.2f度" % daily_usage)
print("*" * 33) 