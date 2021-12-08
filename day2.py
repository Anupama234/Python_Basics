Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Identifiers in Python
>>> 'python'
'python'
>>> s = 'python'
>>> #variable
>>> 25
25
>>> a = 25
>>> a
25
>>> #Rules to specify identifier
>>> # we can use alphabates, A-Z,a-z,_
>>> _ = 120
>>> _
120
>>> a =10
>>> b= 20
>>> a b =100
SyntaxError: invalid syntax
>>> a_b = 100
>>> a_b
100
>>> # space is not allowed when we are using 2 diffrnt letter or word in order to represent an identifier
>>> bank ifsc=13212343
SyntaxError: invalid syntax
>>> bank_ifsc=13212343
>>> bank_ifsc
13212343
>>> # dont use numbers or special charachters
>>> @2 = 'hello'
SyntaxError: invalid syntax
>>> 3a = 23
SyntaxError: invalid syntax
>>> a4 = 'Yameen'
>>> # we can use number after char/word but not before
>>> 4a = 34
SyntaxError: invalid syntax
>>> a4 = 34
>>> a4
34
>>> 3 = 300
SyntaxError: can't assign to literal
>>> a4 = 50
>>> a4
50
>>> a4=50
>>> a4
50
>>> # PEP 8 standards
>>> a@ = 45
SyntaxError: invalid syntax
>>> @a = 45
SyntaxError: invalid syntax
>>> a4 = 50
>>> a_4 = 50
>>> # Python is case senstive language
>>> a = 10
>>> A = 20
>>> a
10
>>> A
20
>>> s = 'python'
>>> S
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    S
NameError: name 'S' is not defined
>>> _ =400
>>> __ = 4567
>>> _
400
>>> __
4567
>>> a4 = 50
>>> a4=50
>>> # Literals
>>> # Literals are those which are used to store a perticular object
>>> # Types depends on type of data you are trying to save
>>> s = 'python'
>>> s
'python'
>>> # s is of type string== its a string literal
>>> a = 100
>>> type(a)
<class 'int'>
>>> # abecomes a int literal
>>> # complex number: real+img
>>> c =  3+4j
>>> c
(3+4j)
>>> type(c)
<class 'complex'>
>>> x = True
>>> x
True
>>> type(x)
<class 'bool'>
>>> # Keywords
>>> import keywords
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    import keywords
ModuleNotFoundError: No module named 'keywords'
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> len(keyword.kwlist)
35
>>> # These keywrods are reserved
>>> # you can not use these as an identifier
>>> in = 23
SyntaxError: invalid syntax
>>> try = 'Hello'
SyntaxError: invalid syntax
>>> _in = 12
>>> IN = 23
>>> In = 34
>>> iN = 3
>>> None
>>> False
False
>>> False + False
0
>>> True + True
2
>>> # Its amazing calculator
>>> # Operators in Python
>>> # Arithmetic operators
>>> # + - * / % ** //
>>> 2 + 3
5
>>> 3 - 1
2
>>> 5 * 4
20
>>> 4/5
0.8
>>> 4/2
2.0
>>> #floor division
>>> 4//2
2
>>> # floor----ceil
>>> 3/5
0.6
>>> 3//5
0
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> 2**3
8
>>> 3**2
9
>>> # Assignment operators
>>> # += -= *= /= %= **= //=
>>> # %
>>> 4 % 2
0
>>> 5 % 4
1
>>> a = 10
>>> a
10
>>> a + 5
15
>>> a
10
>>> a = a + 5
>>> a
15
>>> # u have changed a here
>>> a
15
>>> a - 10
5
>>> a
15
>>> a-=10 # a = a - 10
>>> a
5
>>> b = 500
>>> b/10
50.0
>>> b
500
>>> b/=10
>>> b
50.0
>>> 100 + 200
300
>>> 100+=200
SyntaxError: can't assign to literal
>>> # when u r using an assignment operator , it will only work on the oject with name( identifier)
>>> 100+=200 # 100 = 100 + 200
SyntaxError: can't assign to literal
>>> # Logical Operators
>>> # 1. and 2. or 3. not
>>> 1 * 1
1
>>> 1 * 0
0
>>> 0 * 1
0
>>> 0 * 0
0
>>> # AND means multiplication
>>> # True means 1
>>> # False means 0
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> 1 and 0
0
>>> 1 and 1
1
>>> 0 and 1
0
>>> 0 and 0
0
>>> # or operator
>>> # addition
>>> 1 + 1
2
>>> 1 + 0
1
>>> 0 + 1
1
>>> 0 + 0
0
>>> # 0 None ''
>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
>>> 1 or 1
1
>>> 1 or 0
1
>>> 0 or 1
1
>>> 0 or 0
0
>>> 10 and 20
20
>>> 0 and 20
0
>>> # When we have both True or Positive values
>>> # when we have x and y
>>> # when X is positive/True , ti will return y
>>> # when X is negative /False then it will return y
>>> 10 and 0
0
>>> # when X is negative/ False then it will return x
>>> 
