import math
x=-8
while x<=8:
    if x>5:
        y=math.sin(x)/x
    elif -5<=x<=5:
        y=x-4
    elif x<-5:
        y=x**3
    else:
        print(error)
     print('y=',round(y,2),'when x=',round(x,2))
     x+=0.3
