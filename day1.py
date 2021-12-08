Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('Hello world')
Hello world
>>> # 1-100
>>> list(range(1,101))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> # Dynamic Typing
>>> a = 10
>>> a
10
>>> # if we want to check type of data then use type()
>>> s
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> a
10
>>> type(a)
<class 'int'>
>>> b = 12.33
>>> b
12.33
>>> type(b)
<class 'float'>
>>> s = 'python'
>>> s
'python'
>>> type(s)
<class 'str'>
>>> a
10
>>> b
12.33
>>> s
'python'
>>> # if we want to check the address of any object
>>> # then use id()
>>> id(a)
8791437071680
>>> id(b)
5356592
>>> id(s)
48943032
>>> #print()
>>> 
= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/sample5.py =
Hello
Good morning
1223432
>>> a = 10
>>> type(a)
<class 'int'>
>>> a = 12.50
>>> a
12.5
>>> type(a)
<class 'float'>
>>> a = 'python'
>>> type(a)
<class 'str'>
>>> 
