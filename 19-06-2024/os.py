quote1="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
quote2="bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"

file=open("quotes.txt","a")
file.write(quote1)
file.write(quote2)

file.close()
print("Data Written.....")