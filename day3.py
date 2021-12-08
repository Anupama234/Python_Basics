Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 100
100
>>> type(100)
<class 'int'>
>>> a = 100
>>> a
100
>>> type(a)
<class 'int'>
>>> a4 = 200
>>> 4a = 200
SyntaxError: invalid syntax
>>> a=20
>>> a = 20
>>> # PEP 8 standards
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> a
20
>>> a + 10
30
>>> a
20
>>> a
20
>>> a+=10 # a = a+10
>>> a
30
>>> a
30
>>> a - 5
25
>>> a
30
>>> a-=5
>>> a
25
>>> #Logical Operators
>>> # True False===> booleans
>>> #  1 and 0
>>> # and or not
>>> #and means multiplication
>>> 1 * 1
1
>>> 1 * 0
0
>>> 0 * 1
0
>>> 0 * 0
0
>>> 1 and 1
1
>>> 1 and  0
0
>>> 0 and 1
0
>>> 0 and 0
0
>>> True and True
True
>>> #conditional operators
>>> name = 'Yameen'
>>> age = 35
>>> name=='Yameen'
True
>>> age==50
False
>>> name=='Yameen' and age==50
False
>>> name=='Yameen' and age==35
True
>>> name=='Yameen' or age==50
True
>>> name=='Yameen
SyntaxError: EOL while scanning string literal
>>> name=='Yameen'
True
>>> age==50
False
>>> True or False
True
>>> #####################
>>> #and
>>> 1 and 1
1
>>> 1 and 0
0
>>> 0 and 1
0
>>> 0 and 0
0
>>> #or
>>> 1 or 1
1
>>> 1 or 0
1
>>> 0 or 1
1
>>> 0 or 0
0
>>> #not
>>> True
True
>>> not True
False
>>> not False
True
>>> not 1
False
>>> not 0
True
>>> name
'Yameen'
>>> not name=='Yameen'
False
>>> name
'Yameen'
>>> age
35
>>> not age==40
True
>>> #conditional operators
>>> # < > <= >= == !=
>>> 2>3
False
>>> 4==4
True
>>> #conditional operators always result boolean output means True and False
>>> 'a'=='A'
False
>>> 'a'!='A'
True
>>> for i in range(20):
    print(i)
print('Process completed.!!!!!!')
SyntaxError: invalid syntax
>>> 
