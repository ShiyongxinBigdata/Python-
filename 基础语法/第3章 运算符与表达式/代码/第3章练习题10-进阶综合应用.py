"""
第3章练习题10：进阶综合应用

题目：智能计算器与数据分析系统
- 实现一个多功能计算器
- 支持基本运算、进制转换、统计分析
- 使用所有类型的运算符
- 模拟真实的数据处理场景

功能模块：
1. 基础计算器（四则运算、幂运算、取余等）
2. 进制转换器（二进制、八进制、十六进制）
3. 数据统计分析（平均值、最值、方差等）
4. 逻辑表达式计算器
5. 位运算工具

考查知识点：所有运算符的综合运用、复杂算法实现、实际问题解决
"""

# 智能计算器与数据分析系统
print("="*60)
print("           智能计算器与数据分析系统")
print("="*60)

def display_menu():
    """显示主菜单"""
    print("\n请选择功能模块：")
    print("1. 基础计算器")
    print("2. 进制转换器")
    print("3. 数据统计分析")
    print("4. 逻辑表达式计算器")
    print("5. 位运算工具")
    print("6. 综合应用示例")
    print("0. 退出系统")

def basic_calculator():
    """基础计算器模块"""
    print("\n=== 基础计算器 ===")
    
    # 获取两个操作数
    num1 = float(input("请输入第一个数："))
    num2 = float(input("请输入第二个数："))
    
    print("\n计算结果：")
    print("%.2f + %.2f = %.2f" % (num1, num2, num1 + num2))
    print("%.2f - %.2f = %.2f" % (num1, num2, num1 - num2))
    print("%.2f * %.2f = %.2f" % (num1, num2, num1 * num2))
    
    if num2 != 0:
        print("%.2f / %.2f = %.2f" % (num1, num2, num1 / num2))
        print("%.2f // %.2f = %.2f" % (num1, num2, num1 // num2))
        print("%.2f %% %.2f = %.2f" % (num1, num2, num1 % num2))
    else:
        print("除数不能为0！")
    
    print("%.2f ** %.2f = %.2f" % (num1, num2, num1 ** num2))
    
    # 复合表达式计算
    complex_expr = (num1 + num2) * (num1 - num2) + num1 ** 2 / (num2 + 1)
    print("复合表达式 (a+b)*(a-b)+a²/(b+1) = %.2f" % complex_expr)

def base_converter():
    """进制转换器模块"""
    print("\n=== 进制转换器 ===")
    
    number = int(input("请输入一个十进制整数："))
    
    print("\n转换结果：")
    print("十进制：%d" % number)
    print("二进制：%s" % bin(number))
    print("八进制：%s" % oct(number))
    print("十六进制：%s" % hex(number))
    
    # 手动实现二进制转换（使用位运算）
    print("\n手动二进制转换过程：")
    temp = abs(number)
    binary_digits = []
    
    if temp == 0:
        binary_digits.append('0')
    else:
        while temp > 0:
            digit = temp & 1  # 使用位运算获取最低位
            binary_digits.append(str(digit))
            temp >>= 1  # 右移一位
            print("当前数：%d，最低位：%d" % (temp, digit))
    
    manual_binary = ''.join(reversed(binary_digits))
    if number < 0:
        manual_binary = '-' + manual_binary
    
    print("手动转换结果：%s" % manual_binary)

def data_analyzer():
    """数据统计分析模块"""
    print("\n=== 数据统计分析 ===")
    
    # 获取数据
    data_count = int(input("请输入数据个数："))
    data_list = []
    data_sum = 0
    
    print("请输入%d个数据：" % data_count)
    for i in range(data_count):
        value = float(input("第%d个数据：" % (i + 1)))
        data_list.append(value)
        data_sum += value  # 使用复合赋值运算符
    
    # 基本统计
    average = data_sum / data_count
    maximum = data_list[0]
    minimum = data_list[0]
    
    # 找最大值和最小值
    for value in data_list:
        if value > maximum:
            maximum = value
        if value < minimum:
            minimum = value
    
    # 计算方差
    variance_sum = 0
    for value in data_list:
        variance_sum += (value - average) ** 2
    variance = variance_sum / data_count
    std_deviation = variance ** 0.5
    
    # 数据分类统计
    positive_count = 0
    negative_count = 0
    zero_count = 0
    even_count = 0
    odd_count = 0
    
    for value in data_list:
        # 正负零统计
        if value > 0:
            positive_count += 1
        elif value < 0:
            negative_count += 1
        else:
            zero_count += 1
        
        # 奇偶统计（仅对整数）
        if value == int(value):  # 是整数
            if int(value) & 1:  # 使用位运算判断奇偶
                odd_count += 1
            else:
                even_count += 1
    
    # 输出统计结果
    print("\n=== 统计结果 ===")
    print("数据个数：%d" % data_count)
    print("数据总和：%.2f" % data_sum)
    print("平均值：%.2f" % average)
    print("最大值：%.2f" % maximum)
    print("最小值：%.2f" % minimum)
    print("极差：%.2f" % (maximum - minimum))
    print("方差：%.2f" % variance)
    print("标准差：%.2f" % std_deviation)
    
    print("\n=== 数据分类 ===")
    print("正数：%d个，负数：%d个，零：%d个" % (positive_count, negative_count, zero_count))
    print("整数中奇数：%d个，偶数：%d个" % (odd_count, even_count))
    
    # 数据质量评估
    is_balanced = abs(positive_count - negative_count) <= 1
    is_diverse = (maximum - minimum) > average
    has_outliers = any(abs(value - average) > 2 * std_deviation for value in data_list)
    
    print("\n=== 数据质量评估 ===")
    print("数据平衡性：%s" % ("良好" if is_balanced else "不平衡"))
    print("数据多样性：%s" % ("丰富" if is_diverse else "单一"))
    print("是否有异常值：%s" % ("是" if has_outliers else "否"))

def logic_calculator():
    """逻辑表达式计算器"""
    print("\n=== 逻辑表达式计算器 ===")
    
    # 获取逻辑值
    print("请输入逻辑值（True/False或1/0）：")
    a_input = input("变量A：").strip().lower()
    b_input = input("变量B：").strip().lower()
    c_input = input("变量C：").strip().lower()
    
    # 转换为布尔值
    def to_bool(value):
        return value in ['true', '1', 'yes', 'y']
    
    a = to_bool(a_input)
    b = to_bool(b_input)
    c = to_bool(c_input)
    
    print("\n输入值：A=%s, B=%s, C=%s" % (a, b, c))
    
    # 基本逻辑运算
    print("\n=== 基本逻辑运算 ===")
    print("A and B = %s" % (a and b))
    print("A or B = %s" % (a or b))
    print("not A = %s" % (not a))
    print("A xor B = %s" % (a != b))  # 异或运算
    
    # 复合逻辑表达式
    print("\n=== 复合逻辑表达式 ===")
    expr1 = a and b or c
    expr2 = (a or b) and c
    expr3 = not (a and b) or c
    expr4 = a and (b or not c)
    
    print("A and B or C = %s" % expr1)
    print("(A or B) and C = %s" % expr2)
    print("not (A and B) or C = %s" % expr3)
    print("A and (B or not C) = %s" % expr4)
    
    # 德摩根定律验证
    print("\n=== 德摩根定律验证 ===")
    demorgan1_left = not (a and b)
    demorgan1_right = (not a) or (not b)
    demorgan2_left = not (a or b)
    demorgan2_right = (not a) and (not b)
    
    print("not (A and B) = %s" % demorgan1_left)
    print("(not A) or (not B) = %s" % demorgan1_right)
    print("德摩根定律1验证：%s" % (demorgan1_left == demorgan1_right))
    
    print("not (A or B) = %s" % demorgan2_left)
    print("(not A) and (not B) = %s" % demorgan2_right)
    print("德摩根定律2验证：%s" % (demorgan2_left == demorgan2_right))

def bit_operations():
    """位运算工具"""
    print("\n=== 位运算工具 ===")
    
    num1 = int(input("请输入第一个整数："))
    num2 = int(input("请输入第二个整数："))
    
    print("\n=== 位运算结果 ===")
    print("%d 的二进制：%s" % (num1, bin(num1)))
    print("%d 的二进制：%s" % (num2, bin(num2)))
    
    print("\n按位运算：")
    print("%d & %d = %d (二进制：%s)" % (num1, num2, num1 & num2, bin(num1 & num2)))
    print("%d | %d = %d (二进制：%s)" % (num1, num2, num1 | num2, bin(num1 | num2)))
    print("%d ^ %d = %d (二进制：%s)" % (num1, num2, num1 ^ num2, bin(num1 ^ num2)))
    print("~%d = %d" % (num1, ~num1))
    
    print("\n移位运算：")
    print("%d << 2 = %d (左移2位)" % (num1, num1 << 2))
    print("%d >> 1 = %d (右移1位)" % (num1, num1 >> 1))
    
    # 位运算应用
    print("\n=== 位运算应用 ===")
    
    # 1. 快速判断奇偶
    print("奇偶判断：")
    print("%d 是 %s" % (num1, "奇数" if num1 & 1 else "偶数"))
    print("%d 是 %s" % (num2, "奇数" if num2 & 1 else "偶数"))
    
    # 2. 快速乘除法
    print("\n快速乘除法：")
    print("%d * 8 = %d (左移3位)" % (num1, num1 << 3))
    print("%d / 4 = %d (右移2位)" % (num1, num1 >> 2))
    
    # 3. 交换两个数
    print("\n异或交换：")
    a, b = num1, num2
    print("交换前：a=%d, b=%d" % (a, b))
    a ^= b
    b ^= a
    a ^= b
    print("交换后：a=%d, b=%d" % (a, b))

def comprehensive_example():
    """综合应用示例"""
    print("\n=== 综合应用示例：密码强度检测器 ===")
    
    password = input("请输入要检测的密码：")
    
    # 密码强度评分系统
    score = 0
    feedback = []
    
    # 长度检查
    length = len(password)
    if length >= 12:
        score += 25
        feedback.append("长度优秀（≥12位）")
    elif length >= 8:
        score += 15
        feedback.append("长度良好（8-11位）")
    elif length >= 6:
        score += 5
        feedback.append("长度一般（6-7位）")
    else:
        feedback.append("长度过短（<6位）")
    
    # 字符类型检查（使用成员运算符）
    has_lower = any(c in 'abcdefghijklmnopqrstuvwxyz' for c in password)
    has_upper = any(c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in password)
    has_digit = any(c in '0123456789' for c in password)
    has_special = any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password)
    
    char_types = sum([has_lower, has_upper, has_digit, has_special])
    score += char_types * 10
    
    if has_lower:
        feedback.append("包含小写字母")
    if has_upper:
        feedback.append("包含大写字母")
    if has_digit:
        feedback.append("包含数字")
    if has_special:
        feedback.append("包含特殊字符")
    
    # 复杂度检查（使用逻辑运算符）
    is_complex = has_lower and has_upper and has_digit and has_special
    if is_complex:
        score += 20
        feedback.append("字符类型丰富")
    
    # 重复字符检查
    has_repeat = any(password.count(c) > 2 for c in set(password))
    if not has_repeat:
        score += 10
        feedback.append("无过多重复字符")
    else:
        feedback.append("存在重复字符")
    
    # 连续字符检查
    has_sequence = False
    for i in range(len(password) - 2):
        if (ord(password[i]) + 1 == ord(password[i+1]) and 
            ord(password[i+1]) + 1 == ord(password[i+2])):
            has_sequence = True
            break
    
    if not has_sequence:
        score += 10
        feedback.append("无连续字符序列")
    else:
        feedback.append("存在连续字符序列")
    
    # 强度等级判定（使用比较运算符）
    if score >= 80:
        strength = "非常强"
    elif score >= 60:
        strength = "强"
    elif score >= 40:
        strength = "中等"
    elif score >= 20:
        strength = "弱"
    else:
        strength = "非常弱"
    
    # 输出结果
    print("\n=== 密码强度分析结果 ===")
    print("密码：%s" % ('*' * len(password)))  # 隐藏密码
    print("长度：%d位" % length)
    print("得分：%d/100" % score)
    print("强度等级：%s" % strength)
    
    print("\n详细分析：")
    for item in feedback:
        print("✓ %s" % item)
    
    # 改进建议
    print("\n改进建议：")
    if length < 8:
        print("• 增加密码长度至少8位")
    if not has_lower:
        print("• 添加小写字母")
    if not has_upper:
        print("• 添加大写字母")
    if not has_digit:
        print("• 添加数字")
    if not has_special:
        print("• 添加特殊字符")
    if has_repeat:
        print("• 减少重复字符")
    if has_sequence:
        print("• 避免连续字符序列")

# 主程序循环
while True:
    display_menu()
    choice = input("\n请输入选项（0-6）：").strip()
    
    if choice == '1':
        basic_calculator()
    elif choice == '2':
        base_converter()
    elif choice == '3':
        data_analyzer()
    elif choice == '4':
        logic_calculator()
    elif choice == '5':
        bit_operations()
    elif choice == '6':
        comprehensive_example()
    elif choice == '0':
        print("\n感谢使用智能计算器系统！")
        break
    else:
        print("\n无效选项，请重新输入！")
    
    input("\n按回车键继续...")  # 暂停，等待用户查看结果