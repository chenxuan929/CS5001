Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> ''.join(['hello', 'world'])
'helloworld'
>>> x = ['hello', 'world', "I'm", 'here' '!']
>>> x.sort()
>>> x
["I'm", 'hello', 'here!', 'world']
>>> x.pop()
'world'
>>> x
["I'm", 'hello', 'here!']
>>> x.sort(key = str.lower)
>>> x
['hello', 'here!', "I'm"]
