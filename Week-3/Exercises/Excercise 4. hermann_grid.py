import expyriment
from expyriment import control, stimuli, misc


def draw_hermann_grid(exp,
                      square_size=70,
                      gap=20,
                      rows=5,
                      cols=5,
                      square_colour=misc.constants.C_BLACK):

    
    exp.screen.clear()

    
    grid_width = cols * square_size + (cols - 1) * gap
    grid_height = rows * square_size + (rows - 1) * gap

    
    start_x = -grid_width // 2 + square_size // 2
    start_y = grid_height // 2 - square_size // 2

    
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * (square_size + gap)
            y = start_y - row * (square_size + gap)

            square = stimuli.Rectangle(
                size=(square_size, square_size),
                position=(x, y),
                colour=square_colour
            )

            last_square = (row == rows - 1 and col == cols - 1)
            square.present(clear=False, update=last_square)


exp = expyriment.design.Experiment(
    name="Hermann Grid",
    background_colour=misc.constants.C_WHITE
)

control.set_develop_mode(True)
control.initialize(exp)
control.start()

draw_hermann_grid(
    exp,
    square_size=70,
    gap=20,
    rows=5,
    cols=5,
    square_colour=misc.constants.C_BLACK
)

exp.keyboard.wait()
control.end()