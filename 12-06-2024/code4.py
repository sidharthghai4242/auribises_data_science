def square_of_nums(nums):
    print("number is:- ",nums)
    for idx in range(0,len(nums)):
         nums[idx]*=nums[idx]
    print("number is:- ",nums)

number=[10,20,30,40,50]
print("A, number is:- ",number)
square_of_nums(number)
print("B, number is:- ",number)