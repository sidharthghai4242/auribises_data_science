# promo code is ZOMATO
# condition1: more than 249
# condition2: 50%off upto 150

amount=float(input())
promo_code=input()
min_amt=float(input())
if(promo_code=="Zomato"):
    print("Code Valid")
    if(amount > min_amt):
        print("Code applicable")
        discount=amount*0.5
        if(discount > 150):
            print("Pay:-",amount-150)
        else:
            print("Pay:-",amount-discount)  
    else:
        print("Code not applicable")
else:
    print("Code invalid")
