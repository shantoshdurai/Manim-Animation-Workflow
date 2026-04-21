from manim import *


class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, Manim!", font_size=72)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))


class ShapesDemo(Scene):
    def construct(self):
        circle = Circle(radius=1.5, color=BLUE)
        square = Square(side_length=2, color=RED)
        triangle = Triangle(color=GREEN).scale(1.5)

        shapes = VGroup(circle, square, triangle).arrange(RIGHT, buff=1)

        self.play(Create(circle), Create(square), Create(triangle))
        self.wait(1)
        self.play(shapes.animate.shift(UP))
        self.play(FadeOut(shapes))


class TransformDemo(Scene):
    def construct(self):
        circle = Circle(color=BLUE, fill_opacity=0.5)
        square = Square(color=RED, fill_opacity=0.5)

        self.play(Create(circle))
        self.wait(0.5)
        self.play(Transform(circle, square))
        self.wait(0.5)
        self.play(FadeOut(circle))
