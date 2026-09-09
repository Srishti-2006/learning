# create a 2d coordinate system where user can view 2d coordinates .
#find distance between points and its distance from origin 
#also user can find distance from point to a given line 
class Point:
    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y

    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)  

    def euclidean_distance(self,other):
        return ((self.x_cod-other.x_cod)**2+(self.y_cod-other.y_cod))**0.5  

    def dis_from_origin(self):
        return self.euclidean_distance(Point(0,0))

   
class Line:

    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C

    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A,self.B,self.C)

    def point_on_line(line,point):
        if line.A*point.x_cod+line.B*point.y_cod+line.C ==0:
            return"lies on the line"
        else:
            return "does not lie on the line"

    def shortest_distance(line,point):
       return abs(line.A*point.x_cod+line.B*point.y_cod+line.C)/((line.A**2+line.B**2)**0.5)


p1=Point(1,10)
l1=Line(1,1,-2)
print(l1.shortest_distance(p1))
