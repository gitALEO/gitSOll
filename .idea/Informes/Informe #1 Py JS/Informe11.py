import threading
import datetimne

class ThreadClass(threading.Thread):
	def run(self):
		now = datetime.datetime.now()
		print(“%s  Decir hole en el tiempo: %s” %(self.getName(), now))
for I in range (3):
	t = ThreadClass()
	t.start()
