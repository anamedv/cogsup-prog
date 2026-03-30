from expyriment import design, control, stimuli

control.set_develop_mode()

exp = design.Experiment(name="Triggering")
control.initialize(exp)

square_size = (50, 50)
square_length = 50
left_step = 10
right_step = 30  # 3x faster

left_square = stimuli.Rectangle(
    size=square_size,
    colour=(255, 0, 0),
    position=(-400, 0)
)

right_square = stimuli.Rectangle(
    size=square_size,
    colour=(0, 255, 0),
    position=(0, 0)
)

control.start(subject_id=1)

left_square.present(clear=True, update=False)
right_square.present(clear=False, update=True)
exp.clock.wait(1000)

while right_square.position[0] - left_square.position[0] > square_length:
    left_square.move((left_step, 0))
    left_square.present(clear=True, update=False)
    right_square.present(clear=False, update=True)
    exp.clock.wait(20)

target_x = 400
while right_square.position[0] < target_x:
    right_square.move((right_step, 0))
    left_square.present(clear=True, update=False)
    right_square.present(clear=False, update=True)
    exp.clock.wait(20)

left_square.present(clear=True, update=False)
right_square.present(clear=False, update=True)
exp.clock.wait(1000)

exp.keyboard.wait()
control.end()