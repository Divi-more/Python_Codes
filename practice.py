str1 = "user one demo"
str2 = "demo"

index= str1.index(str2)

if index != -1:
    print(index)
else:
    print("Not found")

# if str2 in str1:
#     for i in range(len(str1)):
#         # if str1[i: i + len(str2)] == str2:
#         if str1.startswith(str2, i):
#             print("Found at index: ", i)
#             break        
# else:
#     print("Not found")