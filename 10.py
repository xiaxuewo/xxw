# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')#传入解析器：lxml
# print(soup.prettify())#格式化代码，自动补全
# print(soup.title.string)#得到title标签里的内容

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')#传入解析器：lxml
# print(soup.title)#选择了title标签
# print(type(soup.title))#查看类型
# print(soup.head)

# from  bs4 import BeautifulSoup
# soup = BeautifulSoup(html,'lxml')
#
#
# print(soup.head.title)
# print(soup.p.contents)

# from  bs4 import BeautifulSoup
#
# sp = BeautifulSoup(html,'lxml')
#
# print(sp.find_all("p"))


# name = input('请输入你想对话的名字:')
# s = input('请输入你想说的话')
# print("{},我必须告诉你：{}".format(name,s*3))
# furen  =  input("请输入你太太的名字：")
# anhao =  input("请输入你想对他说的话：")
#
# print("{},我想告诉你：{}".format(furen,anhao*3))
#
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}*{}={:2} ".format(j,i,i*j),end='')
#     print('')


# for i in range(1,10):
#     for m in range(1,i+1):
#         print("{:5}*{:5}={}".format(m,i,i*m),end =" ")
#     print("")

import turtle

# import random
# str1=input("请输入你的名字:")
# print("Hello!{}".format(str1))
# guard = ord(str1[0]) % 100
# print("你的辛运数字是",random.choice(range(guard)))

name = "eric"
age = 74

# print(f"hello.,{name},you aer {age}")
#
# print(F"yes")

# print(F"{name.lower()} is funny")
