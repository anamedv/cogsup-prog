from expyriment import design, control, stimuli

control.set_develop_mode()

exp = design.Experiment(name="Launching Function")
control.initialize(exp)

square_size = (50, 50)
square_length = 50


def show_event(exp, temporal_gap=0, spatial_gap=0, speed_multiplier=1,
               start_left_x=-400, start_right_x=0, base_step=10, delay_ms=20):
    """Display one horizontal launching-like event."""

    left_square = stimuli.Rectangle(
        size=square_size,
        colour=(255, 0, 0),
        position=(start_left_x, 0)
    )

    right_square = stimuli.Rectangle(
        size=square_size,
        colour=(0, 255, 0),
        position=(start_right_x, 0)
    )

    
    left_square.present(clear=True, update=False)
    right_square.present(clear=False, update=True)
    exp.clock.wait(1000)

    
    while right_square.position[0] - left_square.position[0] > square_length + spatial_gap:
        left_square.move((base_step, 0))
        left_square.present(clear=True, update=False)
        right_square.present(clear=False, update=True)
        exp.clock.wait(delay_ms)

    
    exp.clock.wait(temporal_gap)

    
    right_step = int(base_step * speed_multiplier)
    target_x = 400
    while right_square.position[0] < target_x:
        right_square.move((right_step, 0))
        left_square.present(clear=True, update=False)
        right_square.present(clear=False, update=True)
        exp.clock.wait(delay_ms)

    
    left_square.present(clear=True, update=False)
    right_square.present(clear=False, update=True)
    exp.clock.wait(1000)


control.start(subject_id=1)

# 1. Standard Michottean launching
show_event(exp, temporal_gap=0, spatial_gap=0, speed_multiplier=1)

# 2. Launching with temporal gap
show_event(exp, temporal_gap=500, spatial_gap=0, speed_multiplier=1)

# 3. Launching with spatial gap
show_event(exp, temporal_gap=0, spatial_gap=20, speed_multiplier=1)

# 4. Triggering
show_event(exp, temporal_gap=0, spatial_gap=0, speed_multiplier=3)

exp.keyboard.wait()
control.end()