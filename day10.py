Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ######### List Methods ##########
>>> a = []
>>> a
[]
>>> dir(a) # dir will retrieve all special functions and methods associated wth perticular object, n right now our object is list
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> a
[]
>>> help(a.append)
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.

>>> a
[]
>>> a.append(100)
>>> a
[100]
>>> id(a)
46938376
>>> a.append(1,2,3)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.append(1,2,3)
TypeError: append() takes exactly one argument (3 given)
>>> a.append([1,2,3])
>>> a
[100, [1, 2, 3]]
>>> a.append('123')
>>> a
[100, [1, 2, 3], '123']
>>> a.append(['1','2','3'])
>>> a
[100, [1, 2, 3], '123', ['1', '2', '3']]
>>> a[0]
100
>>> a[1]
[1, 2, 3]
>>> len(a)
4
>>> a[1]
[1, 2, 3]
>>> a[1:2]
[[1, 2, 3]]
>>> a[1]
[1, 2, 3]
>>> a[1][1]
2
>>> a[1,1]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a[1,1]
TypeError: list indices must be integers or slices, not tuple
>>> a
[100, [1, 2, 3], '123', ['1', '2', '3']]
>>> a[2]
'123'
>>> a[2][2]
'3'
>>> type(a[2])
<class 'str'>
>>> a[1]
[1, 2, 3]
>>> # i want to replace this 1,2,3 as 10,20,30
>>> a[1]=[10,20,30]
>>> a
[100, [10, 20, 30], '123', ['1', '2', '3']]
>>> a
[100, [10, 20, 30], '123', ['1', '2', '3']]
>>> a.clear()
>>> a
[]
>>> data = 'Yameen 35 35000'
>>> data
'Yameen 35 35000'
>>> type(data)
<class 'str'>
>>> b = ['Yameen', 35, 35000]
>>> b
['Yameen', 35, 35000]
>>> type(b)
<class 'list'>
>>> data
'Yameen 35 35000'
>>> data.split()
['Yameen', '35', '35000']
>>> ############################
>>> help(b.copy)
Help on built-in function copy:

copy() method of builtins.list instance
    Return a shallow copy of the list.

>>> # Shallow copy & Deep copy
>>> b
['Yameen', 35, 35000]
>>> id(b)
49686600
>>> z = b.copy()
>>> z
['Yameen', 35, 35000]
>>> id(z)
50020680
>>> # when we create a new object from old one, with different id/address ans same elements
>>> z
['Yameen', 35, 35000]
>>> b
['Yameen', 35, 35000]
>>> b[0]
'Yameen'
>>> b[0]='Amol'
>>> b
['Amol', 35, 35000]
>>> id(b)
49686600
>>> z
['Yameen', 35, 35000]
>>> id(z)
50020680
>>> # Deep copy
>>> # We create a new list in such way
>>> # where elements are same, but id's are also same
>>> #hence if we try to change any of the list then that change persist in both
>>> b
['Amol', 35, 35000]
>>> #here b is old list
>>> n = b
>>> n
['Amol', 35, 35000]
>>> id(b)
49686600
>>> id(n)
49686600
>>> n
['Amol', 35, 35000]
>>> b
['Amol', 35, 35000]
>>> b[0]
'Amol'
>>> b[0]='Vishal'
>>> b
['Vishal', 35, 35000]
>>> # here i have replaced Vishal in b
>>> n
['Vishal', 35, 35000]
>>> n
['Vishal', 35, 35000]
>>> n[2]
35000
>>> n[2]=50000
>>> n
['Vishal', 35, 50000]
>>> b
['Vishal', 35, 50000]
>>> b
['Vishal', 35, 50000]
>>> b[:2]
['Vishal', 35]
>>> q = b[:2]
>>> q
['Vishal', 35]
>>> id(b)
49686600
>>> id(q)
49685704
>>> b
['Vishal', 35, 50000]
>>> q
['Vishal', 35]
>>> q[1]
35
>>> q[1]=27
>>> q
['Vishal', 27]
>>> b
['Vishal', 35, 50000]
>>> ####################################
>>> dir(b)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(b.count)
Help on built-in function count:

count(value, /) method of builtins.list instance
    Return number of occurrences of value.

>>> # It support value repetition
>>> # Duplicates are allowed in list
>>> h = [1,2,1,1,1,1,3,4,6]
>>> h
[1, 2, 1, 1, 1, 1, 3, 4, 6]
>>> h.count(1)
5
>>> h.count(4)
1
>>> h.count(40)
0
>>> #################3
>>> b
['Vishal', 35, 50000]
>>> help(b.extend)
Help on built-in function extend:

extend(iterable, /) method of builtins.list instance
    Extend list by appending elements from the iterable.

>>> b.extend(['Pune',411110])
>>> b
['Vishal', 35, 50000, 'Pune', 411110]
>>> b.append(['Pune',411110])
>>> b
['Vishal', 35, 50000, 'Pune', 411110, ['Pune', 411110]]
>>> help(b.append)
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.

>>> #Object: int, float,complex,bool, string, list
>>> # iterable: (collection)string, list, tuple, set, dict
>>> # tell me the similarity and difference between append and extend?
>>> b
['Vishal', 35, 50000, 'Pune', 411110, ['Pune', 411110]]
>>> b.extend(100)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    b.extend(100)
TypeError: 'int' object is not iterable
>>> b.extend(12.50)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    b.extend(12.50)
TypeError: 'float' object is not iterable
>>> b.extend(3+4j)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    b.extend(3+4j)
TypeError: 'complex' object is not iterable
>>> b.extend(True)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    b.extend(True)
TypeError: 'bool' object is not iterable
>>> b
['Vishal', 35, 50000, 'Pune', 411110, ['Pune', 411110]]
>>> b.extend('ABHINANDAN')
>>> b
['Vishal', 35, 50000, 'Pune', 411110, ['Pune', 411110], 'A', 'B', 'H', 'I', 'N', 'A', 'N', 'D', 'A', 'N']
>>> b.extend(['ABHINANDAN'])
>>> b
['Vishal', 35, 50000, 'Pune', 411110, ['Pune', 411110], 'A', 'B', 'H', 'I', 'N', 'A', 'N', 'D', 'A', 'N', 'ABHINANDAN']
>>> 
