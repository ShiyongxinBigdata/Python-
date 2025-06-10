"""
第2章练习题1：变量创建与计算

题目：某学生购买学习用品
- 创建变量存储笔记本单价：15.8元
- 创建变量存储购买数量：3本
- 创建变量存储钢笔单价：12.5元
- 创建变量存储购买数量：2支
- 计算总花费并输出结果

输出格式：购买笔记本花费XX.XX元，购买钢笔花费XX.XX元，总共花费XX.XX元

考查知识点：变量创建、数学运算、浮点数计算
"""

# 学习用品购买计算
# 笔记本相关变量
notebook_price = 15.8  # 笔记本单价
notebook_count = 3     # 购买数量

# 钢笔相关变量
pen_price = 12.5       # 钢笔单价
pen_count = 2          # 购买数量

# 计算各项花费
notebook_cost = notebook_price * notebook_count  # 笔记本总花费
pen_cost = pen_price * pen_count                 # 钢笔总花费
total_cost = notebook_cost + pen_cost            # 总花费

# 输出结果
print("购买笔记本花费%.2f元，购买钢笔花费%.2f元，总共花费%.2f元" % (notebook_cost, pen_cost, total_cost)) 