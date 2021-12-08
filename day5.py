Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ~1
-2
>>> ~2
-3
>>> #bitwise not
>>> # decimal => binary ==> decimal
>>> ~5
-6
>>> ~7
-8
>>> ~10
-11
>>> ~4
-5
>>> 10 == 10
True
>>> 10==10.0
True
>>> 10 is 10
True
>>> 10 is 10.0
False
>>> # Content equality and address equality
>>> 10 == 10.0 #content equality
True
>>> id(10)
8791207105856
>>> id(10.0)
5485600
>>> 10 == 10.0
True
>>> 10 is 10.0
False
>>> # when we use == it performes content equality
>>> # when we use is operator, it performs address equality
>>> #############################################################
>>> # DATA TYPES of the PYTHON
>>> # 14 types
>>> # String
>>> # Number/Numeric: int, float, complex
>>> # boolean
>>> # True False
>>> # Data Structures
>>> # List
>>> # Tuple
>>> # Set
>>> # Dict
>>> # range()
>>> # frozenset()
>>> #bytes()
>>> #bytearray()
>>> # None
>>> if :
	
SyntaxError: invalid syntax
>>> if None:
	print()

	
>>> ################ STRING ######################
>>> # Global data type
>>> # it accepts everything
>>> # if we want to specify string then we can make use of '' or ""
>>> s = 'pythhon'
>>> s
'pythhon'
>>> s = "Welcome"
>>> s
'Welcome'
>>> s = """ Hello Python"""
>>> s
' Hello Python'
>>> s = '"Hello"'
>>> s
'"Hello"'
>>> "Hello"
'Hello'
>>> 'Hello Good Morning'
'Hello Good Morning'
>>> 'Hello "Good Morning"'
'Hello "Good Morning"'
>>> "Hello "Good Morning""
SyntaxError: invalid syntax
>>> "Hello 'Good Morning'"
"Hello 'Good Morning'"
>>> "Hello 'Good morning'"
"Hello 'Good morning'"
>>> "Hello \"Good morning\"" #escape sequence
'Hello "Good morning"'
>>> # if inside its ' the outside its "
>>> # and vice versa
>>> 'Hello \'Good morning\'' #escape sequence
"Hello 'Good morning'"
>>> s = 'python is simple'
>>> s
'python is simple'
>>> # string is having a background data strucutre as an Array
>>> # when we say Array: it supports indexing
>>> # if we want to check the legnth of string
>>> # then use len() function
>>> s
'python is simple'
>>> len(s)
16
>>> # whenw we represent a string , space is also a one block
>>> len(s)-1
15
>>> # indexing starts from 0 and reaches upto (n-1) lenght-1
>>> s
'python is simple'
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[5]
'n'
>>> s[6]
' '
>>> s[15]
'e'
>>> s[16]
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    s[16]
IndexError: string index out of range
>>> # There actual 2 types of indexing
>>> # Positive indexing and negative indexing
>>> # _ve indexing means we can move from 0 to (n-1) and left to right
>>> # +ve indexing means we can move from 0 to (n-1) and left to right
>>> # -ve indexing means we can move from -1 to -n and right to left
>>> s[-16]
'p'
>>> s[-15]
'y'
>>> s
'python is simple'
>>> s[-10]
' '
>>> s[-1]
'e'
>>> # slicing in String
>>> s
'python is simple'
>>> # in indexing at a time we can retrieve only single character
>>> # so retrieving the perticular set of character is possible using slicing
>>> s
'python is simple'
>>> s[:]
'python is simple'
>>> s[:] #[start:stop]
'python is simple'
>>> s[0:6]
'python'
>>> # when we put stop in slicing then its exclusive ( add nahi hoga in output)
>>> s[6]
' '
>>> # i want simple
>>> s
'python is simple'
>>> s[10:]
'simple'
>>> s[10:14]
'simp'
>>> # when we want to reach upto end then there is no need to specify stop
>>> s
'python is simple'
>>> # is
>>> s[6:9]
' is'
>>> s[6:10]
' is '
>>> # s[start:stop]
>>> # s[start: stop : step]
>>> # when we want to skip  a character/block in uniform order then use step
>>> s
'python is simple'
>>> s[::1]
'python is simple'
>>> s[::2]
'pto ssml'
>>> s[::3]
'ph  me'
>>> s[0::3]
'ph  me'
>>> s
'python is simple'
>>> s[::3]
'ph  me'
>>> s
'python is simple'
>>> # in beteween we can also perform steping
>>> s[0:6]
'python'
>>> s[0:6:2]
'pto'
>>> s[:6:2]
'pto'
>>> s
'python is simple'
>>> s[15]
'e'
>>> s[16]
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    s[16]
IndexError: string index out of range
>>> s[0:]
'python is simple'
>>> s[:]
'python is simple'
>>> s[:25]
'python is simple'
>>> s[24:]
''
>>> # reversing of string using slicing
>>> s
'python is simple'
>>> s[::-1]
'elpmis si nohtyp'
>>> s[::]
'python is simple'
>>> s[::1]
'python is simple'
>>> s[::-1]
'elpmis si nohtyp'
>>> s[::-2]
'epi inhy'
>>> # i want to reverse 'simple' only
>>> s
'python is simple'
>>> # elpmis
>>> s[-1:-6]
''
>>> s[-1:-6:-1]
'elpmi'
>>> s[-1:-7:-1]
'elpmis'
>>> 
