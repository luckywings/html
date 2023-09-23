s=input("emter the string \n")
rev=""
for i in s:
    rev=i+rev
print("reversed string",rev)
if(s==rev):
    print("the string is palindrome")
else:
    print("the string is not a palindrome")