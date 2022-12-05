# Day 8 coding Statement: Write a program to find roots of a quadratic equation

a,b,c=input('Enter numbers: ').split()
a=int(a)
b=int(b)
c=int(c)

def quadraticeqn(a,b,c):
    squrt=((b**2) - (4*a*c))**0.5
    eqn1=((-b)+squrt)/(2*a)
    eqn2=((-b)-squrt)/(2*a)
    if eqn1 == eqn2:
        print('Roots are equal\n','Root 1 = root 2 =',eqn1)
    else:
        print('Root 1 =',eqn1,',','Root 2 =',eqn2)

quadraticeqn(a,b,c)