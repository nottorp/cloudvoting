from CCPlugin import CCPlugin

from storageHelper import storageSet

className = "Vote"

form = """
<html><body><form method="get">
Enter name: <input name="name" type="text" /><br/>
Your options are:<br/>
1 - Cake<br/>
2 - Pudding<br/>
3 - Candy<br/>
4 - Lollipop<br/>
5 - Ion Iliescu<br/>
Please enter your order of preference, best first, separated with spaces, in the field below, then press submit<br/>
<input name="hierarchy" type="text" value="5"/><br/>
<input type="submit"/>
<input type="hidden" name="postme" value="dummy"/>
</form></body></html>
"""

class Vote(CCPlugin):
	def perform(self):
		if 'postme' in self._request.args:
			if (not 'name' in self._request.args) or (not 'hierarchy' in self._request.args):
				return "ERR Must specify name and hierarchy!"
			name = self._request.args['name']
			hier = self._request.args['hierarchy']
			if len(name) == 0:
				return "ERR Empty name!"
			# Extract only the digit sequences
			nums = [int(s) for s in hier.split() if s.isdigit()]
			for num in nums:
				if num < 1 or num > 5:
					return "ERR Options are 1 to 5"
			packed_hier = ','.join(str(x) for x in nums)
			storageSet(name, packed_hier)
			return "OK Succesfully voted."

		return form

	def shutdown(self):
		print "Shutting down Borda counter"

	def __init__(self):
		CCPlugin.__init__(self)
		self._path = "/vote"
		#self.db = pickledb.load('storage.db', True)