from expyriment import design, control, stimuli, misc
from expyriment.misc.constants import K_SPACE

FPS = 60
MS_PER_FRAME = 1000 / FPS


def frames_to_ms(n_frames):
    return round(n_frames * MS_PER_FRAME)


def present_for(exp, stims, n_frames):
    """Show stimuli for n_frames."""
    if n_frames <= 0:
        return

    t0 = exp.clock.time
    exp.screen.clear()

    for stim in stims:
        stim.present(clear=False, update=False)

    exp.screen.update()

    dt = exp.clock.time - t0
    remaining = frames_to_ms(n_frames) - dt
    if remaining > 0:
        exp.clock.wait(remaining)

def add_tags(circle, colour):
    tag = stimuli.Circle(
        radius=max(8, circle.radius // 3),
        colour=colour,
        position=(0, 0),
        anti_aliasing=10
    )
    tag.plot(circle)
    circle.preload()

def make_circles(radius=35, tagged=False):
    step = radius * 3


    c1 = stimuli.Circle(radius=radius, position=(-step, 0),
                        colour=misc.constants.C_BLACK, anti_aliasing=10)
    c2 = stimuli.Circle(radius=radius, position=(0, 0),
                        colour=misc.constants.C_BLACK, anti_aliasing=10)
    c3 = stimuli.Circle(radius=radius, position=(step, 0),
                        colour=misc.constants.C_BLACK, anti_aliasing=10)


    c4 = stimuli.Circle(radius=radius, position=(0, 0),
                        colour=misc.constants.C_BLACK, anti_aliasing=10)
    c5 = stimuli.Circle(radius=radius, position=(step, 0),
                        colour=misc.constants.C_BLACK, anti_aliasing=10)
    c6 = stimuli.Circle(radius=radius, position=(2 * step, 0),
                        colour=misc.constants.C_BLACK, anti_aliasing=10)

    if tagged:
        add_tags(c1, misc.constants.C_YELLOW)
        add_tags(c2, misc.constants.C_RED)
        add_tags(c3, misc.constants.C_BLUE)

        add_tags(c4, misc.constants.C_RED)
        add_tags(c5, misc.constants.C_BLUE)
        add_tags(c6, misc.constants.C_YELLOW)
    else:
        for c in (c1, c2, c3, c4, c5, c6):
            c.preload()

    return [c1, c2, c3], [c4, c5, c6]


def run_trial(exp, radius=35, isi_frames=2, tagged=False, demo_frames=300):
    """
    Run one Ternus demo for demo_frames total frames.
    SPACE skips to the next demo.
    """
    frame1, frame2 = make_circles(radius=radius, tagged=tagged)

    stim_frames = 12
    cycle_frames = stim_frames + isi_frames + stim_frames + isi_frames
    n_cycles = max(1, demo_frames // max(1, cycle_frames))

    for _ in range(n_cycles):
        present_for(exp, frame1, stim_frames)

        if isi_frames > 0:
            exp.screen.clear()
            exp.screen.update()
            exp.clock.wait(frames_to_ms(isi_frames))

        present_for(exp, frame2, stim_frames)

        if isi_frames > 0:
            exp.screen.clear()
            exp.screen.update()
            exp.clock.wait(frames_to_ms(isi_frames))

        if exp.keyboard.check(K_SPACE):
            break


exp = design.Experiment(
    name="Ternus Illusion",
    background_colour=misc.constants.C_WHITE
)

control.set_develop_mode(True)
control.initialize(exp)

control.start()

run_trial(exp, radius=35, isi_frames=1, tagged=False, demo_frames=300)

run_trial(exp, radius=35, isi_frames=5, tagged=False, demo_frames=300)

run_trial(exp, radius=35, isi_frames=5, tagged=True, demo_frames=300)

control.end()