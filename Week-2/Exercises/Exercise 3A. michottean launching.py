from expyriment import design, control, stimuli

exp = design.Experiment(name="Michottean launching")
control.set_develop_mode()
control.initialize(exp)

square_length = 50
square_size = (square_length, square_length)
displacement_x = 400
step_size = 10

left_square = stimuli.Rectangle(
    size=square_size,
    colour=(0, 0, 255),
    position=(-200, 0)
)

right_square = stimuli.Rectangle(
    size=square_size,
    colour=(255, 0, 0),
    position=(0, 0)
)

control.start(subject_id=1)

left_square.present(clear=True, update=False)
right_square.present(clear=False, update=True)

exp.clock.wait(500)

while right_square.position[0] - left_square.position[0] > square_length:
    left_square.move((step_size, 0))

    left_square.present(clear=True, update=False)
    right_square.present(clear=False, update=True)

    exp.clock.wait(30)

while right_square.position[0] < displacement_x:
    right_square.move((step_size, 0))

    left_square.present(clear=True, update=False)
    right_square.present(clear=False, update=True)

    exp.clock.wait(30)

exp.keyboard.wait()
control.end()