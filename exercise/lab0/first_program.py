Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello world!")
Hello world!
>>> print x
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> print("X")
X
>>> print("welcome to CS 5001!")
welcome to CS 5001!
>>> 
>>> 
>>> def main():
...     print("Welcome to CS 5001!")
... 
...     
>>> if __name__== "__main__":
...     main()
... 
...     
Welcome to CS 5001!

>>> 
>>> def main():
...     my_number = int(input("Enter a number:"))
...     print("The next number is", my_nuumber +1)
... 
...     
>>> if __name__ == "__main__":
...     main()
