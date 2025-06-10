"""
第2章练习题12：图书馆借书系统

题目：图书馆借书信息管理
- 用户输入借书证号、姓名、借书数量、借书天数
- 定义每本书每天的借书费用为0.5元
- 计算总借书费用
- 判断是否为长期借阅（超过30天为True）
- 如果超过30天，额外收取10%的延期费
- 从借书证号中提取前3位和后4位
- 生成借书凭证字符串
- 输出详细的借书信息单

输出格式：
请输入借书证号：B202312345678
请输入借阅者姓名：王小雨
请输入借书数量：5
请输入借书天数：45

************ 借书信息单 ************
借书证号：B202312345678
证号前缀：B20
证号后缀：5678
借阅者姓名：王小雨
借阅者姓氏：王
借书数量：5本
借书天数：45天
每本每天费用：0.50元
基础费用：112.50元
是否长期借阅：是
延期费用：11.25元
总计费用：123.75元
***********************************

考查知识点：用户输入、类型转换、条件判断、字符串切片、数学运算、格式化输出
"""

# 图书馆借书系统
print("欢迎使用图书馆借书系统")
print()

# 获取用户输入
library_card = input("请输入借书证号：")
borrower_name = input("请输入借阅者姓名：")
book_count_str = input("请输入借书数量：")
borrow_days_str = input("请输入借书天数：")

# 类型转换
book_count = int(book_count_str)
borrow_days = int(borrow_days_str)

# 定义借书费用标准
daily_fee_per_book = 0.5  # 每本书每天0.5元

# 计算基础费用
basic_fee = book_count * borrow_days * daily_fee_per_book

# 判断是否为长期借阅
is_long_term = borrow_days > 30

# 计算延期费用
if is_long_term:
    overtime_fee = basic_fee * 0.1  # 10%延期费
else:
    overtime_fee = 0.0

# 计算总费用
total_fee = basic_fee + overtime_fee

# 从借书证号中提取信息
card_prefix = library_card[0:3]  # 前3位
card_suffix = library_card[-4:]  # 后4位

# 提取借阅者姓氏
borrower_surname = borrower_name[0]

# 将布尔值转换为中文
long_term_status = "是" if is_long_term else "否"

# 输出借书信息单
print()
print("*" * 12 + " 借书信息单 " + "*" * 12)
print("借书证号：%s" % library_card)
print("证号前缀：%s" % card_prefix)
print("证号后缀：%s" % card_suffix)
print("借阅者姓名：%s" % borrower_name)
print("借阅者姓氏：%s" % borrower_surname)
print("借书数量：%d本" % book_count)
print("借书天数：%d天" % borrow_days)
print("每本每天费用：%.2f元" % daily_fee_per_book)
print("基础费用：%.2f元" % basic_fee)
print("是否长期借阅：%s" % long_term_status)
print("延期费用：%.2f元" % overtime_fee)
print("总计费用：%.2f元" % total_fee)
print("*" * 35) 