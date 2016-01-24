
from CCPlugin import CCPlugin
from storageHelper import storageGetAll

className = "Borda"

optionNames = ['Cake', 'Pudding', 'Candy', 'Lollipop', 'Ion Iliescu']

class Borda(CCPlugin):
	def perform(self):
		print "************************************************"
		all = storageGetAll()
		print all
		scores = [0, 0, 0, 0, 0]
		for vote in all.itervalues():
			votelist = map(int, vote.split(','))
			print 'votelist:', votelist
			print 'votelist[0]:', votelist[0]
			for i in range(1, 6):
				if len(votelist) >= i:
					print "Adjusting vote for ", i-1, "by", 5-i
					idx = votelist[i-1]-1
					print "idx=", idx, "len(scores)=", len(scores)
					scores[idx] += (5 - i)
			print scores
		print "************************************************"
		scoresdict = {}
		for i in range(0, len(scores)):
			scoresdict[i+1] = scores[i]
		final = sorted(scoresdict, key=scoresdict.get, reverse=True)
		output = "Borda hierarchy:<br/>"
		for i in final:
			print "index is", i
			output += optionNames[i-1] + ": " + str(scoresdict[i]) + "<br/>"
		return output


	def shutdown(self):
		print "Shutting down Borda counter"

	def __init__(self):
		CCPlugin.__init__(self)
		self._path = "/borda"
		#self.db = pickledb.load('storage.db', True)