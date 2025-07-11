# Factory example
from turtle import circle


class ShapeFactory:
    def create_shape(self, type):
        if type == "circle":
            return circle()
        elif type == "square":
            return Square() # type: ignore

