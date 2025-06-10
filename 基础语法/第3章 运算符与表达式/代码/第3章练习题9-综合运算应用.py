"""
第3章练习题9：综合运算应用

题目：学生成绩管理系统
- 输入多个学生的成绩信息
- 使用各种运算符进行成绩分析
- 计算平均分、等级判定、排名比较
- 综合运用算数、比较、逻辑、赋值运算符

功能：
1. 成绩录入和基本计算
2. 等级判定（优秀、良好、及格、不及格）
3. 成绩统计分析
4. 奖学金评定

考查知识点：多种运算符综合应用、复杂逻辑判断、实际问题解决
"""

# 学生成绩管理系统
print("=== 学生成绩管理系统 ===")

# 获取学生信息
student_count = int(input("请输入学生人数："))
print("请依次输入每个学生的成绩信息：")

# 存储学生数据的变量
total_score = 0
highest_score = 0
lowest_score = 100
excellent_count = 0  # 优秀人数（>=90）
good_count = 0       # 良好人数（80-89）
pass_count = 0       # 及格人数（60-79）
fail_count = 0       # 不及格人数（<60）

# 逐个录入学生成绩
for i in range(student_count):
    print("\n--- 第%d个学生 ---" % (i + 1))
    
    # 获取基本信息
    name = input("姓名：")
    chinese = float(input("语文成绩："))
    math = float(input("数学成绩："))
    english = float(input("英语成绩："))
    
    # 计算总分和平均分
    student_total = chinese + math + english
    student_average = student_total / 3
    
    # 更新统计数据（使用复合赋值运算符）
    total_score += student_total
    
    # 更新最高分和最低分（使用比较运算符）
    if student_average > highest_score:
        highest_score = student_average
        top_student = name
    
    if student_average < lowest_score:
        lowest_score = student_average
        bottom_student = name
    
    # 等级判定（使用比较运算符和逻辑运算符）
    if student_average >= 90:
        grade = "优秀"
        excellent_count += 1
    elif student_average >= 80:  # 等价于 student_average >= 80 and student_average < 90
        grade = "良好"
        good_count += 1
    elif student_average >= 60:
        grade = "及格"
        pass_count += 1
    else:
        grade = "不及格"
        fail_count += 1
    
    # 单科成绩分析
    best_subject = "语文" if chinese >= math and chinese >= english else ("数学" if math >= english else "英语")
    worst_subject = "语文" if chinese <= math and chinese <= english else ("数学" if math <= english else "英语")
    
    # 是否偏科判断（最高分与最低分差距超过20分）
    max_score = max(chinese, math, english)
    min_score = min(chinese, math, english)
    is_unbalanced = max_score - min_score > 20
    
    # 奖学金评定（使用复合逻辑表达式）
    # 条件：平均分>=85 且 单科成绩都>=80 且 不偏科
    scholarship_eligible = (student_average >= 85 and 
                          chinese >= 80 and math >= 80 and english >= 80 and 
                          not is_unbalanced)
    
    # 输出学生成绩报告
    print("\n=== %s的成绩报告 ===" % name)
    print("语文：%.1f分，数学：%.1f分，英语：%.1f分" % (chinese, math, english))
    print("总分：%.1f分，平均分：%.1f分" % (student_total, student_average))
    print("等级：%s" % grade)
    print("最强科目：%s，最弱科目：%s" % (best_subject, worst_subject))
    print("是否偏科：%s" % ("是" if is_unbalanced else "否"))
    print("奖学金资格：%s" % ("符合" if scholarship_eligible else "不符合"))

# 班级整体统计
print("\n" + "="*50)
print("=== 班级成绩统计 ===")

class_average = total_score / (student_count * 3)
pass_rate = (excellent_count + good_count + pass_count) / student_count * 100
excellent_rate = excellent_count / student_count * 100

print("班级总人数：%d人" % student_count)
print("班级平均分：%.2f分" % class_average)
print("及格率：%.1f%%" % pass_rate)
print("优秀率：%.1f%%" % excellent_rate)
print("最高平均分：%.1f分（%s）" % (highest_score, top_student))
print("最低平均分：%.1f分（%s）" % (lowest_score, bottom_student))

# 成绩分布统计
print("\n=== 成绩分布 ===")
print("优秀（90分以上）：%d人" % excellent_count)
print("良好（80-89分）：%d人" % good_count)
print("及格（60-79分）：%d人" % pass_count)
print("不及格（60分以下）：%d人" % fail_count)

# 班级评价（使用复合逻辑判断）
print("\n=== 班级评价 ===")
if excellent_rate >= 30 and pass_rate >= 95:
    class_level = "优秀班级"
elif excellent_rate >= 20 and pass_rate >= 90:
    class_level = "良好班级"
elif pass_rate >= 80:
    class_level = "普通班级"
else:
    class_level = "需要改进"

print("班级等级：%s" % class_level)

# 改进建议
if fail_count > 0:
    print("建议：关注不及格学生，加强辅导")
if excellent_rate < 20:
    print("建议：提高教学质量，培养更多优秀学生")
if pass_rate < 90:
    print("建议：整体提升班级成绩水平")

# 位运算应用：学生状态标记
print("\n=== 学生状态标记（位运算应用）===")
# 使用位运算标记学生状态
EXCELLENT = 1    # 001 优秀
BALANCED = 2     # 010 不偏科
SCHOLARSHIP = 4  # 100 奖学金

# 示例：假设第一个学生的状态
student_status = 0
if excellent_count > 0:  # 假设有优秀学生
    student_status |= EXCELLENT  # 设置优秀标记
    student_status |= BALANCED   # 设置不偏科标记
    student_status |= SCHOLARSHIP # 设置奖学金标记

print("学生状态码：%d（二进制：%s）" % (student_status, bin(student_status)[2:]))
print("是否优秀：%s" % bool(student_status & EXCELLENT))
print("是否不偏科：%s" % bool(student_status & BALANCED))
print("是否获得奖学金：%s" % bool(student_status & SCHOLARSHIP)) 