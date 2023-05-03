# Day 83 coding Statement: 

z=0
while True:
    n=int(input('Enter length: '))
    if n==0:
        break
    s=list(map(int,input('Enter elements of binary tree: ').split()))
    tree_dict={}
    for i,n in enumerate(s):
        l=[]
        left_child=2*i+1
        right_child=2*i+2
        if (left_child>len(s) and right_child>len(s)) or left_child>len(s) or right_child>len(s):
            continue
        elif left_child<len(s) and right_child<len(s):
            l.append(s[left_child])
            l.append(s[right_child])
        elif left_child<len(s):
            l.append(s[left_child]) 
        elif right_child<len(s):
            l.append(s[right_child])
        tree_dict[n]=l

    for w in s[::-1]:
        if w in tree_dict:
            for key1 in tree_dict:
                if w==key1:
                    one,two=tree_dict[w][0],tree_dict[w][1]
                    pi=w*max(one,two)

            for key in tree_dict:
                for e, value in enumerate(tree_dict[key]):
                    if w==value:
                        tree_dict[key][e] = pi

    print(pi)