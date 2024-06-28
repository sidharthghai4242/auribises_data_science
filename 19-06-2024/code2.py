def add(num1,num2,num3):
    result= num1+num2+num3
    print("result is: {}".format(result))

add(num1=10,num3=30,num2=20)

def square(num=5):
    result=num*num
    print("result is: {}".format(result))

square()
square(3)
square(9)

def subtract(num1,num2=5):
    result= num1-num2
    print("result is: {}".format(result))

subtract(num1=10)