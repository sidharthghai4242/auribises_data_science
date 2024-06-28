def add(num1,num2):
    sum=num1+num2+10
    return sum

def square(num):
    return num*num

hello=add

def hello(num1,num2):
    sum=num1+num2-2
    return sum

square=hello


result=hello(num1=5,num2=3)
print(result)