def add(num1,num2):
    result= num1+num2
    print("result is: {}".format(result))

print(hex(id(add)))
print(add)
add(10,20)

hello=add

hello(11,22)

def add(num1,num2,num3):
    result= num1+num2+num3+10
    print("result is",result)

print(hex(id(add)))
print(add)

add(10,20,30)

