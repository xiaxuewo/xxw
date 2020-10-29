# from urllib import request
#
# response = request.urlopen('https://www.baidu.com')
# print(response.read().decode())

from urllib import reuqest

response = request.urlopen('http://httpbin.org/post', data=b'word=hello')

print(response.read().decode())
