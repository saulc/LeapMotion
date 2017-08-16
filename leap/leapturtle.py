#import Tkinter as tkinter

import sys
sys.path.insert(0, "./lib")
import Leap
import turtle

class Tl(Leap.Listener):
	x = 0
	y = 0
	z = 0
	xc = 10
	yc =  100
	zc = 40
	

					
	
	def on_init(self, controller):
		print "Initialized"
	
	def on_connect(self, controller):
		print "Connected"
		
	def on_disconnect(self, controller):
		# Note: not dispatched when running in a debugger.
		print "Disconnected"
	
	def on_exit(self, controller):
		print "Exited"
	
	def on_frame(self, controller):
		# Get the most recent frame and report some basic information
		frame = controller.frame()
		for h in frame.hands:
			handType = "Left hand" if h.is_left else "Right hand"
			print "  %s, id %d, position: %s" % (handType, h.id, h.palm_position)
			self.x = h.palm_position.x
			self.y = h.palm_position.y
			self.z = h.palm_position.z
			self.scale()
			#self.update()

	def scale(self):
		y = self.y
		y = y * 2
		y = y - 400
		self. y = y
     
def update(l):
	if l.x == 0 and l.y == 0: 	
		turtle.circle(-20)
		print "No hands"
	else: turtle.setpos(l.x, l.y)
			# if l.x > l.xc:  
# 				turtle.forward(15)	#right
# 				print "Going foward"
# 			else: turtle.backward(15)
# 			if l.y > l.yc: turtle.left(20)
# 			else: turtle.right(20)
				
def main():
	# Create a sample listener and controller
	listener = Tl()
	controller = Leap.Controller()
	
	
	# Have the sample listener receive events from the controller
	controller.add_listener(listener)

	# Keep this process running until Enter is pressed
	print "Press Enter to quit..."
	try:
		while True:
			update(listener)
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		# Remove the sample listener when done
		controller.remove_listener(listener)


if __name__ == "__main__":
    main()

