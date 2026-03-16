from expyriment import design, control, stimuli

exp = design.Experiment(name="timing puzzle")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
text = stimuli.TextLine("Fixation removed")

fixation.preload()
text.preload()

control.start()

t0 = exp.clock.time
fixation.present()
dt = exp.clock.time - t0
exp.clock.wait(1000 - dt)

t0 = exp.clock.time
text.present()
dt = exp.clock.time - t0
exp.clock.wait(1000 - dt)

duration = 1.0
units = "second" if duration == 1.0 else "seconds"
duration_text = f"Fixation was present on the screen for {duration} {units}"

text2 = stimuli.TextLine(duration_text)
text2.present()
exp.keyboard.wait(2000)

control.end()