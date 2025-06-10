"""
第3章练习题4：逻辑运算符应用

题目：用户权限验证系统
- 用户输入年龄、是否为会员、积分
- 使用逻辑运算符判断各种权限
- 演示短路运算的特性
- 综合判断用户等级

权限规则：
- 成年用户：年龄 >= 18
- VIP用户：是会员 且 积分 >= 1000
- 高级用户：(年龄 >= 25 且 积分 >= 500) 或 积分 >= 2000
- 特殊优惠：成年用户 且 (VIP用户 或 积分 >= 800)

考查知识点：and、or、not运算符、短路运算、复合逻辑表达式
"""

# 用户权限验证系统
print("=== 用户权限验证系统 ===")

# 获取用户输入
age = int(input("请输入您的年龄："))
is_member_str = input("是否为会员？(y/n)：")
points = int(input("请输入您的积分："))

# 转换会员状态为布尔值
is_member = is_member_str.lower() == 'y'

print("\n=== 用户信息 ===")
print("年龄：%d岁" % age)
print("会员状态：%s" % ("是" if is_member else "否"))
print("积分：%d分" % points)

# 基本权限判断
print("\n=== 权限判断 ===")

# 成年用户判断
is_adult = age >= 18
print("成年用户：%s" % is_adult)

# VIP用户判断（需要同时满足两个条件）
is_vip = is_member and points >= 1000
print("VIP用户：%s" % is_vip)

# 高级用户判断（复合逻辑表达式）
is_advanced = (age >= 25 and points >= 500) or points >= 2000
print("高级用户：%s" % is_advanced)

# 特殊优惠判断
special_offer = is_adult and (is_vip or points >= 800)
print("享受特殊优惠：%s" % special_offer)

# 逻辑非运算演示
print("\n=== 逻辑非运算 ===")
is_not_member = not is_member
print("非会员用户：%s" % is_not_member)

is_minor = not is_adult
print("未成年用户：%s" % is_minor)

# 短路运算演示
print("\n=== 短路运算演示 ===")

# and短路运算：如果第一个条件为False，不会计算第二个条件
result1 = False and (points > 0)  # 不会检查积分
print("False and (积分>0)：%s" % result1)

# or短路运算：如果第一个条件为True，不会计算第二个条件
result2 = True or (age > 100)  # 不会检查年龄
print("True or (年龄>100)：%s" % result2)

# 复杂的短路运算
result3 = is_member and points >= 500 and age >= 18
print("会员 且 积分>=500 且 成年：%s" % result3)

# 用户等级综合判断
print("\n=== 用户等级 ===")
if is_vip and is_advanced:
    user_level = "钻石用户"
elif is_vip:
    user_level = "VIP用户"
elif is_advanced:
    user_level = "高级用户"
elif is_adult:
    user_level = "普通用户"
else:
    user_level = "新手用户"

print("您的用户等级：%s" % user_level) 