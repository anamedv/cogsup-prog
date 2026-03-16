from expyriment import design, control, stimuli
import random


def load(stims):
    for stim in stims:
        stim.preload()


def timed_draw(stims):
    t0 = exp.clock.time

    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()

    return exp.clock.time - t0


def present_for(stims, t=1000):
    dt = timed_draw(stims)
    remaining = t - dt

    if remaining > 0:
        exp.clock.wait(remaining)


""" Test functions """
exp = design.Experiment(name="Drawing Functions")

control.set_develop_mode(True)
control.initialize(exp)
control.start()

fixation = stimuli.FixCross()
load([fixation])

n = 20
positions = [(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(n)]
squares = [stimuli.Rectangle(size=(50, 50), position=pos) for pos in positions]
load(squares)

durations = []

t0 = exp.clock.time
for square in squares:
    if not square.is_preloaded:
        print("Preloading function not implemented correctly.")

    stims = [fixation, square]
    present_for(stims, 500)

    t1 = exp.clock.time
    durations.append(t1 - t0)
    t0 = t1

if all(abs(d - 500) <= 1 for d in durations):
    print("Well done!")
else:
    print(f"Timing off. Measured durations were: {durations}")

control.end()