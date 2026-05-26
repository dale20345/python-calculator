def add(a, b):
    return a + b

def min(a, b):
    return a - b

print('첫 번째 수를 입력하세요: ')
a = int(input())
print('두 번째 수를 입력하세요: ')
b = int(input())
print('연산자를 입력하세요: ')
c = input()

if c == '+':
    print(add(a,b))
elif c == '-':
    print(min(a,b))
else:
    print('연산자를 올바르게 입력하세요.')