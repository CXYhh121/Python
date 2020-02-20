# coding=utf-8
print('hello world')

# 变量的定义与使用
# 格式化输出变量的值
name = 'TOM'
print('我的名字是%s' % name)

age = 20
print('我的年龄是%d岁' % age)

weight = 47.8
print('我的体重是%f斤' % weight)

# if else 语句的使用
x = 10
if x > 0:
    print('我就是很喜欢你')
else:
    print ('我其实就是不喜欢你')


# 判断语句的运用实例
#
"""
需求
   1、输入用户的年龄，判断是否大于18岁
   2、如果满18岁，就可以进入网吧
   3。如果未满18岁就回家写作业
"""

age = int(input("今年多大了？"))

if age >= 18:
    print("可以进网吧happy......")
else:
    print('你还没长大，赶紧回家写作业')


