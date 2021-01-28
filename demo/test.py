# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 0:02
# @Project : InterfaceProject
import re
c = {'a':'b',
     'c':{'d':'f'},
     'e':{'g':{'g':'1'}}}
b = str(c)
d = eval(b)
print(d)

# print(a.items())
# print(a.keys())
# print(a.values())

a = {"client":{"bundleId":"com.qlchat.hexiaoyu",
     "caller":"app","ex":{"model":"VOG-AL00"},
     "os":"25","platform":"android","ver":"1.3.1"},
     "data":{},"id":"1610968043916936","sign":
          "6ac9bb271ebd14ef13ad77adf6f79efc","timestamp":1610968043916,"user":
          {"sid":"<sid>","userId":2000002398561712}}
# re.sub()
a = str(a)
# a = 'bbb<sid>ccc'
# print(type(a))
# repl =   'aaa'
repl ='41539b39836e43ec920e2cf8dd323973'
# a.replace('"[sid]"',sid)
pattern = '<sid>'
a = re.sub(pattern, repl, a,count=1, flags=re.IGNORECASE)
# re.sub(,sid,a)
# print(a)
