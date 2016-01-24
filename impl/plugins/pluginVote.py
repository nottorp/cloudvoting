from CCPlugin import CCPlugin

className = "Vote"

form = """
<html><body><form method="get">
Your options are:<br/>
1 - Cake<br/>
2 - Pudding<br/>
3 - Candy<br/>
4 - Lollipop<br/>
5 - Ion Iliescu<br/>
Please enter your order of preference, best first, in the field below, then press submit<br/>
<input name="hierarchy" type="text" value="5"/><br/>
<input type="submit"/>
<input type="hidden" name="postme" value="dummy"/>
</form></body></html>
"""

class Vote(CCPlugin):
	def perform(self):
		if 'postme' in self._request.args:
			res = self._request.args['hierarchy']
			return "Received hierarchy: " + str(res)
		return form

	def shutdown(self):
		print "Shutting down Borda counter"

	def __init__(self):
		CCPlugin.__init__(self)
		self._path = "/vote"
		#self.db = pickledb.load('storage.db', True)