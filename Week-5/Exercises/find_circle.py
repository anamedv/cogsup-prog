from expyriment import design, control, stimuli, io
from expyriment.misc.constants import K_LEFT, K_RIGHT

control.set_develop_mode()

exp = design.Experiment(name="Find the Circle")
control.initialize(exp)

keyboard = io.Keyboard()

instruction = stimuli.TextScreen(
    "Instruction",
    "Find the circle.\nPress LEFT if the circle is on the left.\nPress RIGHT if the circle is on the right.\n\nPress left or right to start"
)
instruction.present()

keyboard.wait(keys=[K_LEFT, K_RIGHT])

circle_position = "left"

if circle_position == "left":
    circle_x = -150
    square_x = 150
    correct_key = K_LEFT
else:
    circle_x = 150
    square_x = -150
    correct_key = K_RIGHT

circle = stimuli.Circle(radius=40, colour=(255, 255, 255), position=(circle_x, 0))
square = stimuli.Rectangle(size=(80, 80), colour=(255, 255, 255), position=(square_x, 0))

blank = stimuli.BlankScreen()
circle.plot(blank)
square.plot(blank)

blank.present()

key, rt = keyboard.wait(keys=[K_LEFT, K_RIGHT])

if key == correct_key:
    feedback_text = f"Correct\nRT = {rt} ms"
else:
    feedback_text = f"False\nRT = {rt} ms"

feedback = stimuli.TextScreen("Feedback", feedback_text)
feedback.present()

exp.clock.wait(2000)

control.end()