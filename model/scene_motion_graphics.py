from manim import *
import numpy as np


class OdysseyOfMathAndMind(ThreeDScene):
    def construct(self):
        # -------------------------------------------------------------
        # Universal Aesthetics & Color Palette
        # -------------------------------------------------------------
        self.camera.background_color = "#07080d"

        COLOR_CYAN = "#00f0ff"
        COLOR_MAGENTA = "#ff007f"
        COLOR_YELLOW = "#ffea00"
        COLOR_PURPLE = "#7928ca"
        COLOR_BLUE = "#0070f3"
        COLOR_WHITE = "#ffffff"
        COLOR_GRID = "#141724"

        # =============================================================
        # ACT 1: KINETIC TYPOGRAPHY & VECTOR MATRIX (0.0s - 11.0s)
        # =============================================================
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        # Ambient background grid
        bg_grid = NumberPlane(
            x_range=[-12, 12, 1],
            y_range=[-8, 8, 1],
            background_line_style={"stroke_color": COLOR_GRID, "stroke_width": 1.2, "stroke_opacity": 0.5},
            axis_config={"stroke_color": "#1f2438", "stroke_width": 2},
        )
        self.add(bg_grid)

        # Kinetic Word 1: MATHEMATICS
        t_math = Text("MATHEMATICS", font_size=56, weight=BOLD, color=COLOR_WHITE)
        t_math.set_stroke(color=COLOR_CYAN, width=1.5)
        t_math.move_to(ORIGIN)

        self.play(
            FadeIn(t_math, scale=2.5, rate_func=rush_into),
            run_time=0.8,
        )
        self.play(
            t_math.animate.scale(0.85).set_color_by_gradient(COLOR_CYAN, COLOR_BLUE),
            run_time=0.6,
        )

        # Morph to: IS THE POETRY OF
        t_poetry = Text("IS THE POETRY OF", font_size=38, weight=SEMIBOLD, color=COLOR_YELLOW)
        self.play(
            Transform(t_math, t_poetry),
            run_time=0.8,
        )
        self.wait(0.4)

        # Snap to: LOGICAL IDEAS
        t_ideas = Text("LOGICAL IDEAS", font_size=62, weight=HEAVY, color=COLOR_MAGENTA)
        t_ideas.set_stroke(color=COLOR_WHITE, width=1)
        self.play(
            Transform(t_math, t_ideas),
            Flash(ORIGIN, color=COLOR_MAGENTA, flash_radius=2.0, line_length=0.4, num_lines=16),
            run_time=0.8,
        )
        self.wait(0.5)

        # Transition typography up to become header
        self.play(
            t_math.animate.scale(0.45).to_edge(UP, buff=0.4).set_color(COLOR_WHITE),
            run_time=0.8,
        )

        # Harmonic Unit Circle & Trigonometric Vectors
        circle = Circle(radius=2.0, color=COLOR_BLUE, stroke_width=2.5)
        circle_axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=6, y_length=6, axis_config={"color": "#2c334d"})
        center_dot = Dot(ORIGIN, color=COLOR_WHITE, radius=0.06)

        orbit_dot = Dot(circle.point_at_angle(0), color=COLOR_YELLOW, radius=0.09)
        radius_vector = always_redraw(lambda: Line(ORIGIN, orbit_dot.get_center(), color=COLOR_YELLOW, stroke_width=3))
        cos_line = always_redraw(lambda: Line(ORIGIN, [orbit_dot.get_center()[0], 0, 0], color=COLOR_CYAN, stroke_width=3.5))
        sin_line = always_redraw(lambda: Line([orbit_dot.get_center()[0], 0, 0], orbit_dot.get_center(), color=COLOR_MAGENTA, stroke_width=3.5))

        self.play(
            Create(circle_axes),
            Create(circle),
            FadeIn(center_dot),
            FadeIn(radius_vector),
            FadeIn(cos_line),
            FadeIn(sin_line),
            FadeIn(orbit_dot),
            run_time=1.2,
        )

        # Spin unit circle vector through 2 full rotations
        self.play(
            Rotate(orbit_dot, about_point=ORIGIN, angle=4 * PI),
            run_time=3.2,
            rate_func=linear,
        )

        # Clean Act 1 elements
        self.play(
            FadeOut(circle_axes),
            FadeOut(circle),
            FadeOut(radius_vector),
            FadeOut(cos_line),
            FadeOut(sin_line),
            FadeOut(orbit_dot),
            FadeOut(center_dot),
            FadeOut(t_math),
            run_time=1.0,
        )

        # =============================================================
        # ACT 2: 3D SPACE WARP — TORUS & LORENZ ATTRACTOR (11.0s - 24.0s)
        # =============================================================
        # Dynamic 3D Camera sweep
        self.move_camera(phi=65 * DEGREES, theta=45 * DEGREES, zoom=1.1, run_time=2.0)
        self.begin_ambient_camera_rotation(rate=0.25)

        # Generate a 3D Torus
        torus = Surface(
            lambda u, v: np.array([
                (2.2 + 0.8 * np.cos(v)) * np.cos(u),
                (2.2 + 0.8 * np.cos(v)) * np.sin(u),
                0.8 * np.sin(v),
            ]),
            u_range=[0, TAU],
            v_range=[0, TAU],
            resolution=(32, 16),
            should_make_jagged=False,
            stroke_color=COLOR_CYAN,
            stroke_width=0.8,
            fill_color=COLOR_PURPLE,
            fill_opacity=0.45,
        )

        self.play(Create(torus), run_time=2.2)
        self.wait(1.5)

        # Smooth morph from Torus to Lorenz Strange Attractor
        # Precompute Lorenz trajectory
        dt = 0.012
        sigma, rho, beta = 10.0, 28.0, 8.0 / 3.0
        x, y, z = 0.1, 0.0, 0.0
        lorenz_pts = []
        for _ in range(850):
            dx = sigma * (y - x) * dt
            dy = (x * (rho - z) - y) * dt
            dz = (x * y - beta * z) * dt
            x += dx
            y += dy
            z += dz
            # Scale down and center
            lorenz_pts.append(np.array([x * 0.12, y * 0.12, (z - 25) * 0.12]))

        # Split attractor into colored gradient curves
        curve1 = VMobject(color=COLOR_CYAN, stroke_width=2.5)
        curve1.set_points_smoothly(lorenz_pts[:425])
        curve2 = VMobject(color=COLOR_MAGENTA, stroke_width=2.5)
        curve2.set_points_smoothly(lorenz_pts[425:])

        lorenz_group = VGroup(curve1, curve2)

        lead_particle = Dot(lorenz_pts[0], color=COLOR_YELLOW, radius=0.14)

        self.play(
            ReplacementTransform(torus, lorenz_group),
            FadeIn(lead_particle),
            run_time=2.0,
        )

        # Move the glow dot along the trajectory
        self.play(
            MoveAlongPath(lead_particle, curve1),
            run_time=2.2,
            rate_func=linear,
        )
        self.play(
            MoveAlongPath(lead_particle, curve2),
            run_time=2.2,
            rate_func=linear,
        )

        self.stop_ambient_camera_rotation()

        # =============================================================
        # ACT 3: FOURIER HARMONIC EPICYCLES (24.0s - 36.0s)
        # =============================================================
        # Transition back to 2D view
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, zoom=1.0, run_time=1.8)

        self.play(
            FadeOut(lorenz_group),
            FadeOut(lead_particle),
            run_time=0.8,
        )

        # Construct Fourier Epicycles
        fourier_title = Text("FOURIER HARMONICS", font_size=28, weight=BOLD, color=COLOR_CYAN)
        fourier_title.to_edge(UP, buff=0.5)
        self.play(FadeIn(fourier_title, shift=DOWN * 0.2), run_time=0.8)

        # 3 Cascading Epicycles
        r1, r2, r3 = 1.4, 0.7, 0.35
        w1, w2, w3 = 1.0, -3.0, 5.0  # Harmonic frequencies

        center_origin = LEFT * 2.5 + DOWN * 0.2
        c1 = Circle(radius=r1, color="#243049", stroke_width=1.5).move_to(center_origin)

        # Value tracker for time
        time_tracker = ValueTracker(0)

        # Compute dynamic epicycle positions
        def get_p1():
            t = time_tracker.get_value()
            return center_origin + np.array([r1 * np.cos(w1 * t), r1 * np.sin(w1 * t), 0])

        def get_p2():
            t = time_tracker.get_value()
            p1 = get_p1()
            return p1 + np.array([r2 * np.cos(w2 * t), r2 * np.sin(w2 * t), 0])

        def get_p3():
            t = time_tracker.get_value()
            p2 = get_p2()
            return p2 + np.array([r3 * np.cos(w3 * t), r3 * np.sin(w3 * t), 0])

        c2 = always_redraw(lambda: Circle(radius=r2, color="#2c3c5f", stroke_width=1.2).move_to(get_p1()))
        c3 = always_redraw(lambda: Circle(radius=r3, color="#344874", stroke_width=1.0).move_to(get_p2()))

        v1 = always_redraw(lambda: Arrow(center_origin, get_p1(), buff=0, color=COLOR_BLUE, stroke_width=2.5, tip_length=0.12))
        v2 = always_redraw(lambda: Arrow(get_p1(), get_p2(), buff=0, color=COLOR_CYAN, stroke_width=2.0, tip_length=0.10))
        v3 = always_redraw(lambda: Arrow(get_p2(), get_p3(), buff=0, color=COLOR_YELLOW, stroke_width=1.8, tip_length=0.08))

        pen_dot = always_redraw(lambda: Dot(get_p3(), color=COLOR_MAGENTA, radius=0.07))

        # Traced curve
        traced_curve = TracedPath(pen_dot.get_center, stroke_color=COLOR_YELLOW, stroke_width=2.8)

        # Frequency Spectrum analyzer bars on the right
        spectrum_group = VGroup()
        bar_heights = [1.8, 1.2, 2.4, 0.8, 1.6, 2.1, 0.5, 1.4, 2.7, 1.1]
        for idx, h in enumerate(bar_heights):
            bar = RoundedRectangle(
                corner_radius=0.05,
                width=0.22,
                height=h,
                color=COLOR_CYAN if idx % 2 == 0 else COLOR_MAGENTA,
                fill_color=COLOR_CYAN if idx % 2 == 0 else COLOR_MAGENTA,
                fill_opacity=0.75,
                stroke_width=0,
            )
            bar.move_to(RIGHT * (1.2 + idx * 0.38) + DOWN * (1.5 - h / 2))
            spectrum_group.add(bar)

        spectrum_label = Text("SPECTRAL DECOMPOSITION", font_size=16, color=COLOR_WHITE)
        spectrum_label.next_to(spectrum_group, UP, buff=0.3)

        self.play(
            Create(c1),
            FadeIn(c2),
            FadeIn(c3),
            FadeIn(v1),
            FadeIn(v2),
            FadeIn(v3),
            FadeIn(pen_dot),
            FadeIn(spectrum_group, lag_ratio=0.08),
            Write(spectrum_label),
            run_time=1.4,
        )
        self.add(traced_curve)

        # Animate epicycles drawing the curve while spectrum bars dance
        def bounce_spectrum(mob, dt):
            t = time_tracker.get_value()
            for i, rect in enumerate(mob):
                scale_factor = 0.7 + 0.3 * np.sin(t * 4 + i * 0.8)
                rect.stretch_to_fit_height(bar_heights[i] * scale_factor, about_edge=DOWN)

        spectrum_group.add_updater(bounce_spectrum)

        self.play(
            time_tracker.animate.set_value(TAU * 1.5),
            run_time=4.6,
            rate_func=linear,
        )

        spectrum_group.remove_updater(bounce_spectrum)

        # Cleanup Act 3
        self.play(
            FadeOut(c1),
            FadeOut(c2),
            FadeOut(c3),
            FadeOut(v1),
            FadeOut(v2),
            FadeOut(v3),
            FadeOut(pen_dot),
            FadeOut(traced_curve),
            FadeOut(spectrum_group),
            FadeOut(spectrum_label),
            FadeOut(fourier_title),
            run_time=1.0,
        )

        # =============================================================
        # ACT 4: 4D TESSERACT HYPERCUBE PROJECTION (36.0s - 48.0s)
        # =============================================================
        self.move_camera(phi=65 * DEGREES, theta=35 * DEGREES, zoom=1.15, run_time=1.6)

        tesseract_title = Text("4D HYPERCUBE PROJECTION", font_size=26, weight=BOLD, color=COLOR_YELLOW)
        tesseract_title.to_corner(UL, buff=0.5)
        self.add_fixed_in_frame_mobjects(tesseract_title)
        self.play(Write(tesseract_title), run_time=0.8)

        # Generate 16 4D Vertices (+-1, +-1, +-1, +-1)
        raw_4d_vertices = []
        for x in [-1, 1]:
            for y in [-1, 1]:
                for z in [-1, 1]:
                    for w in [-1, 1]:
                        raw_4d_vertices.append(np.array([x, y, z, w], dtype=float))

        # Find the 32 edges (vertices differing by 1 coordinate)
        edges_idx = []
        for i in range(len(raw_4d_vertices)):
            for j in range(i + 1, len(raw_4d_vertices)):
                if np.sum(np.abs(raw_4d_vertices[i] - raw_4d_vertices[j])) == 2:
                    edges_idx.append((i, j))

        # 4D Rotation matrix in X-W and Y-Z planes
        angle_tracker = ValueTracker(0)

        def project_4d_to_3d():
            alpha = angle_tracker.get_value()
            c, s = np.cos(alpha), np.sin(alpha)
            # 4D Rotation Matrix R_xw(alpha) * R_yz(alpha * 0.7)
            pts_3d = []
            for v4 in raw_4d_vertices:
                # Rotate in X-W plane
                x_rot = v4[0] * c - v4[3] * s
                w_rot = v4[0] * s + v4[3] * c
                # Rotate in Y-Z plane
                beta = alpha * 0.65
                cb, sb = np.cos(beta), np.sin(beta)
                y_rot = v4[1] * cb - v4[2] * sb
                z_rot = v4[1] * sb + v4[2] * cb

                # Perspective projection from 4D to 3D
                distance = 2.4
                proj_factor = 1.0 / (distance - w_rot * 0.45)
                pts_3d.append(np.array([x_rot * proj_factor * 2.0, y_rot * proj_factor * 2.0, z_rot * proj_factor * 2.0]))
            return pts_3d

        # Create 3D nodes & connecting lines
        current_pts = project_4d_to_3d()
        nodes_3d = VGroup(*[Dot3D(p, radius=0.08, color=COLOR_CYAN) for p in current_pts])
        lines_3d = VGroup(*[
            Line(current_pts[i], current_pts[j], stroke_width=2.5, color=COLOR_BLUE)
            for i, j in edges_idx
        ])

        tesseract_group = VGroup(nodes_3d, lines_3d)
        self.play(Create(tesseract_group), run_time=1.8)

        # Dynamic updater for the 4D rotation
        def update_tesseract(mob):
            pts = project_4d_to_3d()
            for idx, pt in enumerate(pts):
                mob[0][idx].move_to(pt)
                # Outer vs inner node coloring
                if pt[2] > 0:
                    mob[0][idx].set_color(COLOR_CYAN)
                else:
                    mob[0][idx].set_color(COLOR_MAGENTA)

            for e_idx, (i, j) in enumerate(edges_idx):
                mob[1][e_idx].set_points_by_ends(pts[i], pts[j])

        tesseract_group.add_updater(update_tesseract)

        # Rotate 4D Tesseract smoothly
        self.play(
            angle_tracker.animate.set_value(TAU * 1.25),
            run_time=4.5,
            rate_func=linear,
        )

        tesseract_group.remove_updater(update_tesseract)
        self.remove_fixed_in_frame_mobjects(tesseract_title)
        self.play(FadeOut(tesseract_title), run_time=0.4)

        # =============================================================
        # ACT 5: THE SINGULARITY COLLAPSE & SHOCKWAVE FINALE (48.0s - 60.0s)
        # =============================================================
        # Zoom camera into singularity
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, zoom=1.0, run_time=1.2)

        # Collapse tesseract into a blinding central singularity point
        singularity = VGroup(
            Dot(ORIGIN, color=COLOR_WHITE, radius=0.18),
            Circle(radius=0.4, color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_WHITE, fill_opacity=0.3),
        )

        self.play(
            ReplacementTransform(tesseract_group, singularity),
            run_time=1.2,
            rate_func=rush_into,
        )
        self.wait(0.3)

        # --- THE COSMIC SHOCKWAVE BURST ---
        # Concentric shockwave rings
        shock_ring_1 = Circle(radius=0.1, color=COLOR_CYAN, stroke_width=8)
        shock_ring_2 = Circle(radius=0.1, color=COLOR_MAGENTA, stroke_width=6)
        shock_ring_3 = Circle(radius=0.1, color=COLOR_YELLOW, stroke_width=4)

        # Radial particle burst (48 particles)
        np.random.seed(1337)
        num_particles = 48
        particle_group = VGroup()
        target_positions = []
        for _ in range(num_particles):
            angle = np.random.uniform(0, TAU)
            dist = np.random.uniform(3.0, 7.5)
            c = np.random.choice([COLOR_CYAN, COLOR_MAGENTA, COLOR_YELLOW, COLOR_WHITE])
            p = Dot(ORIGIN, radius=np.random.uniform(0.04, 0.08), color=c)
            particle_group.add(p)
            target_positions.append(np.array([dist * np.cos(angle), dist * np.sin(angle), 0]))

        self.add(shock_ring_1, shock_ring_2, shock_ring_3, particle_group)

        # Explode shockwaves & particles
        particle_anims = [
            particle_group[i].animate(rate_func=rush_from).move_to(target_positions[i]).set_opacity(0)
            for i in range(num_particles)
        ]

        self.play(
            FadeOut(singularity, scale=0.1),
            shock_ring_1.animate(rate_func=rush_from).scale(45).set_stroke(width=0, opacity=0),
            shock_ring_2.animate(rate_func=rush_from).scale(35).set_stroke(width=0, opacity=0),
            shock_ring_3.animate(rate_func=rush_from).scale(25).set_stroke(width=0, opacity=0),
            *particle_anims,
            run_time=1.4,
        )

        self.remove(shock_ring_1, shock_ring_2, shock_ring_3, particle_group)

        # Assemble Final Hero Brand & Signature
        hexagon = RegularPolygon(n=6, radius=1.6, color=COLOR_CYAN, stroke_width=3)
        inner_tri_1 = Triangle(color=COLOR_MAGENTA, stroke_width=2).scale(1.2)
        inner_tri_2 = Triangle(color=COLOR_YELLOW, stroke_width=2).scale(1.2).rotate(PI)

        badge = VGroup(hexagon, inner_tri_1, inner_tri_2)

        final_title = Text("INFINITE POSSIBILITIES", font_size=42, weight=HEAVY, color=COLOR_WHITE)
        final_title.set_stroke(color=COLOR_CYAN, width=1)
        final_title.next_to(badge, DOWN, buff=0.45)

        tech_specs = Text(
            "Rendered in 1440p 60fps • Powered by NVIDIA RTX 2050 • Manim Community",
            font_size=15,
            color="#7a889b",
        )
        tech_specs.next_to(final_title, DOWN, buff=0.25)

        self.play(
            DrawBorderThenFill(badge, run_time=1.4),
            Write(final_title, run_time=1.2),
            FadeIn(tech_specs, shift=UP * 0.15, run_time=1.0),
        )

        self.play(
            badge.animate.rotate(PI / 3),
            Flash(badge.get_center(), color=COLOR_CYAN, flash_radius=2.2, num_lines=24),
            run_time=1.6,
        )

        self.wait(2.0)

        # Elegant fade to black
        self.play(
            FadeOut(badge),
            FadeOut(final_title),
            FadeOut(tech_specs),
            FadeOut(bg_grid),
            run_time=1.5,
        )
        self.wait(0.5)
