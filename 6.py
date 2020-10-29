# import os
#  ph = "D:/xxw/untitled1/1.py"
#
#
#
#  if os.path.exists(ph):
#      os.remove(ph)
#
# else:
#     print("没有这个文件")

# import os
# path = 'd:/xxw/untitled1/1.py'  # 文件路径
# if os.path.exists(path):  # 如果文件存在
#     # 删除文件，可使用以下两种方法。
#     os.remove(path)
#     # os.unlink(path)
# else:
#     print('no such file:%s' % path)  # 则返回文件不存在

# import os
# pt_path = "d:/xxw/untitled1/.1.py"
#
# if  os.path.exists(pt_path):
#     os.remove(pt_path)
#
# else:
#     print ("no  such  file  ")

# import os
#
# pt_path = './123.py'
#
# if not os.path.exists(pt_path):
#     file = open(pt_path,'w')
#     file.write('nihao')
#     file.close()
# else:
#     os.remove(pt_path)
#
#
# def  text_create(name,msg):
#     pt_path  = "./"
#     fullpath = pt_path + name +".py"
#
#     file = open(fullpath,'w')
#
#     file.write(msg)
#
# text_create("7",'nihao me' )

