def addition(b):
    c=int(input())
    b=b+c
    return b
def subtraction(b):
    c=int(input())
    b=b-c
    return b
def multiplication(b):
    c=int(input())
    b=b*c
    return b
def division(b):
    c=int(input())
    b=b/c
    return b
i=0
a=int(input())
a=0+a
while(i!="="):
    i=input()
    if i=='+':
      d=int(addition(a))
    if i=='-':
        d=int(subtraction(a))
    if i=='*':
        d=int(multiplication(a))
    if i=='/':
        d=int(division(a))
    a=d
print(a)