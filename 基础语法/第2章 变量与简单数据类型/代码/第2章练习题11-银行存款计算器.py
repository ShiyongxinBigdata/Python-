"""
第2章练习题11：银行存款计算器

题目：银行定期存款收益计算
- 用户输入客户姓名、存款金额、存款年限
- 定义年利率为3.5%
- 计算到期本息总额（本金+利息）
- 计算纯利息收益
- 判断是否为大额存款（>=50000为True）
- 提取客户姓氏
- 计算月均收益
- 输出详细的存款收益报告

输出格式：
请输入客户姓名：李明华
请输入存款金额（元）：80000
请输入存款年限（年）：3

************ 存款收益报告 ************
客户姓名：李明华
客户姓氏：李
存款金额：80000.00元
存款年限：3年
年利率：3.50%
利息收益：8400.00元
到期本息：88400.00元
是否大额存款：是
月均收益：233.33元
***********************************

考查知识点：用户输入、类型转换、数学运算、布尔判断、字符串切片、格式化输出
"""

# 银行存款计算器
print("欢迎使用银行存款计算器")
print()

# 获取用户输入
customer_name = input("请输入客户姓名：")
deposit_amount_str = input("请输入存款金额（元）：")
deposit_years_str = input("请输入存款年限（年）：")

# 类型转换
deposit_amount = float(deposit_amount_str)
deposit_years = int(deposit_years_str)

# 定义年利率
annual_rate = 0.035  # 3.5%

# 计算利息和本息总额
interest = deposit_amount * annual_rate * deposit_years
total_amount = deposit_amount + interest

# 判断是否为大额存款
is_large_deposit = deposit_amount >= 50000

# 提取客户姓氏
surname = customer_name[0]

# 计算月均收益
monthly_income = interest / (deposit_years * 12)

# 将布尔值转换为中文
large_deposit_status = "是" if is_large_deposit else "否"

# 输出存款收益报告
print()
print("*" * 12 + " 存款收益报告 " + "*" * 12)
print("客户姓名：%s" % customer_name)
print("客户姓氏：%s" % surname)
print("存款金额：%.2f元" % deposit_amount)
print("存款年限：%d年" % deposit_years)
print("年利率：%.2f%%" % (annual_rate * 100))
print("利息收益：%.2f元" % interest)
print("到期本息：%.2f元" % total_amount)
print("是否大额存款：%s" % large_deposit_status)
print("月均收益：%.2f元" % monthly_income)
print("*" * 35) 