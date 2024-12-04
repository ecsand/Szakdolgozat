list=["a", "aa", "cc", 'a', "aaaaa", "aaa"]
l2=[]
i=0

for x in range(1, len(list)):
    for x in range(0, len(list)):
        if len(list[x])>len(list[x-1]):
            maxa=list[x]
            maxi=x
    l2.append(list[maxi])
    list.remove(list[maxi])
l2.append(list[0])           
print(l2)