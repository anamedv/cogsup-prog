from expyriment import design, control, stimuli

exp = design.Experiment(name="Square Fixation")

control.set_develop_mode(True)
control.initialize(exp)

fixation = stimuli.FixCross()
square = stimuli.Rectangle(size=(100, 100), line_width=5)

control.start()

fixation.present(clear=True, update=True)

exp.clock.wait(500)

fixation.present(clear=True, update=False)
square.present(clear=False, update=True)

exp.keyboard.wait()

control.end()