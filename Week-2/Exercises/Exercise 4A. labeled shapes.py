import math
from expyriment import design, control, stimuli

control.set_develop_mode()

exp = design.Experiment(name="Labeled Shapes")
control.initialize(exp)


def regular_polygon_vertices(n_sides, radius, start_angle=0):
    vertices = []
    for i in range(n_sides):
        angle = start_angle + 2 * math.pi * i / n_sides
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        vertices.append((x, y))
    return vertices


control.start(subject_id=1)

left_pos = (-100, 0)
right_pos = (100, 0)

triangle_radius = 50
hexagon_radius = 30

triangle = stimuli.Shape(
    vertex_list=regular_polygon_vertices(3, triangle_radius),
    colour=(160, 32, 240),
    position=left_pos
)

hexagon = stimuli.Shape(
    vertex_list=regular_polygon_vertices(6, hexagon_radius),
    colour=(255, 255, 0),
    position=right_pos
)

line_length = 50

triangle_line = stimuli.Line(
    start_point=(left_pos[0], left_pos[1] + 35),
    end_point=(left_pos[0], left_pos[1] + 35 + line_length),
    line_width=3,
    colour=(255, 255, 255)
)

hexagon_line = stimuli.Line(
    start_point=(right_pos[0], right_pos[1] + 35),
    end_point=(right_pos[0], right_pos[1] + 35 + line_length),
    line_width=3,
    colour=(255, 255, 255)
)

triangle_label = stimuli.TextLine(
    text="triangle",
    text_colour=(255, 255, 255),
    position=(left_pos[0], left_pos[1] + 35 + line_length + 20)
)

hexagon_label = stimuli.TextLine(
    text="hexagon",
    text_colour=(255, 255, 255),
    position=(right_pos[0], right_pos[1] + 35 + line_length + 20)
)

triangle.present(clear=True, update=False)
hexagon.present(clear=False, update=False)
triangle_line.present(clear=False, update=False)
hexagon_line.present(clear=False, update=False)
triangle_label.present(clear=False, update=False)
hexagon_label.present(clear=False, update=True)

exp.keyboard.wait()
control.end()