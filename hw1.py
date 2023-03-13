def get_radius() :
    r = int(input())
    return r
def get_circle_area() :
    d = 3.14*r**2
    return d
print('넓이를 구하고자 하는 원의 넓인는?',end = ' ')
r = get_radius()
d = get_circle_area()
print('반지름 ',r,'인 원의 넓이 = 3.14 x ',r,' x ',r,' = ',d)
