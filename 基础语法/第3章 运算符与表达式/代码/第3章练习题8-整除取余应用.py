"""
第3章练习题8：整除取余应用

题目：时间转换器
- 用户输入总秒数
- 将秒数转换为时、分、秒格式
- 计算天数、小时、分钟、秒数
- 应用整除和取余运算解决实际问题

输出格式：
请输入总秒数：3725
3725秒 = 1小时2分5秒
详细转换：
总秒数：3725秒
小时数：1小时 (3725 // 3600)
剩余秒数：125秒 (3725 % 3600)
分钟数：2分钟 (125 // 60)
最终秒数：5秒 (125 % 60)

考查知识点：整除运算符//、取余运算符%、实际问题解决
"""

# 时间转换器
print("=== 时间转换器 ===")

# 获取用户输入
total_seconds = int(input("请输入总秒数："))

# 时间单位常量
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600
SECONDS_PER_DAY = 86400

# 方法1：逐步转换（详细过程）
print("\n=== 详细转换过程 ===")

# 计算小时数
hours = total_seconds // SECONDS_PER_HOUR
remaining_after_hours = total_seconds % SECONDS_PER_HOUR

print("总秒数：%d秒" % total_seconds)
print("小时数：%d小时 (%d // %d)" % (hours, total_seconds, SECONDS_PER_HOUR))
print("剩余秒数：%d秒 (%d %% %d)" % (remaining_after_hours, total_seconds, SECONDS_PER_HOUR))

# 计算分钟数
minutes = remaining_after_hours // SECONDS_PER_MINUTE
final_seconds = remaining_after_hours % SECONDS_PER_MINUTE

print("分钟数：%d分钟 (%d // %d)" % (minutes, remaining_after_hours, SECONDS_PER_MINUTE))
print("最终秒数：%d秒 (%d %% %d)" % (final_seconds, remaining_after_hours, SECONDS_PER_MINUTE))

# 输出最终结果
print("\n=== 转换结果 ===")
print("%d秒 = %d小时%d分%d秒" % (total_seconds, hours, minutes, final_seconds))

# 方法2：包含天数的完整转换
print("\n=== 完整时间转换（包含天数）===")

# 计算天数
days = total_seconds // SECONDS_PER_DAY
remaining_after_days = total_seconds % SECONDS_PER_DAY

# 计算小时数（从剩余秒数中）
hours_in_day = remaining_after_days // SECONDS_PER_HOUR
remaining_after_hours_in_day = remaining_after_days % SECONDS_PER_HOUR

# 计算分钟数
minutes_in_hour = remaining_after_hours_in_day // SECONDS_PER_MINUTE
seconds_final = remaining_after_hours_in_day % SECONDS_PER_MINUTE

print("%d秒 = %d天%d小时%d分%d秒" % (total_seconds, days, hours_in_day, minutes_in_hour, seconds_final))

# 其他整除取余应用示例
print("\n=== 其他应用示例 ===")

# 1. 分页计算
total_items = int(input("请输入总项目数："))
items_per_page = int(input("请输入每页显示项目数："))

total_pages = total_items // items_per_page
if total_items % items_per_page != 0:
    total_pages += 1  # 如果有余数，需要额外一页

remaining_items = total_items % items_per_page

print("分页结果：")
print("总页数：%d页" % total_pages)
print("最后一页项目数：%d个" % (remaining_items if remaining_items != 0 else items_per_page))

# 2. 钱币找零
print("\n--- 钱币找零计算 ---")
amount = int(input("请输入找零金额（分）："))

# 人民币面额（分）
denominations = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 1]
denomination_names = ["100元", "50元", "20元", "10元", "5元", "2元", "1元", "5角", "2角", "1角", "5分", "1分"]

print("找零方案：")
remaining = amount

for i, denom in enumerate(denominations):
    count = remaining // denom
    if count > 0:
        print("%s：%d张" % (denomination_names[i], count))
        remaining = remaining % denom

if remaining == 0:
    print("找零完成！")
else:
    print("剩余：%d分（无法找零）" % remaining)

# 3. 数字反转
print("\n--- 数字反转 ---")
number = int(input("请输入一个正整数："))
original_number = number
reversed_number = 0

print("反转过程：")
while number > 0:
    digit = number % 10  # 取最后一位数字
    reversed_number = reversed_number * 10 + digit  # 构建反转数字
    number = number // 10  # 去掉最后一位数字
    print("当前数字：%d，取出：%d，反转结果：%d" % (number, digit, reversed_number))

print("原数字：%d" % original_number)
print("反转后：%d" % reversed_number)

# 4. 判断回文数
is_palindrome = original_number == reversed_number
print("是否为回文数：%s" % is_palindrome) 