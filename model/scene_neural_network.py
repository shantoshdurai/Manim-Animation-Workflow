from manim import *
import numpy as np


class NeuralNetworkMNIST(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # Color Palette & Background (3Blue1Brown Aesthetic)
        # ---------------------------------------------------------
        self.camera.background_color = "#0c0d12"

        NEON_CYAN = "#00f0ff"
        GLOW_YELLOW = "#ffe066"
        SOFT_BLUE = "#3a86ff"
        SOFT_RED = "#ff006e"
        DEEP_GRAY = "#2b2d42"
        TEXT_WHITE = "#edf2f4"

        # ---------------------------------------------------------
        # Act 1: Title & The Handwritten Digit Image (0s - 6s)
        # ---------------------------------------------------------
        title = Text("How a Neural Network Recognizes Digits", font_size=36, color=TEXT_WHITE)
        title.to_edge(UP, buff=0.4)
        subtitle = Text("From Pixels to Predictions • 3Blue1Brown Style", font_size=20, color=NEON_CYAN)
        subtitle.next_to(title, DOWN, buff=0.15)

        self.play(Write(title, run_time=1.2), FadeIn(subtitle, shift=UP * 0.2))
        self.wait(0.5)

        # Draw a simplified 8x8 pixel grid for digit '3'
        grid_dim = 8
        digit_matrix = np.array([
            [0.0, 0.1, 0.8, 0.9, 0.9, 0.8, 0.1, 0.0],
            [0.0, 0.0, 0.1, 0.2, 0.3, 0.9, 0.3, 0.0],
            [0.0, 0.0, 0.0, 0.1, 0.2, 0.9, 0.2, 0.0],
            [0.0, 0.0, 0.2, 0.8, 0.9, 0.8, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.1, 0.3, 0.9, 0.3, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.2, 0.9, 0.4, 0.0],
            [0.0, 0.1, 0.7, 0.9, 0.9, 0.8, 0.2, 0.0],
            [0.0, 0.0, 0.1, 0.2, 0.2, 0.1, 0.0, 0.0],
        ])

        pixel_size = 0.32
        pixel_grid = VGroup()
        for r in range(grid_dim):
            for c in range(grid_dim):
                val = digit_matrix[r, c]
                color = interpolate_color(ManimColor(DEEP_GRAY), ManimColor(GLOW_YELLOW), val)
                sq = Square(side_length=pixel_size, fill_color=color, fill_opacity=0.25 + 0.75 * val)
                sq.set_stroke(color="#1a1c24", width=1)
                sq.move_to(np.array([(c - grid_dim / 2 + 0.5) * pixel_size, (grid_dim / 2 - r - 0.5) * pixel_size, 0]))
                pixel_grid.add(sq)

        image_frame = SurroundingRectangle(pixel_grid, color=NEON_CYAN, buff=0.08, stroke_width=2)
        grid_group = VGroup(pixel_grid, image_frame).move_to(LEFT * 4.6 + DOWN * 0.3)
        grid_label = Text("Input Image\n(28×28 Pixels)", font_size=18, color=TEXT_WHITE, line_spacing=1.2)
        grid_label.next_to(grid_group, DOWN, buff=0.25)

        self.play(FadeIn(grid_group, shift=RIGHT * 0.5), Write(grid_label))
        self.wait(1.0)

        # ---------------------------------------------------------
        # Act 2: Architecture Setup (Input -> Hidden1 -> Hidden2 -> Output) (6s - 13s)
        # ---------------------------------------------------------
        layer_sizes = [6, 8, 8, 10]
        layer_x_coords = [-1.8, 0.4, 2.4, 4.4]
        layer_names = ["Inputs (784)", "Features (16)", "Patterns (16)", "Outputs (0-9)"]
        node_radius = 0.14

        network_layers = []
        layer_labels = VGroup()

        for l_idx, (size, x_pos) in enumerate(zip(layer_sizes, layer_x_coords)):
            layer_nodes = VGroup()
            y_span = 3.6
            y_step = y_span / (size - 1)
            y_start = y_span / 2

            for n_idx in range(size):
                y_pos = y_start - n_idx * y_step + DOWN * 0.3
                node = Circle(
                    radius=node_radius,
                    stroke_color=NEON_CYAN if l_idx == 3 else SOFT_BLUE,
                    stroke_width=2,
                    fill_color="#141824",
                    fill_opacity=0.9,
                )
                node.move_to(np.array([x_pos, y_pos[1], 0]))
                layer_nodes.add(node)

            network_layers.append(layer_nodes)
            lbl = Text(layer_names[l_idx], font_size=14, color=TEXT_WHITE)
            lbl.next_to(layer_nodes, UP, buff=0.3)
            layer_labels.add(lbl)

        # Create synaptic connections with weights (blue = positive, red = negative)
        np.random.seed(42)
        synapses = VGroup()
        for l in range(len(network_layers) - 1):
            curr_layer = network_layers[l]
            next_layer = network_layers[l + 1]
            for n1 in curr_layer:
                for n2 in next_layer:
                    weight = np.random.uniform(-1, 1)
                    color = SOFT_BLUE if weight > 0 else SOFT_RED
                    opacity = 0.08 + 0.22 * abs(weight)
                    line = Line(
                        n1.get_center(),
                        n2.get_center(),
                        stroke_color=color,
                        stroke_width=1.0 if abs(weight) < 0.6 else 1.6,
                        stroke_opacity=opacity,
                    )
                    synapses.add(line)

        # Draw connecting line from image grid to input layer
        transfer_arrows = VGroup()
        for i in range(len(network_layers[0])):
            target = network_layers[0][i].get_center()
            source = grid_group.get_right() + UP * (1.2 - i * 0.48)
            arrow = CurvedArrow(source, target + LEFT * 0.05, angle=-0.2, color=GLOW_YELLOW, stroke_width=1.5, stroke_opacity=0.6)
            transfer_arrows.add(arrow)

        self.play(
            FadeIn(synapses, lag_ratio=0.005),
            *[Create(nodes) for nodes in network_layers],
            Write(layer_labels),
            run_time=2.2,
        )
        self.play(Create(transfer_arrows, lag_ratio=0.1), run_time=1.2)
        self.wait(0.8)

        # ---------------------------------------------------------
        # Act 3: Forward Propagation & Activation Cascades (13s - 20s)
        # ---------------------------------------------------------
        # Formula display
        formula_box = Rectangle(width=4.6, height=0.7, color=NEON_CYAN, fill_color="#10121a", fill_opacity=0.9, stroke_width=1.5)
        formula_box.to_corner(DR, buff=0.5)
        formula_text = Text("a⁽ᴸ⁾ = σ( W⁽ᴸ⁾ · a⁽ᴸ⁻¹⁾ + b⁽ᴸ⁾ )", font_size=18, color=GLOW_YELLOW)
        formula_text.move_to(formula_box.get_center())
        formula_group = VGroup(formula_box, formula_text)

        self.play(FadeIn(formula_group, shift=UP * 0.3))

        # Pulse wave through the layers
        # 1. Inputs activate
        input_pulses = []
        for i, node in enumerate(network_layers[0]):
            val = [0.1, 0.8, 0.95, 0.85, 0.3, 0.05][i]
            input_pulses.append(
                node.animate.set_fill(color=GLOW_YELLOW, opacity=val).set_stroke(color=GLOW_YELLOW, width=3)
            )
        self.play(*input_pulses, run_time=1.0)

        # 2. Layer 1 -> Layer 2 Forward Pulse
        pulse_dots_1 = []
        for _ in range(24):
            n1 = network_layers[0][np.random.randint(len(network_layers[0]))]
            n2 = network_layers[1][np.random.randint(len(network_layers[1]))]
            dot = Dot(n1.get_center(), radius=0.04, color=GLOW_YELLOW)
            pulse_dots_1.append((dot, n1.get_center(), n2.get_center()))

        anims_1 = []
        for dot, p1, p2 in pulse_dots_1:
            self.add(dot)
            anims_1.append(dot.animate(rate_func=linear).move_to(p2))

        self.play(*anims_1, run_time=1.2)
        for dot, _, _ in pulse_dots_1:
            self.remove(dot)

        # Layer 1 nodes illuminate
        l1_pulses = [
            node.animate.set_fill(color=interpolate_color(ManimColor(SOFT_BLUE), ManimColor(NEON_CYAN), np.random.rand()), opacity=np.random.uniform(0.4, 0.95))
            for node in network_layers[1]
        ]
        self.play(*l1_pulses, run_time=0.8)

        # 3. Layer 2 -> Layer 3 Pulse
        pulse_dots_2 = []
        for _ in range(24):
            n1 = network_layers[1][np.random.randint(len(network_layers[1]))]
            n2 = network_layers[2][np.random.randint(len(network_layers[2]))]
            dot = Dot(n1.get_center(), radius=0.04, color=NEON_CYAN)
            pulse_dots_2.append((dot, n1.get_center(), n2.get_center()))

        anims_2 = []
        for dot, p1, p2 in pulse_dots_2:
            self.add(dot)
            anims_2.append(dot.animate(rate_func=linear).move_to(p2))

        self.play(*anims_2, run_time=1.2)
        for dot, _, _ in pulse_dots_2:
            self.remove(dot)

        l2_pulses = [
            node.animate.set_fill(color=NEON_CYAN, opacity=np.random.uniform(0.5, 1.0))
            for node in network_layers[2]
        ]
        self.play(*l2_pulses, run_time=0.8)

        # ---------------------------------------------------------
        # Act 4: Output Layer Classification & Probability Bars (20s - 27s)
        # ---------------------------------------------------------
        # Output digits labels and probability bars
        output_layer = network_layers[3]
        digit_probabilities = [0.01, 0.02, 0.03, 0.94, 0.01, 0.04, 0.01, 0.02, 0.08, 0.02]

        prob_bars = VGroup()
        prob_labels = VGroup()
        target_digit = 3

        for d_idx, (node, prob) in enumerate(zip(output_layer, digit_probabilities)):
            # Digit label next to node
            d_text = Text(str(d_idx), font_size=14, color=GLOW_YELLOW if d_idx == target_digit else TEXT_WHITE)
            d_text.next_to(node, RIGHT, buff=0.15)
            prob_labels.add(d_text)

            # Horizontal probability bar
            bar_max_width = 1.3
            bar_width = max(0.04, bar_max_width * prob)
            bar_color = GLOW_YELLOW if d_idx == target_digit else DEEP_GRAY
            bar = RoundedRectangle(
                corner_radius=0.03,
                height=0.12,
                width=bar_width,
                color=bar_color,
                fill_color=bar_color,
                fill_opacity=0.9 if d_idx == target_digit else 0.4,
                stroke_width=0,
            )
            bar.next_to(d_text, RIGHT, buff=0.15)
            # Align bar left edge
            bar.align_to(d_text.get_right() + RIGHT * 0.15, LEFT)
            prob_bars.add(bar)

        # Pulse into output layer
        pulse_dots_3 = []
        for n1 in network_layers[2]:
            target_node = output_layer[target_digit]
            dot = Dot(n1.get_center(), radius=0.04, color=GLOW_YELLOW)
            pulse_dots_3.append((dot, n1.get_center(), target_node.get_center()))

        anims_3 = []
        for dot, p1, p2 in pulse_dots_3:
            self.add(dot)
            anims_3.append(dot.animate(rate_func=linear).move_to(p2))

        self.play(*anims_3, run_time=1.0)
        for dot, _, _ in pulse_dots_3:
            self.remove(dot)

        # Illuminate output nodes and animate probability bars
        output_illuminations = []
        for idx, (node, prob) in enumerate(zip(output_layer, digit_probabilities)):
            c = GLOW_YELLOW if idx == target_digit else SOFT_BLUE
            op = 1.0 if idx == target_digit else 0.15
            output_illuminations.append(
                node.animate.set_fill(color=c, opacity=op).set_stroke(color=c, width=3 if idx == target_digit else 1.5)
            )

        self.play(
            *output_illuminations,
            FadeIn(prob_labels),
            GrowFromEdge(prob_bars, LEFT),
            run_time=1.5,
        )

        # Highlight winner '3'
        winner_node = output_layer[target_digit]
        winner_ring = Circle(radius=0.28, stroke_color=GLOW_YELLOW, stroke_width=3).move_to(winner_node.get_center())
        winner_glow = Circle(radius=0.38, stroke_color=GLOW_YELLOW, stroke_width=1, stroke_opacity=0.4).move_to(winner_node.get_center())

        confidence_badge = RoundedRectangle(corner_radius=0.1, width=3.2, height=0.6, color=GLOW_YELLOW, fill_color="#12141c", fill_opacity=0.95, stroke_width=2)
        confidence_badge.next_to(prob_bars[target_digit], RIGHT, buff=0.35)
        conf_text = Text("Output: '3'  (94%)", font_size=16, color=GLOW_YELLOW)
        conf_text.move_to(confidence_badge.get_center())
        conf_group = VGroup(confidence_badge, conf_text)

        self.play(
            Create(winner_ring),
            Create(winner_glow),
            FadeIn(conf_group, shift=LEFT * 0.2),
            Flash(winner_node, color=GLOW_YELLOW, flash_radius=0.45, line_length=0.15),
            run_time=1.4,
        )

        self.wait(2.5)

        # Final fade out
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(grid_group),
            FadeOut(grid_label),
            FadeOut(transfer_arrows),
            FadeOut(synapses),
            FadeOut(VGroup(*network_layers)),
            FadeOut(layer_labels),
            FadeOut(formula_group),
            FadeOut(prob_labels),
            FadeOut(prob_bars),
            FadeOut(winner_ring),
            FadeOut(winner_glow),
            FadeOut(conf_group),
            run_time=1.6,
        )
        self.wait(0.5)
