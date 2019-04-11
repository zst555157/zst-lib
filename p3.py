import re
'''s=r'([a-z]+) ([a-z]+)'
pattern=re.compile(s,re.I)  #s.I表示忽略大小写
m=pattern.match("Hellow world wide web")
s=m.group(0)  #group(0)表示返回匹配成功的整个字符串
print(s)

a=m.span(0) #返回匹配成功的整个字符串的跨度
print(a)
s=m.group(1) #返回第一个匹配成功的字符串
print(s)
a=m.span(1)  #返回匹配成功的第一个字符串的跨度
print(a)
s=m.groups()  #返回匹配成功的整个字符串
print(s)'''
'''
正则方法：
match : 从开始位置开始查找，一次匹配
search: 从任何位置查找，一次匹配
findall: 全部匹配，返回列表
split: 分割字符串，返回列表
sub: 替换'''

s=r'\d+'
pattern=re.compile(s)
m=pattern.search("one12two34three56")
print(m.group())
m=pattern.search("one12two34three56",10,40)
print(m.group())
m=pattern.findall("i am 18 years old and 185 hight")
print(m)
m=pattern.finditer("i am 18 years old and 185 hight")
print(m,type(m))

'''
匹配中文
中文Unicode范围主要在【u4e00-u9fa5]'''

hello=u'你好，世界'
pattern=re.compile(r'[\u4e00-\u9fa5]+')
m=pattern.findall(hello)
print(m)
'''
贪婪与非贪婪模式
贪婪：越多越好
非贪婪：越少越好、
python默认贪婪模式
eg 'abbbbbbcd
贪婪：abbbbbb
非贪婪：a'''

