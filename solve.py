from dataclasses import dataclass
import numpy as np

c = 299792458

class Point:
    def __init__(self, *args):
        if len(args) > 4 or len(args) < 3:
            raise Exception("too many arguments provided")
            
        self.x = args[0] 
        self.y = args[1]
        self.z = args[2] + c * (0 if len(args) == 3 else args[3]) * 1e-9

    def __repr__(self):
        return f"(x, y, z): ({self.x}, {self.y}, {self.z})"

    def __add__(self, other_point):
        return self.__class__(
                self.x + other_point.x,
                self.y + other_point.y,
                self.z + other_point.z,
              )

    def __sub__(self, other_point):
        return self.__class__(
                self.x - other_point.x,
                self.y - other_point.y,
                self.z - other_point.z,
              )

    def dot(self, other_point):
        return float(
                self.x * other_point.x +
                self.y * other_point.y +
                self.z * other_point.z
                ) 

    def out(self, other_point):
        return self.__class__(
                self.y * other_point.z - self.z * other_point.y,
                self.z * other_point.x - self.x * other_point.z,
                self.x * other_point.y - self.y * other_point.x,
                )

    def norm(self):
        abs_val = np.sqrt(self.dot(self))

        if abs_val == 0: 
            raise ZeroDivisionError("zero div")

        return self.__class__(
                self.x / abs_val,
                self.y / abs_val,
                self.z / abs_val
                )


def solve(point_list: [Point]) -> Direction:

    if len(point_list) != 3:
        raise TooManyPointsError
    
    base_point: Point = point_list[0]
    
    diff_vec1: Point = point_list[1] - base_point
    diff_vec2: Point = point_list[2] - base_point

    outer = diff_vec1.out(diff_vec2).norm()
    print("theta:", np.arccos(outer.z) * 360 / 2 / np.pi, "phi:", np.arctan(outer.y / outer.x) * 360 / 2 / np.pi)

if __name__ == "__main__":
    solve([Point(0, 0, 0, 14), Point(10, 0, 0, 6), Point(0, 10, 0, 0)])
