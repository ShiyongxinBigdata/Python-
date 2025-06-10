"""
第2章练习题7：字符串索引切片

题目：手机号码处理
- 创建手机号码字符串：phone = "13812345678"
- 输出第1个数字（索引0）
- 输出最后一个数字（负索引）
- 输出前3位数字（切片）
- 输出后4位数字（切片）
- 输出中间4位数字（索引3-6）
- 将手机号码反转
- 每隔一位取一个数字

输出格式：
手机号码：13812345678
第1个数字：1
最后一个数字：8
前3位：138
后4位：5678
中间4位：1234
反转号码：87654321831
每隔一位：1812468

考查知识点：字符串索引、正负索引、切片操作、步长参数
"""

# 手机号码处理
# 创建手机号码字符串
phone = "13812345678"

# 字符串索引操作
first_digit = phone[0]      # 第1个数字
last_digit = phone[-1]     # 最后一个数字

# 字符串切片操作
first_three = phone[0:3]    # 前3位数字
last_four = phone[-4:]      # 后4位数字（从倒数第4位到结尾）
middle_four = phone[3:7]    # 中间4位数字（索引3到6）

# 字符串反转
reversed_phone = phone[::-1]  # 使用负步长反转

# 每隔一位取数字
every_other = phone[::2]      # 步长为2，每隔一位取一个

# 输出结果
print("手机号码：%s" % phone)
print("第1个数字：%s" % first_digit)
print("最后一个数字：%s" % last_digit)
print("前3位：%s" % first_three)
print("后4位：%s" % last_four)
print("中间4位：%s" % middle_four)
print("反转号码：%s" % reversed_phone)
print("每隔一位：%s" % every_other) 