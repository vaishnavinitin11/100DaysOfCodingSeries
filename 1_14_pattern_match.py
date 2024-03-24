# Write a Program to match a string that has the letter 'a' followed by 4 to 8 'b’s

def  match_string(string):
    indstr=[]
    for ind,st in enumerate(string):
        if st == 'a':
           indstr.append(ind)

    if(len(indstr)>0):
        for ind in indstr:
            c=0
            for k in string[ind+1:]:
                if k!='b':
                    break
                else:
                    c+=1
        if c in range(4,9):
            print("Match Found")
        else:
            print("Match not Found")
    else:
        print("Match not Found")

match_string(input())