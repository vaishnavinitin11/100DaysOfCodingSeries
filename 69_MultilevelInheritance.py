# Day 69 coding Statement : Suppose, we have a class A which is the base class and we have a class B which is derived from class A and we have a class C which is derived from class B, we can access the functions of both class A and class B by creating an object for class C.

class Isosceles:
    def dispay_Isosceles(self):
        print('I am an isosceles triangle I am a triangle')

class Equilateral(Isosceles):
    def display_Equilateral(self):
        print('I am an equilateral triangle.')

class C(Equilateral):
    def displayC(self):
        print('I am a triangle')

s=C()

s.display_Equilateral()
s.dispay_Isosceles()
s.displayC()
