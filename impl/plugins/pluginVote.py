from CCPlugin import CCPlugin

className = "Vote"

class Vote(CCPlugin):
	def perform(self):
		return "WIP"

	def shutdown(self):
		print "Shutting down Borda counter"

	def __init__(self):
		CCPlugin.__init__(self)
		self._path = "/vote"
		#self.db = pickledb.load('storage.db', True)