# 5. Replace list’s item with new value if found

list=["apple","banana","orange"]

if "apple" in list:
    index=list.index("apple")
    list[index]="chery"
print(list)