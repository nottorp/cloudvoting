className = "BordaCounter"

class BordaCounter(CCPlugin):
	def perform(self):
        return "WIP"

	def shutdown(self):
        print "Shutting down Borda counter"

	def __init__(self):
		CCPlugin.__init__(self)
		self._path = "/borda"
		#self.db = pickledb.load('storage.db', True)