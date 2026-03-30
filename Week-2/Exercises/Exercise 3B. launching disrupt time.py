from expyriment import design, control, stimuli

control.set_develop_mode()

exp = design.Experiment(name="Launching Disrupt Time")
control.initialize(exp)

square_size = (50, 50)
square_length = 50
step_size = 10

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
    left_square.move((step_size, 0))
    left_square.present(clear=True, update=False)
    right_square.present(clear=False, update=True)
    exp.clock.wait(20)

exp.clock.wait(100)   # around this delay, causality still feels intact to me
# I tried several delays (2000, 500, 200, 100, 80, 50 ms).


target_x = 400
while right_square.position[0] < target_x:
    right_square.move((step_size, 0))
    left_square.present(clear=True, update=False)
    right_square.present(clear=False, update=True)
    exp.clock.wait(20)

left_square.present(clear=True, update=False)
right_square.present(clear=False, update=True)
exp.clock.wait(1000)

exp.keyboard.wait()
control.end()