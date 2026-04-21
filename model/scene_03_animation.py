from manim import *


class MovementDemo(Scene):
    def construct(self):
        dot = Dot(color=YELLOW, radius=0.2)

        self.play(FadeIn(dot))
        self.play(dot.animate.move_to(RIGHT * 3))
        self.play(dot.animate.move_to(UP * 2))
        self.play(dot.animate.move_to(LEFT * 3 + DOWN * 2))
        self.play(dot.animate.move_to(ORIGIN))
        self.wait(1)


class ColorAndOpacity(Scene):
    def construct(self):
        square = Square(side_length=2, color=BLUE, fill_opacity=0.5)

        self.play(Create(square))
        self.play(square.animate.set_fill(RED, opacity=0.8))
        self.play(square.animate.set_stroke(GREEN, width=6))
        self.play(square.animate.set_fill(YELLOW, opacity=0.2))
        self.wait(1)


class Updaters(Scene):
    def construct(self):
        dot = Dot(color=RED)
        label = always_redraw(
            lambda: MathTex(
                f"({round(dot.get_x(), 1)},\\ {round(dot.get_y(), 1)})"
            ).next_to(dot, UP * 0.5)
        )

        self.add(dot, label)
        self.play(dot.animate.move_to(RIGHT * 2 + UP), run_time=2)
        self.play(dot.animate.move_to(LEFT * 2 + DOWN), run_time=2)
        self.play(dot.animate.move_to(ORIGIN), run_time=1)
        self.wait(1)


class CameraZoom(MovingCameraScene):
    def construct(self):
        text = Text("Zoom In", font_size=48)
        small_text = Text("Tiny Detail", font_size=12).shift(DOWN * 0.3)

        self.play(Write(text))
        self.play(Write(small_text))
        self.wait(0.5)
        self.play(self.camera.frame.animate.scale(0.3).move_to(small_text))
        self.wait(1)
        self.play(self.camera.frame.animate.scale(1 / 0.3).move_to(ORIGIN))
        self.wait(1)
