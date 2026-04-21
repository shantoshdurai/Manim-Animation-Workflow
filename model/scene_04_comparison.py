from manim import *

class MathComparison(Scene):
    def construct(self):
        # 1. Normal Text (Attempting to represent math)
        text_title = Text("Normal Text", color=BLUE).to_edge(UP)
        normal_text = Text(
            "E = mc^2  or  (a+b)^2 = a^2 + 2ab + b^2",
            font_size=36
        ).next_to(text_title, DOWN, buff=1)

        # 2. MathTex (Professional LaTeX rendering)
        math_title = Text("MathTex (LaTeX)", color=GREEN).next_to(normal_text, DOWN, buff=1.5)
        math_tex = MathTex(
            r"E = mc^2 \quad \text{or} \quad (a+b)^2 = a^2 + 2ab + b^2",
            font_size=48
        ).next_to(math_title, DOWN, buff=1)

        self.add(text_title, normal_text)
        self.wait(1)
        self.play(Write(math_title), Write(math_tex))
        self.wait(2)

        # Show something Text CANNOT easily do
        complex_title = Text("Complex Math (LaTeX Only)", color=YELLOW).to_edge(UP)
        complex_math = MathTex(
            r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}",
            font_size=72
        )

        self.play(FadeOut(text_title, normal_text, math_title, math_tex))
        self.play(Write(complex_title))
        self.play(Create(complex_math))
        self.wait(3)
