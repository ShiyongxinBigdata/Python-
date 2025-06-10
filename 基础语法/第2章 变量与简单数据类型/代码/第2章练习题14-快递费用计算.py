"""
第2章练习题14：快递费用计算

题目：快递公司运费计算系统
- 用户输入寄件人姓名、收件人姓名、包裹重量、寄送距离
- 定义计费标准：首重1公斤内12元，续重每公斤6元
- 定义距离费：500公里内不加收，超过500公里每100公里加收2元
- 计算总运费
- 判断是否为重包裹（重量>5公斤为True）
- 判断是否为长途运输（距离>500公里为True）
- 生成快递单号（使用字符串拼接）
- 从寄件人姓名中提取姓氏
- 输出详细的快递运费清单

输出格式：
请输入寄件人姓名：刘德华
请输入收件人姓名：张学友
请输入包裹重量（公斤）：3.5
请输入寄送距离（公里）：800

************ 快递运费清单 ************
快递单号：EMS20231225001
寄件人：刘德华
寄件人姓氏：刘
收件人：张学友
收件人姓氏：张
包裹重量：3.50公斤
寄送距离：800公里
首重费用：12.00元
续重费用：15.00元
距离附加费：6.00元
总运费：33.00元
是否重包裹：否
是否长途运输：是
***********************************

考查知识点：用户输入、类型转换、条件计算、字符串操作、数学运算、格式化输出
"""

# 快递费用计算
print("欢迎使用快递费用计算系统")
print()

# 获取用户输入
sender_name = input("请输入寄件人姓名：")
receiver_name = input("请输入收件人姓名：")
package_weight_str = input("请输入包裹重量（公斤）：")
distance_str = input("请输入寄送距离（公里）：")

# 类型转换
package_weight = float(package_weight_str)
distance = int(distance_str)

# 定义计费标准
first_weight_fee = 12.0  # 首重1公斤内费用
additional_weight_fee = 6.0  # 续重每公斤费用
distance_threshold = 500  # 距离阈值
distance_fee_per_100km = 2.0  # 超距离每100公里费用

# 计算重量费用
if package_weight <= 1.0:
    # 首重以内
    weight_fee = first_weight_fee
    additional_fee = 0.0
else:
    # 超过首重
    additional_weight = package_weight - 1.0
    additional_fee = additional_weight * additional_weight_fee
    weight_fee = first_weight_fee

# 计算距离附加费
if distance <= distance_threshold:
    distance_fee = 0.0
else:
    extra_distance = distance - distance_threshold
    # 计算超出距离需要多少个100公里（向上取整）
    extra_100km_count = int((extra_distance + 99) / 100)  # 向上取整的简单方法
    distance_fee = extra_100km_count * distance_fee_per_100km

# 计算总运费
total_fee = weight_fee + additional_fee + distance_fee

# 判断是否为重包裹和长途运输
is_heavy_package = package_weight > 5.0
is_long_distance = distance > distance_threshold

# 生成快递单号（字符串拼接）
express_number = "EMS" + "20231225" + "001"

# 提取姓氏
sender_surname = sender_name[0]
receiver_surname = receiver_name[0]

# 将布尔值转换为中文
heavy_package_status = "是" if is_heavy_package else "否"
long_distance_status = "是" if is_long_distance else "否"

# 输出快递运费清单
print()
print("*" * 12 + " 快递运费清单 " + "*" * 12)
print("快递单号：%s" % express_number)
print("寄件人：%s" % sender_name)
print("寄件人姓氏：%s" % sender_surname)
print("收件人：%s" % receiver_name)
print("收件人姓氏：%s" % receiver_surname)
print("包裹重量：%.2f公斤" % package_weight)
print("寄送距离：%d公里" % distance)
print("首重费用：%.2f元" % weight_fee)
print("续重费用：%.2f元" % additional_fee)
print("距离附加费：%.2f元" % distance_fee)
print("总运费：%.2f元" % total_fee)
print("是否重包裹：%s" % heavy_package_status)
print("是否长途运输：%s" % long_distance_status)
print("*" * 35) 