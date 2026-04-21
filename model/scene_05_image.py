from manim import *

class ImageScene(Scene):
    def construct(self):
        # Load the image from the assets folder
        # Path is relative to where you run the render command
        image = ImageMobject("assets/manim-image.png")
        
        # Scale it a bit and place in center (default is center)
        image.scale(2)
        
        # Add some text above it
        title = Text("My Manim Asset", font_size=48).to_edge(UP)
        
        # Display the title and fade in the image
        self.play(Write(title))
        self.play(FadeIn(image, shift=UP))
        self.wait(2)
        
        # Animate the image moving
        self.play(image.animate.scale(0.5).to_edge(DOWN))
        self.wait(1)
