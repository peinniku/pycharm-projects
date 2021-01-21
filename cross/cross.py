class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def show(self):
        print('点的坐标为({},{})'.format(self.x, self.y))


class Line:
    def __init__(self, a=1.0, b=1.0, c=0.0):
        self.a = a
        self.b = b
        self.c = c

    def show(self):
        print('直线的方程为：{}*x+{}*y+{}=0'.format(self.a, self.b, self.c))


class Circle:
    def __init__(self, center=Point(0, 0), r=1.0):
        self.center = center
        self.r = r

    def show(self):
        print('圆的标准方程为：(x-{})^2+(y-{})^2={}^2'.format(self.center.x, self.center.y, self.r))


class Rectangle:
    def __init__(self, pa=Point(-1, 1), pc=Point(1, -1)):
        self.pb = Point()
        self.pd = Point()
        self.pa = pa
        self.pc = pc

        self.pb.y = pa.y
        self.pb.x = pc.x

        self.pd.y = pc.y
        self.pd.x = pa.x

    def show(self):
        print('矩形的四个顶点分别为：')
        print('({},{}),({},{})\n({},{}),({},{})'.format(self.pa.x, self.pa.y, self.pb.x, self.pb.y,
                                                        self.pd.x, self.pd.y, self.pc.x, self.pc.y))


def line_line_inter(l1, l2):
    inter = Point()

    if l1.a * l2.b != l2.a * l1.b:
        inter.x = (l1.b * l2.c - l2.b * l1.c) / (l1.a * l2.b - l2.a * l1.b)
        inter.y = (l2.a * l1.c - l1.a * l2.c) / (l1.a * l2.b - l2.a * l1.b)
    elif l1.b * l2.c == l2.b * l1.c and l1.a * l2.c == l2.a * l1.c:
        print('两直线重合')
        return 0
    else:
        print('两直线平行')
        return 0

    inter.show()
    return inter


def line_circle(l, c):
    inter1 = Point()
    inter2 = Point()
    if l.b == 0:
        if abs(-l.c / l.a - c.center.x) > c.r:
            print('直线与圆没有交点')
        elif abs(-l.c / l.a - c.center.x) == c.r:
            inter1.y = c.center.y
            inter1.x = -l.c / l.a
            print('直线与圆有一个交点')
            inter1.show()
        else:
            inter1.x = inter2.x = -l.c / l.a
            h = (c.r ** 2 - (-l.c / l.a - c.center.x) ** 2) ** 0.5
            inter1.y = c.center.y + h
            inter2.y = c.center.y - h
            print('直线与圆有两个交点')
            inter1.show()
            inter2.show()
    else:
        k = -l.a / l.b
        b = -l.c / l.b
        e = c.center.x
        d = c.center.y
        r = c.r

        delta = (2 * k * (b - d) - 2 * e) ** 2 - 4 * (k * k + 1) * ((b - d) * (b - d) + e * e - r * r)

        if delta < 0:
            print('直线与圆没有交点')
        elif delta == 0:
            inter1.x = (e - k * (b - d)) / (1 + k * k)
            inter1.y = k * inter1.x + b
            print('直线与圆有一个交点')
            inter1.show()
        else:
            inter1.x = (2 * e - 2 * k * (b - d) + delta ** 0.5) / (
                    2 * k * k + 2)
            inter1.y = k * inter1.x + b
            inter2.x = (2 * e - 2 * k * (b - d) - delta ** 0.5) / (
                    2 * k * k + 2)
            inter2.y = k * inter2.x + b
            print('直线与圆有两个交点')
            inter1.show()
            inter2.show()


def line_rectangle(l, r):
    if l.a * l.b != 0:
        p1 = -(l.b / l.a) * r.pa.y - l.c * l.a
        p2 = -(l.a / l.b) * r.pb.x - l.c * l.b
        p3 = -(l.b / l.a) * r.pd.y - l.c * l.a
        p4 = -(l.a / l.b) * r.pa.x - l.c * l.b

        if not (r.pa.x <= p1 <= r.pb.x or r.pc.y <= p2 <= r.pb.y or r.pd.x <= p3 <= r.pc.x or r.pd.y <= p4 <= r.pa.y):
            print('直线与矩形没有交点')
            return
        if r.pa.x <= p1 < r.pb.x:
            print('直线与矩形交点为：({},{})'.format(p1, r.pa.y))
        if r.pc.y < p2 <= r.pb.y:
            print('直线与矩形交点为：({},{})'.format(r.pb.x, p2))
        if r.pd.x < p3 <= r.pc.x:
            print('直线与矩形交点为：({},{})'.format(p3, r.pd.y))
        if r.pd.y <= p4 < r.pa.y:
            print('直线与矩形交点为：({},{})'.format(r.pa.x, p4))
    else:
        if l.a == 0:
            y = -l.c / l.b
            if r.pd.y < y < r.pa.y:
                print('直线与矩形交点为：({},{})'.format(r.pa.x, y))
                print('直线与矩形交点为：({},{})'.format(r.pb.x, y))
            elif y == r.pd.y:
                print('直线与矩形下边界重合')
            elif y == r.pa.y:
                print('直线与矩形上边界重合')
            else:
                print('直线与矩形无交点')
        else:
            x = -l.c / l.a
            if r.pa.x < x < r.pb.x:
                print('直线与矩形交点为：({},{})'.format(x, r.pa.y))
                print('直线与矩形交点为：({},{})'.format(x, r.pd.y))
            elif x == r.pa.x:
                print('直线与矩形左边界重合')
            elif x == r.pb.x:
                print('直线与矩形右边界重合')
            else:
                print('直线与矩形无交点')


if __name__ == '__main__':
    l1 = Line(2, 0, 6)
    l2 = Line(0, 1, 0)
    # line_line_inter(l1, l2)

    c = Circle(Point(0, 0), 1)
    # line_circle(l2, c)

    r = Rectangle(Point(-1, 1), Point(1, -1))
    line_rectangle(l2, r)
