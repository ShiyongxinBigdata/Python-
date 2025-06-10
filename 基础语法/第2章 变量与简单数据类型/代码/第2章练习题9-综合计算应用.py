"""
第2章练习题9：综合计算应用

题目：餐厅点餐系统
- 定义菜品价格：宫保鸡丁 28.5元，麻婆豆腐 18.0元，米饭 3.0元
- 用户输入各菜品数量
- 计算小计金额
- 应用8.8折优惠
- 计算最终金额
- 输出详细账单

输出格式：
请输入宫保鸡丁数量：2
请输入麻婆豆腐数量：1
请输入米饭数量：3
========== 餐厅账单 ==========
宫保鸡丁 x2 = 57.00元
麻婆豆腐 x1 = 18.00元
米饭 x3 = 9.00元
小计：84.00元
优惠折扣：8.8折
最终金额：73.92元
============================

考查知识点：变量创建、用户输入、类型转换、数学运算、格式化输出
"""

# 餐厅点餐系统
# 定义菜品价格
gongbao_price = 28.5    # 宫保鸡丁单价
mapo_price = 18.0       # 麻婆豆腐单价
rice_price = 3.0        # 米饭单价

# 获取用户输入的数量
gongbao_count = int(input("请输入宫保鸡丁数量："))
mapo_count = int(input("请输入麻婆豆腐数量："))
rice_count = int(input("请输入米饭数量："))

# 计算各菜品小计
gongbao_total = gongbao_price * gongbao_count
mapo_total = mapo_price * mapo_count
rice_total = rice_price * rice_count

# 计算总小计
subtotal = gongbao_total + mapo_total + rice_total

# 应用8.8折优惠
discount = 0.88
final_amount = subtotal * discount

# 输出详细账单
print("=" * 10 + " 餐厅账单 " + "=" * 10)
print("宫保鸡丁 x%d = %.2f元" % (gongbao_count, gongbao_total))
print("麻婆豆腐 x%d = %.2f元" % (mapo_count, mapo_total))
print("米饭 x%d = %.2f元" % (rice_count, rice_total))
print("小计：%.2f元" % subtotal)
print("优惠折扣：%.1f折" % (discount * 10))
print("最终金额：%.2f元" % final_amount)
print("=" * 28) 