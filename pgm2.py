# a=("carclh;j'k'")
# x = a.capitalize()
# print(x)
a="@#%^a^&dithy*"
len=len(a)
res1,res2="",""
for i in range(0,len):
    c=a[i]
    if c.isalnum():
        res1=res1+c
    else:
        res2=res2+c
print(c)