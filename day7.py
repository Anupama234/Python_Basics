Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ~1
-2
>>> ~2
-3
>>> ~3
-4
>>> ~4
-5
>>> 
>>> s = 'simple string'
>>> s
'simple string'
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(s)
No Python documentation found for 'simple string'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found, 
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers such as "def" and
 |      "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |        sep
 |          The delimiter according which to split the string.
 |          None (the default value) means split according to any whitespace,
 |          and discard empty strings from the result.
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      
 |      Splits are done starting at the end of the string and working to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |      sep
 |        The delimiter according which to split the string.
 |        None (the default value) means split according to any whitespace,
 |        and discard empty strings from the result.
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace remove.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

>>> s
'simple string'
>>> s.index('p')
3
>>> s.index('e')
5
>>> s[5]
'e'
>>> s.index('s')
0
>>> help(s.index)
Help on built-in function index:

index(...) method of builtins.str instance
    S.index(sub[, start[, end]]) -> int
    
    Return the lowest index in S where substring sub is found, 
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Raises ValueError when the substring is not found.

>>> s.indxe('s',6)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.indxe('s',6)
AttributeError: 'str' object has no attribute 'indxe'
>>> s.index('s',6)
7
>>> s
'simple string'
>>> s[7]
's'
>>> s.index('S',6)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s.index('S',6)
ValueError: substring not found
>>> s
'simple string'
>>> ## JOIN ###
>>> help(s.join)
Help on built-in function join:

join(iterable, /) method of builtins.str instance
    Concatenate any number of strings.
    
    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.
    
    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

>>> '-'.join(['Ajay','Pradnya])
	      
SyntaxError: EOL while scanning string literal
>>> '-'.join(['Ajay','Pradnya','Juber'])
	      
'Ajay-Pradnya-Juber'
>>> '=='.join(['Ajay','Pradnya','Juber'])
	      
'Ajay==Pradnya==Juber'
>>> ' '.join(['Ajay','Pradnya','Juber'])
	      
'Ajay Pradnya Juber'
>>> ls = ['this', 'is', 'sample','list']
	      
>>> ls
	      
['this', 'is', 'sample', 'list']
>>> type(ls)
	      
<class 'list'>
>>> ' '.join(ls)
	      
'this is sample list'
>>> s
	      
'simple string'
>>> # is.......
	      
>>> s = 'abc 2375243'
	      
>>> s.isalpha()
	      
False
>>> a = 'abc'
	      
>>> a
	      
'abc'
>>> a.isalpha()
	      
True
>>> s
	      
'abc 2375243'
>>> a.isalnum()
	      
True
>>> s.isalnum()
	      
False
>>> s
	      
'abc 2375243'
>>> help(s.isascii)
	      
Help on built-in function isascii:

isascii() method of builtins.str instance
    Return True if all characters in the string are ASCII, False otherwise.
    
    ASCII characters have code points in the range U+0000-U+007F.
    Empty string is ASCII too.

>>> v = 'U0000'
	      
>>> v
	      
'U0000'
>>> v.isascii()
	      
True
>>> v = ' '
	      
>>> v.isascii()
	      
True
>>> a
	      
'abc'
>>> a.isascii()
	      
True
>>> s
	      
'abc 2375243'
>>> s.islower()
	      
True
>>> s.isupper()
	      
False
>>> s
	      
'abc 2375243'
>>> s.isdecimal()
	      
False
>>> z = '12323'
	      
>>> z
	      
'12323'
>>> z.isdecimal()
	      
True
>>> # upper() isupper()
	      
>>> s = 'python'
	      
>>> s.upper()
	      
'PYTHON'
>>> s.isuuper()
	      
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s.isuuper()
AttributeError: 'str' object has no attribute 'isuuper'
>>> s.isupper()
	      
False
>>> d = '123'
	      
>>> d.isdigit()
	      
True
>>> d.isdecimal()
	      
True
>>> help(d.isdigit)
	      
Help on built-in function isdigit:

isdigit() method of builtins.str instance
    Return True if the string is a digit string, False otherwise.
    
    A string is a digit string if all characters in the string are digits and there
    is at least one character in the string.

>>> help(d.isdecimal)
	      
Help on built-in function isdecimal:

isdecimal() method of builtins.str instance
    Return True if the string is a decimal string, False otherwise.
    
    A string is a decimal string if all characters in the string are decimal and
    there is at least one character in the string.

>>> s = 'ProgRAMiZ'
	      
>>> s
	      
'ProgRAMiZ'
>>> s.upper()
	      
'PROGRAMIZ'
>>> s.lower()
	      
'programiz'
>>> s.casefold()
	      
'programiz'
>>> s.title()
	      
'Programiz'
>>> s.capitalize()
	      
'Programiz'
>>> ######################################################
	      
>>> s = 'python'
	      
>>> s = 'mango'
	      
>>> #mongo
	      
>>> s.replace('a','o')
	      
'mongo'
>>> s
	      
'mango'
>>> s[1]
	      
'a'
>>> s[1]='o'
	      
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    s[1]='o'
TypeError: 'str' object does not support item assignment
>>> s
	      
'mango'
>>> id(s)
	      
52654632
>>> s1 = s.replace('a','o')
	      
>>> s1
	      
'mongo'
>>> id(s1)
	      
52827728
>>> # string is ummutable
	      
>>> #string is immutable
	      
>>> s
	      
'mango'
>>> id(s)
	      
52654632
>>> del s
	      
>>> s
	      
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> a
	      
'abc'
>>> del a
	      
>>> a
	      
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> v
	      
' '
>>> del v
	      
>>> 
=============================== RESTART: Shell ===============================
>>> a = 20
	      
>>> b = 3-
	      
SyntaxError: invalid syntax
>>> b = 30
	      
>>> c = 'python'
	      
>>> a
	      
20
>>> b
	      
30
>>> c
	      
'python'\
>>> dir()
	      
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'c']
>>> del 1
	      
SyntaxError: can't delete literal
>>> del a
	      
>>> a
	      
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> b
	      
30
>>> c
	      
'python'
>>> 
=============================== RESTART: Shell ===============================
>>> a
	      
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> b
	      
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> c
	      
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> a = 2
	      
>>> b = 10
	      
>>> a
	      
2
>>> b
	      
10
>>> del a,b
	      
>>> a
	      
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> b
	      
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> s = 'mango'
	      
>>> s.replace('a','')
	      
'mngo'
>>> s
	      
'mango'
>>> s[4]
	      
'o'
>>> s[5]
	      
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    s[5]
IndexError: string index out of range
>>> a = 10
	      
>>> b = 20
	      
>>> # swap the values without using 3rd vaiable
	      
>>> a
	      
10
>>> b
	      
20
>>> a,b
	      
(10, 20)
>>> a,b = b,a
	      
>>> a
	      
20
>>> b
	      
10
>>> a
	      
20
>>> id(a)
	      
8791207564928
>>> c = 20
	      
>>> id(c)
	      
8791207564928
>>> a
	      
20
>>> c
	      
20
>>> 
