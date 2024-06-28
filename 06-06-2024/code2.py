promo_code1="ZOMATO40"
print(promo_code1,type(promo_code1),id(promo_code1))
promo_code2=promo_code1 #refernce copy operation
del promo_code1
print(promo_code2,type(promo_code2),id(promo_code2))
