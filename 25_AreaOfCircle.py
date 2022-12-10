# Day 25 coding Statement : Write a program to find Area of a circle

radius=int(input('Enter Radius: '))
def AreaOfCircle(radius):
    Area=3.14*radius*radius
    return('%.2f'%Area)

area_circle=AreaOfCircle(radius)
print(area_circle)