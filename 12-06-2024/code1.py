for i in range(0,8):
    for j in range(0,8):
        if(i%2==0):
            # print("\u25A0",end=" ")
            if(j%2==0):
                print("\u25A1",end=" ")
            else:
                print("\u25A0",end=" ")
        if(i%2!=0):
            if(j%2==0):
                print("\u25A0",end=" ")
            else:
                print("\u25A1",end=" ")
    print()