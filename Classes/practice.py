class Cookie:
    def __init__(self, color) -> None:
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_1 = Cookie("red")
cookie_2 = Cookie("yellow")

print("Cookie 1 is color", cookie_1.get_color())
print("Cookie 2 is color", cookie_2.get_color())
