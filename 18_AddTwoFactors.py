# Day 18 coding Statement : Write a program to Add two fractions

# to find gcm
'''
Algo for gcd:
two var a and b
factors of a and b
finding common in both
print the largest
'''
x1,y1=input('Enter x1 and y1: ').split()
x2,y2=input('Enter x1 and y1: ').split()
x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)

def addTwoFractions(x1,y1,x2,y2):
    def gcd(a,b):
        def Factors(n):
            first=[]
            i=1
            while i<=n:
                if n%i==0:
                    first.append(i)
                i+=1
            return first
        FirstFactors=set(Factors(a))
        SecondFactors=set(Factors(b))
        CommonFactorList=list(FirstFactors & SecondFactors)

        def GreatestNumber(CommonFactorList):
            greatestno=0
            if len(FirstFactors & SecondFactors)>1:
                for val in CommonFactorList:   
                    if val> greatestno:
                        greatestno=val
                return greatestno    
            else:
                return CommonFactorList[0]   
        main_gcd=GreatestNumber(CommonFactorList)
        return main_gcd

    def simplify(x3,y3):
        gcd1=gcd(x3,y3)
        x=int(x3/gcd1)
        y=int(y3/gcd1)
        print(x,'/',y)

    if y1==y2:
        x3=x1+x2
        y3=y1
        simplify(x3,y3)
    else:
        x3=(x1*y2)+(x2*y1)
        y3=y1*y2
        simplify(x3,y3)

addTwoFractions(x1,y1,x2,y2)