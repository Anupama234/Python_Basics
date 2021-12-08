Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = '12341111144567567111111198098000000011110000'
>>> # replace 1 by 0 and 0 by 1
>>> s
'12341111144567567111111198098000000011110000'
>>> s.replace(1,*)
SyntaxError: invalid syntax
>>> s.replace('1','*')
'*234*****44567567*******980980000000****0000'
>>> s
'12341111144567567111111198098000000011110000'
>>> s1 = s.replace('1','*')
>>> s1
'*234*****44567567*******980980000000****0000'
>>> s2 = s1.replace('0','1')
>>> s2
'*234*****44567567*******981981111111****1111'
>>> s3 = s2.replace('*','1')
>>> s3
'12341111144567567111111198198111111111111111'
>>> s
'12341111144567567111111198098000000011110000'
>>> s2
'*234*****44567567*******981981111111****1111'
>>> s4 = s2.replace('*','0')
>>> s4
'02340000044567567000000098198111111100001111'
>>> s
'12341111144567567111111198098000000011110000'
>>> s
'12341111144567567111111198098000000011110000'
>>> s=='1'
False
>>> s=='0'
False
>>> s
'12341111144567567111111198098000000011110000'
>>> s.replace('1','0').replace('0','1')
'12341111144567567111111198198111111111111111'
>>> s.replace('1','0')
'02340000044567567000000098098000000000000000'
>>> s.replace('0','t').replace('1','0').replace('t','1')
'02340000044567567000000098198111111100001111'
>>> s4
'02340000044567567000000098198111111100001111'
>>> ####################################################
>>> # Numeric data type: int float complex
>>> # [0-9]
>>> # int= decimal values== base10
>>> a = 10
>>> type(a)
<class 'int'>
>>> b = 12.45
>>> b
12.45
>>> type(b)
<class 'float'>
>>> #Complex
>>> # (real+imag)
>>> c = 2+4j
>>> c
(2+4j)
>>> type(c)
<class 'complex'>
>>> d = 3+1J
>>> d
(3+1j)
>>> type(d)
<class 'complex'>
>>> f = 4+2k
SyntaxError: invalid syntax
>>> 2+5a
SyntaxError: invalid syntax
>>> 2+3j
(2+3j)
>>> ############## Mutable and Immutable #############
>>> s = 'python'
>>> s
'python'
>>> id(s)
48938376
>>> s.upper()
'PYTHON'
>>> s
'python'
>>> s = s.upper()
>>> s
'PYTHON'
>>> id(s)
51899672
>>> s[0]
'P'
>>> s[0]='J'
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    s[0]='J'
TypeError: 'str' object does not support item assignment
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> a
10
>>> dir(a)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> a
10
>>> # numeric values does not support array,indexing slicing
>>> a[0]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a[0]
TypeError: 'int' object is not subscriptable
>>> type(a)
<class 'int'>
>>> b
12.45
>>> b[0]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    b[0]
TypeError: 'float' object is not subscriptable
>>> # int float & complex are immutable data types
>>> a
10
>>> id(a)
8791391851840
>>> a+=20
>>> a
30
>>> id(a)
8791391852480
>>> # Boolean: True False
>>> x = True #keyword
>>> x
True
>>> type(x)
<class 'bool'>
>>> x
True
>>> x[0]
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    x[0]
TypeError: 'bool' object is not subscriptable
>>> x[:]
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    x[:]
TypeError: 'bool' object is not subscriptable
>>> x
True
>>> id(x)
8791391320400
>>> ' '
' '
>>> id(' ')
41560136
>>> ##################################
>>> # Data structure
>>> # List
>>> # Creation
>>> ls = []
>>> ls
[]
>>> type(ls)
<class 'list'>
>>> id(ls)
52006984
>>> ls2 = [10,20,30,40]
>>> ls2
[10, 20, 30, 40]
>>> type(ls2)
<class 'list'>
>>> id(ls2)
46939976
>>> ls
[]
>>> id(ls)
52006984
>>> ls = 10
>>> ls
10
>>> type(ls)
<class 'int'>
>>> ls = []
>>> type(ls)
<class 'list'>
>>> ls.append([1,2,3])
>>> ls
[[1, 2, 3]]
>>> id(ls)
52245768
>>> ls
[[1, 2, 3]]
>>> ls.append(10,20,30)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    ls.append(10,20,30)
TypeError: append() takes exactly one argument (3 given)
>>> ls.append([10,20,30])
>>> ls
[[1, 2, 3], [10, 20, 30]]
>>> id(ls)
52245768
>>> k = [1,2,3,4]
>>> k
[1, 2, 3, 4]
>>> id(k)
46939592
>>> k.remove(2)
>>> k
[1, 3, 4]
>>> id(k)
46939592
>>> k
[1, 3, 4]
>>> k.append(200)
>>> k
[1, 3, 4, 200]
>>> id(k)
46939592
>>> dir(k)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> [1,2,3]+[10,20,30]
[1, 2, 3, 10, 20, 30]
>>> 
