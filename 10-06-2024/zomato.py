#condition:- promo applicable if and only if min_amt=500
promo_code = "GET200"
amount = float(input())
min_amt = 500
if(amount >= min_amt):
    print("Promo 'GET200' applicable")
    amount-=200
    print("Promo applied successfully, plz pay",amount)
else:
    print("Promo 'GET200' not applicable")
    print("Add items worth:- ",min_amt-amount)
