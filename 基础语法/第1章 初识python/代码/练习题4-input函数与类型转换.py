"""
练习题4：input函数与类型转换

题目：编写一个简单的购物计算器：
- 提示用户输入商品名称
- 提示用户输入商品单价（需要转换为浮点数）
- 提示用户输入购买数量（需要转换为整数）
- 计算总价并输出结果

输出格式：您购买的[商品名称]，单价[单价]元，数量[数量]个，总价[总价]元

考查知识点：input函数、int()和float()类型转换、简单计算
"""

# 练习题4：input函数与类型转换
# 简单的购物计算器程序

# 获取用户输入
product_name = input("请输入商品名称：")
price = input("请输入商品单价：")
quantity = input("请输入购买数量：")

# 类型转换
price = float(price)      # 转换为浮点数
quantity = int(quantity)  # 转换为整数

# 计算总价
total_price = price * quantity

# 输出结果
print("您购买的" + product_name + "，单价" + str(price) + "元，数量" + str(quantity) + "个，总价" + str(total_price) + "元") 