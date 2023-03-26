class Point:
    points = []

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.__class__.points.append(self)

    @classmethod
    def find_closest_point(cls):
        if len(Point.points) <= 1:
            return None
        dic = {i: self.distance_to_point(i) for i in Point.points if i is not self}
        #closest_point = min(dic, key=dic.values)
        return dic
    def distance_to_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_to_point(self, point2):
        return round(((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2) ** 0.5, 2)
    def distance_to_x_axis(self):
        return self.y

    def distance_to_y_axis(self):
        return self.x


point = Point(3, 4)
point_2 = Point(-5, -1)
point_3 = Point(4, 4)
point_4 = Point(1, 1)

closest_point = point.find_closest_point()

print(point.points[0])