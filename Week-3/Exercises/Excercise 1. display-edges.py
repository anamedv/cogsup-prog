import expyriment
from expyriment import stimuli, control

exp = expyriment.design.Experiment(name="Display Edges")

control.set_develop_mode(True) 
control.initialize(exp)

width, height = exp.screen.size

square_size = int(width * 0.05) 
half_sq = square_size // 2

top_left     = (-(width // 2) + half_sq,  (height // 2) - half_sq)
top_right    = ( (width // 2) - half_sq,  (height // 2) - half_sq)
bottom_left  = (-(width // 2) + half_sq, -(height // 2) + half_sq)
bottom_right = ( (width // 2) - half_sq, -(height // 2) + half_sq)

sq_tl = stimuli.Rectangle(size=(square_size, square_size), position=top_left, 
                          colour=(255, 0, 0), line_width=1)
sq_tr = stimuli.Rectangle(size=(square_size, square_size), position=top_right, 
                          colour=(255, 0, 0), line_width=1)
sq_bl = stimuli.Rectangle(size=(square_size, square_size), position=bottom_left, 
                          colour=(255, 0, 0), line_width=1)
sq_br = stimuli.Rectangle(size=(square_size, square_size), position=bottom_right, 
                          colour=(255, 0, 0), line_width=1)

control.start()

sq_tl.present(clear=False, update=False)
sq_tr.present(clear=False, update=False)
sq_bl.present(clear=False, update=False)
sq_br.present(clear=False, update=True)

exp.keyboard.wait()

control.end()