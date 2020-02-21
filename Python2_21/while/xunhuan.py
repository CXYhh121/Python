# coding=utf-8

# while循环的使用
# 打印5编hello Python
# i = 0
# while i < 5:
#     # 要重复执行的代码
#     print ('hello Python')
#
#     # 处理计数器i
#     i = i + 1
# print ("循环结束后的i = %d" % i)
# 注意：循环结束后，之前定义的计数器条件的数值是依旧存在的


# 计算 0 ~ 100 之间所有数字的累计求和结果
# result = 0
# i = 0
#
# while i <= 100:
#     result += i
#     i += 1
# print ('0~100之间所有数字的累计结果是:%d' % result)

# 计算 0 ~ 100 之间 所有 偶数 的累计求和结果
# result = 0
# i = 0
#
# while i <= 100:
#     if i % 2 == 0:
#         # print (i)
#         result += i
#     i += 1
# print ('0 ~ 100 之间所有偶数的累计求和结果:%d' % result)


# 03. break 和 continue
#
# break 和 continue 是专门在循环中使用的关键字
# break 某一条件满足时，退出循环，不再执行后续重复的代码
# continue 某一条件满足时，不执行后续重复的代码
# break 和 continue 只针对 当前所在循环 有效

# i = 5
# while i <= 10:
#     if i == 3:
#         break;
#     else:
#         print (i)
#     i += 1
# print ('over')


# 打印九九乘法表
# from aetypes import end
#
# row = 1
#
# while row <= 5:
#     col = 1
#
#     while col <= row:
#         print ("*", end="")
#         col += 1
#     print ("")
#     row += 1

# 定义起始行
# from aetypes import end
#
# row = 1
#
# # 最大打印 9 行
# while row <= 9:
#     # 定义起始列
#     col = 1
#
#     # 最大打印 row 列
#     while col <= row:
#
#         # end = ""，表示输出结束后，不换行
#         # "\t" 可以在控制台输出一个制表符，协助在输出文本时对齐
#         print("%d * %d = %d" % (col, row, row * col), end='\t')
#
#         # 列数 + 1
#         col += 1
#
#     # 一行打印完成的换行
#     print("")
#
#     # 行数 + 1
#     row += 1

