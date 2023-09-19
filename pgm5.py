# total no-of words in string
str1=input("Please enter a string : ")
count=1
i=0
while i<len(str1):
    if(str1[i]== ''):
        count=count+1
    i=i+1
print("Total number of words in the given string= ",count)

# a=input("enter the string:\n")
# i=0
# d=[]
# while(i<len(a)):
#     if i<5:
#         d.append(a)
#     i=i+1
    
# print(d)

# a=int(input("enter the limt"))
# l1=[]
# i=0
# while i<a: