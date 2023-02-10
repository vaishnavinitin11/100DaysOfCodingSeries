# Day 72 coding Statement : In this problem you will have to implement a simple editor. The editor maintains the content of a string S and have two following functions:

# "+ i x": insert a string x into the current string S after the i'th character of the S (we use 1-indexing in this problem). When i equals to 0 it mean we add x at the beginning of S.
# "? i len": Print the sub-string of length len starting at position i'th of S.
# At the beginning, the editor holds an empty string. There will be Q queries of the two types described above.


tc=int(input('Enter tc: '))
S=''
S1=''
for i in range(tc):
    s=input('Enter function: ')

    if s[0]=='+':
        if s[1]=='0':
            S1=s[2:]+S[:]
            S=S1
        else:
            inti=int(s[1])
            S1=S[:inti]+s[2:]+S[inti:]
            S=S1
    elif s[0]=='?':
        intstart=int(s[1]);intend=int(s[2])
        print(S[(intstart-1):intend])

