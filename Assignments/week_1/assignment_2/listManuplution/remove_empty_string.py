# 3. Remove empty strings from the list of strings

lst=["apple","","banana","orange",""]
newlist=[]
for x in lst:
    if x !='' :
        newlist.append(x)
print(newlist)