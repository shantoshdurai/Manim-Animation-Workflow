from manim import *


class EquationScene(Scene):
    def construct(self):
        eq1 = MathTex(r"e^{i\pi} + 1 = 0", font_size=72)
        eq2 = MathTex(r"a^2 + b^2 = c^2", font_size=72)

        self.play(Write(eq1))
        self.wait(1)
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(1)
        self.play(FadeOut(eq2))


class GraphScene(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": BLUE},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        sin_graph = axes.plot(lambda x: np.sin(x), color=YELLOW)
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)

        sin_label = axes.get_graph_label(sin_graph, label=r"\sin(x)", x_val=2)
        cos_label = axes.get_graph_label(cos_graph, label=r"\cos(x)", x_val=2, direction=DOWN)

        self.play(Create(axes), Write(labels))
        self.play(Create(sin_graph), Write(sin_label))
        self.play(Create(cos_graph), Write(cos_label))
        self.wait(2)


class NumberLineScene(Scene):
    def construct(self):
        number_line = NumberLine(x_range=[-5, 5, 1], length=10, include_numbers=True)
        dot = Dot(color=RED).move_to(number_line.n2p(0))
        label = always_redraw(
            lambda: MathTex(str(round(number_line.p2n(dot.get_center()), 1)))
            .next_to(dot, UP)
        )

        self.play(Create(number_line))
        self.play(FadeIn(dot), Write(label))
        self.play(dot.animate.move_to(number_line.n2p(3)), run_time=2)
        self.play(dot.animate.move_to(number_line.n2p(-2)), run_time=2)
        self.wait(1)
