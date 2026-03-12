import expyriment
from expyriment import control, stimuli, misc


def draw_kanizsa_rectangle(exp, aspect_ratio=1.5, rect_scale=0.30, circle_scale=0.05):
    width, height = exp.screen.size

    
    rect_width = int(width * rect_scale)
    rect_height = int(rect_width / aspect_ratio)

    
    circle_radius = int(width * circle_scale)
    mask_size = circle_radius

    half_w = rect_width // 2
    half_h = rect_height // 2

    
    positions = [
        (-half_w,  half_h),   
        ( half_w,  half_h),   
        (-half_w, -half_h),   
        ( half_w, -half_h)    
    ]

    
    circle_colours = [
        misc.constants.C_BLACK,
        misc.constants.C_BLACK,
        misc.constants.C_WHITE,
        misc.constants.C_WHITE
    ]

    mask_offsets = [
        ( mask_size // 2, -mask_size // 2),  
        (-mask_size // 2, -mask_size // 2),  
        ( mask_size // 2,  mask_size // 2),  
        (-mask_size // 2,  mask_size // 2)   
    ]

    circles = []
    masks = []

    for pos, colour, offset in zip(positions, circle_colours, mask_offsets):
        circle = stimuli.Circle(
            radius=circle_radius,
            position=pos,
            colour=colour,
            anti_aliasing=10
        )
        circles.append(circle)

        mask = stimuli.Rectangle(
            size=(mask_size, mask_size),
            position=(pos[0] + offset[0], pos[1] + offset[1]),
            colour=misc.constants.C_GREY
        )
        masks.append(mask)

    exp.screen.clear()

    for circle in circles:
        circle.present(clear=False, update=False)

    for i, mask in enumerate(masks):
        mask.present(clear=False, update=(i == len(masks) - 1))


exp = expyriment.design.Experiment(
    name="Kanizsa Rectangle",
    background_colour=misc.constants.C_GREY
)

control.set_develop_mode(True)
control.initialize(exp)
control.start()

draw_kanizsa_rectangle(exp, aspect_ratio=1.5, rect_scale=0.30, circle_scale=0.05)

exp.keyboard.wait()
control.end()
