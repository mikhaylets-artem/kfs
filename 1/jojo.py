import math
x=0
while x<=4:
    if 0<=x<=1:
        y=math.sin(x)**2
    elif 1 <x<2:
         y=math.sin(x)*-1
    elif 2<=x<3:
         y=math.cos(x)
    elif 3<=x<=4:
        y=math.tan(x)*math.cos(x)
    else:
        print('error')
    print ('y=',round(y),'when x=',x)
    x+=0.5
