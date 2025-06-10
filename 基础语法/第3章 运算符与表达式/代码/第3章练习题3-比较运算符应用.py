"""
第3章练习题3：比较运算符应用

题目：学生成绩比较系统
- 用户输入三个学生的成绩
- 比较成绩的大小关系
- 使用链式比较判断成绩排序
- 判断是否有相同成绩
- 判断成绩是否在及格范围内

输出格式：
请输入学生A的成绩：85
请输入学生B的成绩：92
请输入学生C的成绩：78
A成绩 < B成绩：True
B成绩 > C成绩：True
A成绩 == C成绩：False
成绩按升序排列：False
所有成绩都及格：True

考查知识点：所有比较运算符、链式比较、布尔值输出
"""

# 学生成绩比较系统
# 获取用户输入
score_a = float(input("请输入学生A的成绩："))
score_b = float(input("请输入学生B的成绩："))
score_c = float(input("请输入学生C的成绩："))

# 基本比较运算
print("A成绩 < B成绩：%s" % (score_a < score_b))
print("B成绩 > C成绩：%s" % (score_b > score_c))
print("A成绩 == C成绩：%s" % (score_a == score_c))
print("A成绩 != B成绩：%s" % (score_a != score_b))
print("A成绩 >= 60：%s" % (score_a >= 60))
print("B成绩 <= 100：%s" % (score_b <= 100))

# 链式比较运算
print("\n=== 链式比较 ===")
# 判断成绩是否按升序排列
ascending_order = score_a < score_b < score_c
print("成绩按升序排列（A<B<C）：%s" % ascending_order)

# 判断成绩是否按降序排列
descending_order = score_a > score_b > score_c
print("成绩按降序排列（A>B>C）：%s" % descending_order)

# 判断所有成绩是否都及格（>=60）
all_passed = 60 <= score_a and 60 <= score_b and 60 <= score_c
print("所有成绩都及格：%s" % all_passed)

# 使用链式比较的简化写法
all_passed_chain = 60 <= score_a >= 60 and 60 <= score_b >= 60 and 60 <= score_c >= 60
print("所有成绩都及格（链式）：%s" % all_passed_chain)

# 判断成绩是否在合理范围内（0-100）
valid_range = 0 <= score_a <= 100 and 0 <= score_b <= 100 and 0 <= score_c <= 100
print("所有成绩都在合理范围：%s" % valid_range)

# 找出最高分和最低分
print("\n=== 成绩分析 ===")
if score_a >= score_b and score_a >= score_c:
    print("最高分是A：%.1f" % score_a)
elif score_b >= score_a and score_b >= score_c:
    print("最高分是B：%.1f" % score_b)
else:
    print("最高分是C：%.1f" % score_c) 