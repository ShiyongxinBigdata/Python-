"""
第2章练习题15：汽车油耗计算

题目：汽车油耗与费用分析系统
- 用户输入车主姓名、车牌号、行驶里程、加油量、油价
- 计算百公里油耗
- 计算本次加油费用
- 计算平均每公里燃油成本
- 判断是否为高油耗车辆（百公里油耗>8L为True）
- 从车牌号中提取地区代码（前2位）和车辆号码（后5位）
- 预估下次加油里程（按百公里油耗计算能跑多少公里）
- 输出详细的油耗分析报告

输出格式：
请输入车主姓名：王师傅
请输入车牌号：京A12345
请输入行驶里程（公里）：350
请输入加油量（升）：28.5
请输入油价（元/升）：7.8

************ 油耗分析报告 ************
车主姓名：王师傅
车主姓氏：王
车牌号：京A12345
地区代码：京A
车辆号码：12345
行驶里程：350公里
加油量：28.50升
油价：7.80元/升
百公里油耗：8.14升
加油费用：222.30元
每公里燃油成本：0.64元
是否高油耗：是
预估续航：350公里
***********************************

考查知识点：用户输入、类型转换、数学运算、字符串切片、布尔判断、格式化输出
"""

# 汽车油耗计算
print("欢迎使用汽车油耗分析系统")
print()

# 获取用户输入
owner_name = input("请输入车主姓名：")
license_plate = input("请输入车牌号：")
mileage_str = input("请输入行驶里程（公里）：")
fuel_amount_str = input("请输入加油量（升）：")
fuel_price_str = input("请输入油价（元/升）：")

# 类型转换
mileage = float(mileage_str)
fuel_amount = float(fuel_amount_str)
fuel_price = float(fuel_price_str)

# 计算百公里油耗
fuel_consumption_per_100km = (fuel_amount / mileage) * 100

# 计算本次加油费用
fuel_cost = fuel_amount * fuel_price

# 计算每公里燃油成本
cost_per_km = fuel_cost / mileage

# 判断是否为高油耗车辆
is_high_consumption = fuel_consumption_per_100km > 8.0

# 从车牌号中提取信息
region_code = license_plate[0:2]   # 前2位地区代码
vehicle_number = license_plate[-5:]  # 后5位车辆号码

# 提取车主姓氏
owner_surname = owner_name[0]

# 预估续航里程（假设油箱还能加满，这里简化处理，假设按当前油耗水平能跑多少公里）
# 这里简化为：如果按当前加的油量计算，能跑的里程
estimated_range = mileage  # 简化处理，实际应该是油箱容量/百公里油耗*100

# 将布尔值转换为中文
high_consumption_status = "是" if is_high_consumption else "否"

# 输出油耗分析报告
print()
print("*" * 12 + " 油耗分析报告 " + "*" * 12)
print("车主姓名：%s" % owner_name)
print("车主姓氏：%s" % owner_surname)
print("车牌号：%s" % license_plate)
print("地区代码：%s" % region_code)
print("车辆号码：%s" % vehicle_number)
print("行驶里程：%.0f公里" % mileage)
print("加油量：%.2f升" % fuel_amount)
print("油价：%.2f元/升" % fuel_price)
print("百公里油耗：%.2f升" % fuel_consumption_per_100km)
print("加油费用：%.2f元" % fuel_cost)
print("每公里燃油成本：%.2f元" % cost_per_km)
print("是否高油耗：%s" % high_consumption_status)
print("预估续航：%.0f公里" % estimated_range)
print("*" * 35) 