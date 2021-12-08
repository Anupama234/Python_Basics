Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Mutable and Immutable data types
>>> s = 'hello'
>>> s
'hello'
>>> type(s)
<class 'str'>
>>> s[0]
'h'
>>> s[0]='H'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s[0]='H'
TypeError: 'str' object does not support item assignment
>>> s.replace('h','H')
'Hello'
>>> # if we apply method on string it gives output
>>> s
'hello'
>>> id(s)
49671280
>>> s = s.replace('h','H')
>>> s
'Hello'
>>> id(s)
49052784
>>> ##############################
>>> # List
>>> f = []
>>> f
[]
>>> type(f)
<class 'list'>
>>> id(f)
50055944
>>> f
[]
>>> 120
120
>>> id(120)
8791220282112
>>> c = 120
>>> id(c)
8791220282112
>>> ''
''
>>> id('')
5405920
>>> _
5405920
>>> f
[]
>>> f.append(200)
>>> f
[200]
>>> id(f)
50055944
>>> f.append(['A','B'])
>>> f
[200, ['A', 'B']]
>>> id(f)
50055944
>>> ###############
>>> # string
>>> s
'Hello'
>>> s.lower()
'hello'
>>> s.title()
'Hello'
>>> s.count('l')
2
>>> #List
>>> f
[200, ['A', 'B']]
>>> f.append(500)
>>> f.append(1000)
>>> f
[200, ['A', 'B'], 500, 1000]
>>> id(f)
50055944
>>> f.clear()
>>> f
[]
>>> id(f)
50055944
>>> ####################### LIST ##########################
>>> # List is represented using []
>>> # List background data strucutre is Array
>>> # it supports indexing: +ve and -ve
>>> # it supports slicing
>>> # It support homogenous as wel as heterogeneous data
>>> # Its Mutable: so the changes we do, stored in the same object
>>> # After changes id remains same
>>> d = [10,20,30,40,50,60,70,80,90,100]
>>> d
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> type(d)
<class 'list'>
>>> d
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> len(d)
10
>>> d[0]
10
>>> d[9]
100
>>> #-ve
>>> d[-1]
100
>>> d[-10]
10
>>> d
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> d[:]
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> d[2:]
[30, 40, 50, 60, 70, 80, 90, 100]
>>> d[2:7]
[30, 40, 50, 60, 70]
>>> d
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> d[-1:-10]
[]
>>> d[-1:]
[100]
>>> d[:-1]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> d[::-1]
[100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
>>> d[-1:-10:-1]
[100, 90, 80, 70, 60, 50, 40, 30, 20]
>>> # Heterogeneous list
>>> d
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> g = [1,2,3,'A','D',23.45,3+4j,True]
>>> g
[1, 2, 3, 'A', 'D', 23.45, (3+4j), True]
>>> type(g)
<class 'list'>
>>> g[0]
1
>>> type(g[0])
<class 'int'>
>>> g[4]
'D'
>>> type(g[4])
<class 'str'>
>>> g[-1]
True
>>> type(g[-1])
<class 'bool'>
>>> ############################################
>>> g
[1, 2, 3, 'A', 'D', 23.45, (3+4j), True]
>>> g[-1]
True
>>> g[-1]= '450'
>>> g
[1, 2, 3, 'A', 'D', 23.45, (3+4j), '450']
>>> g[4]
'D'
>>> g[4]='DON'
>>> d
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> g
[1, 2, 3, 'A', 'DON', 23.45, (3+4j), '450']
>>> # If i want to replace mulptiple values at a time
>>> # ex: i want to replace (strating element)1,2,3 by 10,20,30
>>> g[:4]
[1, 2, 3, 'A']
>>> g[:3]
[1, 2, 3]
>>> id(g)
50055560
>>> g[:3]=10,20,30
>>> g
[10, 20, 30, 'A', 'DON', 23.45, (3+4j), '450']
>>> g[:3]
[10, 20, 30]
>>> g[:3]=[100,200,300]
>>> g
[100, 200, 300, 'A', 'DON', 23.45, (3+4j), '450']
>>> g[:4]
[100, 200, 300, 'A']
>>> g[:3]
[100, 200, 300]
>>> g[:3]=[1,2,3,4]
>>> g
[1, 2, 3, 4, 'A', 'DON', 23.45, (3+4j), '450']
>>> g[20:]
[]
>>> g[-1]
'450'
>>> len(g)
9
>>> g[8]
'450'
>>> g[:80]
[1, 2, 3, 4, 'A', 'DON', 23.45, (3+4j), '450']
>>> 
