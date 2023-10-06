# # p=7
# # o=6
# # for i in range(0 , 5):

# #     for k in range(0,p):
# #         print(end="  ")
# #     p=p-1
# #     print("*",end=" ")
# #     for j in range(i, 0, -1,):
# #         #  print("*", end=' ')
# #         print( " " ,end="")
# #         print( " * ", end=" ")
# #     for m in range(7,7):
# #      print(" ", end=" ")
     
# # rows = 7
# # i = 1
# # while i <= rows:
# #     j = rows
# #     while j > i:
# #         # display space
# #         print(' ', end=' ')
# #         j -= 1
# #     print('*', end=' ')
# #     k = 1
# #     p=4
# # for i in range(0 , 17):

# #     for k in range(0,p):
# #         print("",end=" ")
# #         print("* ",end="  ")
# #         p=p-1
# # print( )

# # while k < 2 * (i - 1):
# #     print(' ', end=' ')
# #     k += 1
# # if i == 1:
# #     print()
# # else:
# #     print('*')
# # i += 1
# # print(" * ", end=" ")
# # print( )
# # # p=4
# # # for i in range(0 , 17):

# # #     for k in range(0,p):
# # #         print("",end=" ")
# # #         print("* ",end="  ")
# # #         p=p-1
# # #     print( )

# n=1
# for i in range(0,n):
#     print("*",end=" ")
#     print()
# for j in range(0,n):
#               print(n)
# print()
# c=2
# for a in range(0,c):
#     print("*", end=" ")
# print()
# rows = 1
# for i in range(1, rows+1): 
#     for j in range(1 ,i+2):
#         print(j, end=" ")
#     print('')
# z=3
# for a in range(0,z):
#     print("*", end=" ")
# print()   
# b=4
# for i in range(3, b):
#     for j in range(i, 0,-1):
#         print(j, end=' ')
#     print("")
# z=4
# for a in range(0,z):
#     print("*", end=" ")
# print()  
# rows = 1
# for i in range(1, rows+1): 
#     for j in range( 1,i+4):
#         print(j, end=" ")
#     print('')
# z=5
# for a in range(0,z):
#     print("*", end=" ")
# print()
# b=6
# for i in range(5, b):
#     for j in range(i, 0,-1):
#         print(j, end=' ')
#     print("") 
# z=6
# for a in range(0,z):
#     print("*", end=" ")
# print()
# rows = 1
# for i in range(1, rows+1): 
#     for j in range( 1,i+6):
#         print(j, end=" ")
#     print('')


# def bin(dec):
#    x=""
#    while dec>0:
#         r=dec%2
#         x=str(r)+x
#         dec=dec//2
#    return x
# def oct(dec):
#     y=" "
#     while dec>0:
#         r=dec % 8 
#         y=str(r)+y
#         dec=dec//8
#     return y
# def hex(dec):
#     z=" "
#     while dec>0:
#         r=dec%16
#         if r<10:
#             z=str(r)+z
#         dec=dec//16
#     return z
# dec=int(input("enter a decimal number."))


# a=bin(dec)
# b=oct(dec)
# c=hex(dec)
# print("binary number:",a)
# print("octal number",b)
# print("hexadecimal number",c)

# n=[2,9,8,1,3]
# n.sort()
# print(" list in asending order:",n)

# n.sort(reverse=True)
# print("list in descending order:",n)

# tl=["apple","app","cherry","book","case","banana"]
# def util_func(x,y):
#     return x[0]==y[0]
# res=[]
# for sub in tl:
#     ele=next((x for x in res if util_func(sub,x[0])),[ ])
#     if ele==[]:
#         res.append(ele)
#     ele.append(sub)
# print(res)


# def pcout(arr,n,k):

#     for i in range(0,n):
#         for j in range(i+1,n):
#             if arr[i]+ arr[j]==k:
           

# arr=["abaabbaaabbb"]
# n=len(arr)
# k="ab"
# print(pcout(arr,n,k))       
                



# tl="abaabbaaabbb"
# d=[]
# x=tl[0]
# for i in tl[ 1:]:
#     if i==x[-1]:
#         x+=i
#     else:
#         d.append(x)
#         x+=i
# d.append(i)
# d=[a for a in d if len(a)>1]
# print(d)
# s="p y th o n "
# print('.'.join(c[0] for c in s.split()))



# ellipsis="."
# things=["p,y,th,o,n"]
# print(ellipsis.join(things))

# t=" the lucky wings "
# res=len(t.split())
# print("the no of words in string:"+str(res))



# def ls(s):
#  s= s.split()
#  print(max(s,key=len))
# if __name__ =="__main__":
#     s="the lucky wing"
#     ls(s)


# t="The Lucky Wings"
# res=[char for char in t if char.isupper()]
# print("the uppercase char in string\n:"+str(res))




















