s='vaishnavinitinuttarkar'
t='vaish'
# # count=s.count(t)
# # print(count)

# s1=s.replace('abc','1')
# s1=s.replace('b','2')
# # s1=s.replace('c','3')
# a=[]
# for i in s:
#     if t[i] in s:
#         counta=0
#         for i1 in s:
#             if 'a'==i1:
#                 counta+=1
#     a.append(counta)
# print(s1)
si=''
j=0
for i in s:
    for j in t:
        # print('i =',i,'j =',j)
        if i==j:
            si+=i
            print(si)
ind1=0
count,c1=0,0
for ind in si:
    if ind==t[ind1]:
        count+=1
        ind1+=1
        if count==len(t):
            c1+=1
            count=0

