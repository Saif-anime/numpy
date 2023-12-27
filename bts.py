from sketchpy import canvas as gfg
img = gfg.sketch_from_image("bts.webp")
# Here the threshold value is the parameter that is used based on the user's choice
img.draw(threshold=150)
