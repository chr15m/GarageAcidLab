import socket
from pygame import *

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("localhost", 5050))

def main():
	init()
	
	for x in range(joystick.get_count()):
		j = joystick.Joystick(x)
		j.init()
		print 'Enabled joystick: ' + j.get_name()
	
	while 1:
		for e in event.get():
			txt = ""
			
			print e
			
			if e.type is JOYAXISMOTION: # 7
				txt = "%d %s %d %f" % (e.joy, "axis", e.axis, e.value)
	
			elif e.type is JOYBALLMOTION: # 8
       				txt = "%d %s %d %f" % (e.joy, "ball", e.ball, e.value)
	
			elif e.type is JOYHATMOTION: # 9
				txt = "%d %s %d %f %f" % (e.joy, "hat", e.hat, e.value[0], e.value[1])
		
			elif e.type is JOYBUTTONDOWN: # 10
				txt = "%d %s %d %d" % (e.joy, "button", e.button + 1, 1)
	
			elif e.type is JOYBUTTONUP: # 11
				txt = "%d %s %d %d" % (e.joy, "button", e.button + 1, 0)

			if (txt):
				s.send(txt + ";\n")
		
		time.wait(50)

if __name__ == '__main__': main()

s.close()
