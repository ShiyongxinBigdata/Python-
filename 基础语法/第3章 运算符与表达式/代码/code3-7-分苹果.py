"""
第3章 运算符与表达式 - 分苹果
功能：使用整除和取余运算解决实际分配问题
场景：将苹果平均分给学生，计算每人分得数量和剩余数量
重点：整除运算符//、取余运算符%的实际应用
"""

# 分苹果问题
# 问题描述：有14个苹果，要平均分给4个学生，每人能分几个？还剩几个？

total = 14  # 苹果总数
stu = 4     # 学生人数

# 计算每个学生能分到的苹果数量（整除运算）
apples_per_student = total // stu  # 14 // 4 = 3
print(apples_per_student)  # 输出：3，每个学生分到3个苹果

# 计算分完后已分出的苹果总数
distributed_apples = total // stu * stu  # 3 * 4 = 12
print(distributed_apples)  # 输出：12，总共分出了12个苹果

# 计算剩余的苹果数量（取余运算）
remaining_apples = total - (total // stu * stu)  # 14 - 12 = 2
print(remaining_apples)  # 输出：2，剩余2个苹果

# 更简洁的计算剩余苹果的方法
# remaining_apples = total % stu  # 直接使用取余运算：14 % 4 = 2

# 总结：
# 整除运算 // 用于计算平均分配的数量
# 取余运算 % 用于计算分配后的剩余数量