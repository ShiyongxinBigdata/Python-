"""
第3章练习题6：成员运算符应用

题目：文本分析工具
- 用户输入一段文本和要查找的关键词
- 使用in和not in检查关键词是否存在
- 演示is和is not的身份比较
- 分析文本中的字符和单词

输出格式：
请输入一段文本：Python是一门优秀的编程语言
请输入要查找的关键词：Python
关键词存在于文本中：True
关键词不存在于文本中：False
文本包含"编程"：True
文本包含"Java"：False

考查知识点：in、not in、is、is not运算符、字符串成员检查
"""

# 文本分析工具
print("=== 文本分析工具 ===")

# 获取用户输入
text = input("请输入一段文本：")
keyword = input("请输入要查找的关键词：")

# 成员运算符演示
print("\n=== 成员关系检查 ===")

# 检查关键词是否在文本中
keyword_exists = keyword in text
print("关键词'%s'存在于文本中：%s" % (keyword, keyword_exists))

# 使用not in检查
keyword_not_exists = keyword not in text
print("关键词'%s'不存在于文本中：%s" % (keyword, keyword_not_exists))

# 检查其他关键词
common_words = ["编程", "语言", "Python", "Java", "学习", "代码"]
print("\n--- 常见词汇检查 ---")
for word in common_words:
    if word in text:
        print("文本包含'%s'：True" % word)
    else:
        print("文本包含'%s'：False" % word)

# 字符级别的检查
print("\n=== 字符检查 ===")
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

has_vowels = any(char in vowels for char in text)
has_consonants = any(char in consonants for char in text)

print("文本包含元音字母：%s" % has_vowels)
print("文本包含辅音字母：%s" % has_consonants)

# 特殊字符检查
special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
has_special = any(char in special_chars for char in text)
print("文本包含特殊字符：%s" % has_special)

# 身份运算符演示
print("\n=== 身份运算符演示 ===")

# 字符串的身份比较
str1 = "Python"
str2 = "Python"
str3 = keyword

print("str1 = '%s'" % str1)
print("str2 = '%s'" % str2)
print("str3 = '%s'" % str3)

print("str1 is str2：%s" % (str1 is str2))  # 小字符串可能被缓存
print("str1 == str2：%s" % (str1 == str2))  # 内容相同
print("str1 is str3：%s" % (str1 is str3))  # 取决于输入内容
print("str1 == str3：%s" % (str1 == str3))  # 内容比较

# 列表的身份比较
print("\n--- 列表身份比较 ---")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 is list2：%s" % (list1 is list2))  # False，不同对象
print("list1 == list2：%s" % (list1 == list2))  # True，内容相同
print("list1 is list3：%s" % (list1 is list3))  # True，同一对象
print("list1 == list3：%s" % (list1 == list3))  # True，内容相同

# is not 演示
print("\n--- is not 演示 ---")
print("str1 is not str3：%s" % (str1 is not str3))
print("list1 is not list2：%s" % (list1 is not list2))

# 实际应用：文本统计
print("\n=== 文本统计 ===")
char_count = len(text)
word_count = len(text.split())
digit_count = sum(1 for char in text if char in "0123456789")
space_count = text.count(" ")

print("字符总数：%d" % char_count)
print("单词总数：%d" % word_count)
print("数字字符数：%d" % digit_count)
print("空格数：%d" % space_count)

# 查找所有包含特定字符的位置
if keyword in text:
    start_pos = text.find(keyword)
    print("关键词'%s'首次出现位置：%d" % (keyword, start_pos)) 