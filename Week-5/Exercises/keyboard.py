from expyriment import design, control, stimuli, io
from expyriment.misc.constants import K_DOWN, K_UP, K_LEFT, K_RIGHT

control.set_develop_mode()

exp = design.Experiment(name="Keyboard Test")
control.initialize(exp)

keyboard = io.Keyboard()

cue = stimuli.TextLine("Press arrow key")
cue.present()

key, rt = keyboard.wait(keys=[K_DOWN, K_UP, K_LEFT, K_RIGHT])

key_names = {
    K_UP: "UP",
    K_DOWN: "DOWN",
    K_LEFT: "LEFT",
    K_RIGHT: "RIGHT"
}

pressed_key = key_names.get(key, str(key))

feedback = stimuli.TextScreen(
    "Result",
    f"You pressed {pressed_key}\nRT = {rt} ms"
)
feedback.present()

exp.clock.wait(3000)

control.end()