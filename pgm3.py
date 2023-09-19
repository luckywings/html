import re
rem_char=["!","@","#","$","%","^","&","*"," "]
str="a$d&i t$hy*a"
temp=""
for i in rem_char:
    temp+=i
res=re.sub(rf'[{temp}]','',str)
print(res)