from manim import *

class CuteLoop(Scene):
    def construct(self):
        # Configuration
        colors = [PINK, BLUE, ORANGE, TEAL]
        logo = ImageMobject("assets/manim-image.png").scale(1.5).set_opacity(0)
        
        # Create cute floating circles
        circles = VGroup(*[
            Circle(radius=0.5, color=c, fill_opacity=0.6).shift(
                RIGHT * np.random.uniform(-4, 4) + UP * np.random.uniform(-2, 2)
            )
            for c in colors * 2
        ])

        # Animation Sequence (Loopable)
        # Start state: Circles are small and invisible
        for c in circles:
            c.scale(0)

        # 1. Pulse in the circles
        self.play(
            *[c.animate.scale(1.5).set_opacity(0.8) for c in circles],
            run_time=2,
            rate_func=slow_into
        )
        
        # 2. Move circles to the background and bring in the logo
        self.play(
            *[c.animate.shift(c.get_center() * 0.2).scale(0.8).set_opacity(0.3) for c in circles],
            logo.animate.set_opacity(1).scale(1.2),
            run_time=2
        )
        
        self.wait(1)
        
        # 3. Pulse the logo slightly
        self.play(logo.animate.scale(1.1), run_time=1, rate_func=there_and_back)
        
        self.wait(1)

        # 4. Return to START state (Circles shrink, logo fades)
        # This makes the loop seamless if played on repeat
        self.play(
            *[c.animate.scale(0).set_opacity(0) for c in circles],
            logo.animate.set_opacity(0).scale(0.8),
            run_time=2,
            rate_func=rush_from
        )
        
        self.wait(0.5)
