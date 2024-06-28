def get_max(data,length):
    if(len(data)==1):
        return data[0]
    else:
        if(data[0]>data[1]):
            data.remove(data[1])
            
        else:
            data.remove(data[0])
    return get_max(data,len(data))

data=[10,20,50,75,30,100]

print(get_max(data,len(data)))
