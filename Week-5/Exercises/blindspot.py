from expyriment import design, control, stimuli
from expyriment.misc.constants import (
    C_WHITE, C_BLACK,
    K_LEFT, K_RIGHT, K_UP, K_DOWN,
    K_1, K_2, K_SPACE
)

STEP_POS = 10
STEP_RADIUS = 5
START_RADIUS = 75
MIN_RADIUS = 5

exp = design.Experiment(
    name="Blindspot",
    background_colour=C_WHITE,
    foreground_colour=C_BLACK
)

control.set_develop_mode()

exp.add_data_variable_names([
    "eye",
    "event_type",
    "last_key",
    "radius",
    "x_coord",
    "y_coord"
])

control.initialize(exp)

def make_circle(radius, pos=(0, 0)):
    circle = stimuli.Circle(radius=radius, position=pos, anti_aliasing=10)
    circle.preload()
    return circle


def make_fixation(side):
    """
    side:
        "left"  -> left eye
        "right" -> right eye
    """

    if side == "left":
        fix_pos = (300, 0)
    elif side == "right":
        fix_pos = (-300, 0)
    else:
        raise ValueError("side must be 'left' or 'right'")

    fixation = stimuli.FixCross(
        size=(150, 150),
        line_width=10,
        position=fix_pos
    )
    fixation.preload()
    return fixation


def get_instruction_text(side):
    if side == "left":
        cover_text = "Cover your RIGHT eye."
        fixation_text = "Fixate with your LEFT eye on the cross on the right."
    else:
        cover_text = "Cover your LEFT eye."
        fixation_text = "Fixate with your RIGHT eye on the cross on the left."

    return (
        f"{cover_text}\n\n"
        f"{fixation_text}\n\n"
        "Do not move your gaze from the cross.\n"
        "Arrow keys: move the circle\n"
        "1: decrease size\n"
        "2: increase size\n\n"
        "When the circle disappears in your blind spot and you are done,\n"
        "press SPACE."
    )


def key_to_label(key):
    mapping = {
        K_LEFT: "left",
        K_RIGHT: "right",
        K_UP: "up",
        K_DOWN: "down",
        K_1: "1",
        K_2: "2",
        K_SPACE: "space"
    }
    return mapping.get(key, str(key))


def draw_trial_screen(fixation, radius, pos):
    circle = make_circle(radius, pos)
    fixation.present(clear=True, update=False)
    circle.present(clear=False, update=True)

def run_trial(side):

    instructions = stimuli.TextScreen(
        heading=f"Blind spot: {side} eye",
        text=get_instruction_text(side)
    )
    instructions.present()
    exp.keyboard.wait(keys=[K_SPACE])

    fixation = make_fixation(side)

    if side == "left":
        x, y = -100, 0
    else:
        x, y = 100, 0

    radius = START_RADIUS

    draw_trial_screen(fixation, radius, (x, y))

    while True:
        key, rt = exp.keyboard.wait(
            keys=[K_LEFT, K_RIGHT, K_UP, K_DOWN, K_1, K_2, K_SPACE]
        )

        if key == K_LEFT:
            x -= STEP_POS
        elif key == K_RIGHT:
            x += STEP_POS
        elif key == K_UP:
            y += STEP_POS
        elif key == K_DOWN:
            y -= STEP_POS
        elif key == K_1:
            radius = max(MIN_RADIUS, radius - STEP_RADIUS)
        elif key == K_2:
            radius += STEP_RADIUS
        elif key == K_SPACE:
            # Exercise 2A
            exp.data.add([
                side,
                "final",
                "space",
                radius,
                x,
                y
            ])
            break

        # Exercise 2B
        exp.data.add([
            side,
            "keypress",
            key_to_label(key),
            radius,
            x,
            y
        ])

        draw_trial_screen(fixation, radius, (x, y))


control.start()

run_trial("left")
run_trial("right")

control.end()