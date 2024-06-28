user_name=["john.j","fionna","harry_h","leo.32","ben_a"] #list
names=["john jackson","fionna flynn","harrison","leonardo","bennethan"]
key=0
for i in range(0,len(user_name)):
    if(user_name[i]=="harry_h"):
        print(names[i])
        key=1
        break
if(key==0):
    print("user not found")