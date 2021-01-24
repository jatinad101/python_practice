'''
def decimaltobinary(num):
    if num>1:
        decimaltobinary(num//2)
    print(num%2,end='')

n = input()
k = decimaltobinary(n)
a = k.split('0').count('1')
print(a)
'''


def func(num):
    return num[2:]
    
n = int(input().strip())
a = max(func(bin(n)).split('0')).count('1')
print(a)
