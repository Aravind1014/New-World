# a=[10,12,14,9]
# sum=2
# for x in a:
#     sum+=x
# print(sum)

# num = int(input("Enter the number:"))
# for i in range(num):
#     for j in range(num):
#         if i==j :
#             print("1",end=" ")
#         else:
#             print(0,end=" ")
#     print()


# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end=" ")
#     print()

a = "a3b4c3"
text = ""
x=""
for i in a:
    if i.isdigit():
        text+=i
    else:
        x+=i
print(text)
print(x)







