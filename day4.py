Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #scripting means --- one line code/codes
>>> print('Hello')
Hello
>>> print('Hello')
Hello
>>> print('Hello') print('Good evening all')
SyntaxError: invalid syntax
>>> print('Hello');print('Good evening all')
Hello
Good evening all
>>> for i in range(4):#0-3
	print(i)

	
0
1
2
3
>>> for i in range(4):#0-3
	print(i)
print('Out of my house')
SyntaxError: invalid syntax
>>> for i in range(4):#0-3
	print(i)
	print('Out of my house')

	
0
Out of my house
1
Out of my house
2
Out of my house
3
Out of my house
>>> 
= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/sample2.py =
0
1
2
3
Out of my house...
>>> print('This is my sample program')
This is my sample program
>>> 
= RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/sample4.py =
This is my another way to execute puthon code
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> #OPERATORS
>>> #Bitwise operators
>>> # & | ^ ~ >> <<
>>> # it only works on 0 , 1
>>> 0
0
>>> 1 & 2
0
>>> # multplication= &
>>> 4 & 7
4
>>> # Decimal==> Binary==> mulitplication==> Decimal
>>> 1 and 1
1
>>> 1 & 1
1
>>> 10 and 7
7
>>> 10 & 7
2
>>> # | or of Bitwise
>>> 4 | 7
7
>>> # xor =  ^
>>> 4 ^ 7
3
>>> # not
>>> # 	~ tild sign
>>> ~1
-2
>>> ~2
-3
>>> ~4
-5
>>> # >> <<
>>> 4
4
>>> 4>>2
1
>>> 7>>3
0
>>> 3<<2
12
>>> # Membership operator
>>> member1 = [1,2,3,4,5]
>>> member2 = [10]
>>> member1
[1, 2, 3, 4, 5]
>>> member2
[10]
>>> member is member2
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    member is member2
NameError: name 'member' is not defined
>>> member1 is member2
False
>>> member2 is member1
False
>>> [2] is member1
False
>>> member1
[1, 2, 3, 4, 5]
>>> ###################################################
>>> #Membership  operator
>>> # in -------  not in
>>> 'kar' in 'Tendulkar'
True
>>> 'Kar' in 'Tendulkar'
False
>>> [2] in [1,2,3,4,5]
False
>>> 2 in [1,2,3,4,5]
True
>>> 'amit' not in 'Amitabh'
True
>>> # identity opearators
>>> 'amit'=='amit'
True
>>> #is---- is not
>>> 'amit' is 'amit
SyntaxError: EOL while scanning string literal
>>> 'amit' is 'amit'
True
>>> 'amit' is 'Amit'
False
>>> 'amit' is not 'Amit'
True
>>> ######################################
>>> 10 == 10
True
>>> 10 == 10.0
True
>>> 10 is 10
True
>>> 10 is 10.0
False
>>> # Content equality and address equality
>>> 
