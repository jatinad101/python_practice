Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8]],
       [[ 9, 10, 11],
        [12, 13, 14],
        [15, 16, 17]],
       [[18, 19, 20],
        [21, 22, 23],
        [24, 25, 26]]])
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    array([[[ 0,  1,  2],
NameError: name 'array' is not defined
>>> import numpy as np
>>> array=([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8]],
       [[ 9, 10, 11],
        [12, 13, 14],
        [15, 16, 17]],
       [[18, 19, 20],
        [21, 22, 23],
        [24, 25, 26]]])
>>> arr=np.array(array)
>>> arr[3, :-1]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    arr[3, :-1]
IndexError: index 3 is out of bounds for axis 0 with size 3
>>> arr[2, :-1]
array([[18, 19, 20],
       [21, 22, 23]])
>>> arr[2, -1:]
array([[24, 25, 26]])
>>> arr[1, 1:]
array([[12, 13, 14],
       [15, 16, 17]])
>>> arr[:,-1]
            
            
