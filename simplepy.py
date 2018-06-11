from pymol import cmd

iternum = 0

def pubimage(*argumenthere, **kwd):
	'''Takes an image with the specified properties. The properties should be entered in the following order:
	
	ray_trace_mode, antialias, ray number 1, ray number 2, bg_color
			
	
	If not specified, then the properties default to
			ray_trace_mode (int 1-3) 	-->	 	3
			antialias (int 0-2)			--> 	2
			ray num1, raynum2 (int) 	--> 	ray 1200, 1200
			bg_color (string) 			--> 	white
	'''
	
	# The following is for debugging:
			# argumenthere[0] (int 1-3) 				-->	 	ray_trace_mode (int)
			# argumenthere[1] (int 0-2)					--> 	antialias (int)
			# argumenthere[2], argumenthere[3] (int) 	--> 	ray num1, num2 (int)
			# argumenthere[4] (string) 					--> 	bg_color (string)

	global iternum
	
	#Setting ray_trace_mode
	try:
		cmd.set('ray_trace_mode', value=int(argumenthere[0]), selection='', state=0,updates=1, log=0, quiet=1)
	except IndexError:
		cmd.set('ray_trace_mode', 3)
	
	#Setting antialias
	try:
		cmd.set('antialias', int(argumenthere[1]), selection='', state=0,updates=1, log=0, quiet=1)
	except IndexError:
		cmd.set('antialias', 2)
	
	#Setting bg_color
	try:
		cmd.bg_color(argumenthere[4])
	except IndexError:
		cmd.bg_color('white')
	
	#Ray the image
	try:
		cmd.ray(width=int(argumenthere[2]), height=int(argumenthere[3]), antialias=-1, angle=0.0, shift=0.0, renderer=-1, quiet=1, async=0)
	except IndexError:
		cmd.ray(width=1200, height=1200)
	
	#Save the Image
	try:
		cmd.png('image' + iternum + '.png')
	except IndexError:
		cmd.png('image' + iternum + '.png')

	iternum += 1

def pubimage_tmblr(*argumenthere, **kwd):
	'''Takes an image with the specified properties. The properties should be entered in the following order:
	
	ray_trace_mode, antialias, ray number 1, ray number 2, bg_color
			
	
	If not specified, then the properties default to
			ray_trace_mode (int 1-3) 	-->	 	3
			antialias (int 0-2)			--> 	2
			ray num1, raynum2 (int) 	--> 	ray 1200, 1200
			bg_color (string) 			--> 	white
	'''
	
	# The following is for debugging:
			# argumenthere[0] (int 1-3) 				-->	 	ray_trace_mode (int)
			# argumenthere[1] (int 0-2)					--> 	antialias (int)
			# argumenthere[2], argumenthere[3] (int)	--> 	ray num1, num2 (int)
			# argumenthere[4] (string) 					--> 	bg_color (string)

	global iternum
	
	#Setting ray_trace_mode
	try:
		cmd.set('ray_trace_mode', value=int(argumenthere[0]), selection='', state=0,updates=1, log=0, quiet=1)
	except IndexError:
		cmd.set('ray_trace_mode', 3)
	
	#Setting antialias
	try:
		cmd.set('antialias', int(argumenthere[1]), selection='', state=0,updates=1, log=0, quiet=1)
	except IndexError:
		cmd.set('antialias', 2)
		
	#Setting bg_color
	try:
		cmd.bg_color(argumenthere[4])
	except IndexError:
		cmd.bg_color('white')

	#CENTER IMAGE TAKING AND ROTATION
	#Ray the image
	try:
		cmd.ray(width=int(argumenthere[2]), height=int(argumenthere[3]), antialias=-1, angle=0.0, shift=0.0, renderer=-1, quiet=1, async=0)
	except IndexError:
		cmd.ray(width=1200, height=1200)
	
	#Save the Image
	try:
		cmd.png('molecule' + iternum + 'center.png')
	except IndexError:
		cmd.png('molecule' + iternum + 'center.png')
	
	cmd.turn('x', 90.0)
	
	#TOP-DOWN IMAGE TAKING AND ROTATION
	#Ray the image
	try:
		cmd.ray(width=int(argumenthere[2]), height=int(argumenthere[3]), antialias=-1, angle=0.0, shift=0.0, renderer=-1, quiet=1, async=0)
	except IndexError:
		cmd.ray(width=1200, height=1200)

	#Save the Image
	try:
		cmd.png('molecule' + iternum + 'topdown.png')
	except IndexError:
		cmd.png('molecule' + iternum + 'topdown.png')

	cmd.turn('x', -180.0)
	
	#BOTTOM-UP IMAGE TAKING AND ROTATION
	#Ray the image
	try:
		cmd.ray(width=int(argumenthere[2]), height=int(argumenthere[3]), antialias=-1, angle=0.0, shift=0.0, renderer=-1, quiet=1, async=0)
	except IndexError:
		cmd.ray(width=1200, height=1200)

	#Save the Image
	try:
		cmd.png('molecule' + iternum + 'bottomup.png')
	except IndexError:
		cmd.png('molecule' + iternum + 'bottomup.png')

	cmd.turn('x', 90.0)
	cmd.turn('y', 90.0)
	
	#LEFT IMAGE TAKING AND ROTATION
	#Ray the image
	try:
		cmd.ray(width=int(argumenthere[2]), height=int(argumenthere[3]), antialias=-1, angle=0.0, shift=0.0, renderer=-1, quiet=1, async=0)
	except IndexError:
		cmd.ray(width=1200, height=1200)

	#Save the Image
	try:
		cmd.png('molecule' + iternum + 'left.png')
	except IndexError:
		cmd.png('molecule' + iternum + 'left.png')
	
	cmd.turn('y', -180.0)
	
	#RIGHT IMAGE TAKING AND ROTATION
	#Ray the image
	try:
		cmd.ray(width=int(argumenthere[2]), height=int(argumenthere[3]), antialias=-1, angle=0.0, shift=0.0, renderer=-1, quiet=1, async=0)
	except IndexError:
		cmd.ray(width=1200, height=1200)

	#Save the Image
	try:
		cmd.png('molecule' + iternum + 'right.png')
	except IndexError:
		cmd.png('molecule' + iternum + 'right.png')

	cmd.turn('y', 90.0)
	iternum += 1


#Associate the functions with commands in the pymol command line
cmd.extend('pubimage', pubimage)
cmd.extend('pubimage_tmblr', pubimage_tmblr)