import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        # 计算周长 2*pi*r
        perimeter = 2 * math.pi * self.radius
        return round(perimeter, 2)

    def get_area(self):
        # 计算面积 pi*r^2
        area = math.pi * (self.radius ** 2)
        return round(area, 2)

if __name__ == "__main__":
    # 测试代码
    r_input = float(input("请输入圆的半径: "))
    c = Circle(r_input)
    
    print(f"半径为 {r_input} 的圆：")
    print(f"周长: {c.get_perimeter()}")
    print(f"面积: {c.get_area()}")