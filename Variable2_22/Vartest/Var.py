# coding:utf-8
# 高级变量的使用
# Python 中数据类型可以分为 数字型 和 非数字型
# 01.列表list，列表是有序的对象的集合

# # 定义一个列表
# name_list = ["zhangsan", "lisi"]  # type: List[str]
# # 在列表的任意位置插入一个数据
# name_list.insert(0, "wangwu")
# # 通过索引修改列表中的元素
# name_list[0] = "chenxiyue"
# # 在列表末尾追加一个数据
# name_list.append("zhangweixin")
# print (name_list[0])
# # 删除列表中指定索引的数据
# del name_list[0]
# # 删除第一个出现的指定的数据
# name_list.remove("lisi")
# print (len(name_list))
#
# # 遍历列表中的数据并打印
# for n in name_list:
#     print (n)
# print ("")
# # 反转列表中的数据
# name_list.reverse()
#
# # 列表的循环遍历
# for name in name_list:
#     print (name)


# 02.元组Tuple，元组是无序对象的集合
# 元组与列表相类似，但是不同的是在于元组的元素不能修改

# 创建元组
# info_tuple = ()

# 当元组中只包含一个元素时，需要在元素后面添加逗号
# info_tuple = (50, 60, 'zhangsan')

# 元组的常用操作
# 统计元组中某个元素出现的次数
# print (info_tuple.count(50))
#
# # 获取元组中对应元素的下标
# print (info_tuple.index(50))
# for i in info_tuple:
#     print (i)
#
# info = ("zhangsan", 18)
# print ("%s 的年龄是 %d" % info)
#
# # 元组与列表之间的转换
# name_list = ["zhangsan", "lisi", "wangwu"]
#
# tuple(name_list)
# name_list.reverse()
# # list(name_list)
# name_list.reverse()
# for t in name_list:
#     print (t)


# 03.字典dictionary ，字典使用键值对存储数据 即key:value
# key为索引，value为数据，key必须是唯一的，value可以不唯一
# value可取任何数据类型，key只能使用数字，字符串、元组等数据类型

# 定义一个地点
# xiaoming = {"name": "小名", "age": 30, "xingbie": "男", "gender": True, "height": 1.75}

# 获取字典中对应索引的数据
# print (xiaoming.get("name"))

# 拷贝字典中的所有数据
# print (xiaoming.copy())

# # 返回字典中对应的key值
# for k in xiaoming.keys():
#     print (k)
#
# # 返回字典中对应的value值
# for v in xiaoming.values():
#     print (v)
# # 返回字典中对应的键值对
# for i in xiaoming.items():
#     print (i)

# 判断查询的key值是否在字典中
# print (xiaoming.has_key("name"))
#
# # 判断key值或是value值是否在字典中
# print ("name" in xiaoming.keys())
# print ("小名" in xiaoming.values())
# print ("lkd" in xiaoming.keys())
#
# # 设置字典中的数据
# xiaoming.setdefault("mz", "zhangsan")
#
# xiaoming["name"] = "zhangweixin"
#
# for value in xiaoming.values():
#     print (value)
