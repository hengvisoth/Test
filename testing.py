n = 5
form1 = 0
form2 = 0
string1 = ""
res1 = 0
res2 = 0
string2 = ""
for i in range (1,n+1):

    form1 = (i*2)-1
    form2 = i*2
    res1 += form1
    res2 += form2
    string1+= str(form1) + "+"

    string2 +=  str(form2) + "+"
print(string1+"\b=",res1)
print(string2+"\b=",res2)
print(res1)
print(res2)

