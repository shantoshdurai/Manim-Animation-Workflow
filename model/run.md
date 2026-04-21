# Running Manim Scenes

## Basic command
```
manim -pql scene_01_basics.py HelloWorld
```

## Flags
- `-p` — preview after render
- `-ql` — low quality (fast, 480p)
- `-qm` — medium quality (720p)
- `-qh` — high quality (1080p)
- `-qk` — 4K quality

## Render all scenes in a file
```
manim -pql scene_01_basics.py
```

## Available scenes

### scene_01_basics.py
- `HelloWorld` — animated text intro
- `ShapesDemo` — circle, square, triangle
- `TransformDemo` — shape morphing

### scene_02_math.py
- `EquationScene` — Euler's identity & Pythagorean theorem
- `GraphScene` — sin/cos plot on axes
- `NumberLineScene` — animated dot on number line

### scene_03_animation.py
- `MovementDemo` — dot movement paths
- `ColorAndOpacity` — color/fill animations
- `Updaters` — live position label
- `CameraZoom` — MovingCameraScene zoom
