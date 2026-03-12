import expyriment
from expyriment import control, stimuli, misc

exp = expyriment.design.Experiment(
    name="Kanizsa Rectangle",
    background_colour=misc.constants.C_GREY
)

control.set_develop_mode(True)
control.initialize(exp)

width, height = exp.screen.size

square_side = int(width * 0.25)
circle_radius = int(width * 0.05)

offset = square_side // 2
mask_size = circle_radius

top_left = (-offset, offset)
top_right = (offset, offset)
bottom_left = (-offset, -offset)
bottom_right = (offset, -offset)

c_tl = stimuli.Circle(
    radius=circle_radius,
    position=top_left,
    colour=misc.constants.C_BLACK,
    anti_aliasing=10
)

c_tr = stimuli.Circle(
    radius=circle_radius,
    position=top_right,
    colour=misc.constants.C_BLACK,
    anti_aliasing=10
)

c_bl = stimuli.Circle(
    radius=circle_radius,
    position=bottom_left,
    colour=misc.constants.C_WHITE,
    anti_aliasing=10
)

c_br = stimuli.Circle(
    radius=circle_radius,
    position=bottom_right,
    colour=misc.constants.C_WHITE,
    anti_aliasing=10
)

m_tl = stimuli.Rectangle(
    size=(mask_size, mask_size),
    position=(top_left[0] + mask_size // 2, top_left[1] - mask_size // 2),
    colour=misc.constants.C_GREY
)

m_tr = stimuli.Rectangle(
    size=(mask_size, mask_size),
    position=(top_right[0] - mask_size // 2, top_right[1] - mask_size // 2),
    colour=misc.constants.C_GREY
)

m_bl = stimuli.Rectangle(
    size=(mask_size, mask_size),
    position=(bottom_left[0] + mask_size // 2, bottom_left[1] + mask_size // 2),
    colour=misc.constants.C_GREY
)

m_br = stimuli.Rectangle(
    size=(mask_size, mask_size),
    position=(bottom_right[0] - mask_size // 2, bottom_right[1] + mask_size // 2),
    colour=misc.constants.C_GREY
)

control.start()

exp.screen.clear()

c_tl.present(clear=False, update=False)
c_tr.present(clear=False, update=False)
c_bl.present(clear=False, update=False)
c_br.present(clear=False, update=False)

m_tl.present(clear=False, update=False)
m_tr.present(clear=False, update=False)
m_bl.present(clear=False, update=False)
m_br.present(clear=False, update=True)

exp.keyboard.wait()
control.end()