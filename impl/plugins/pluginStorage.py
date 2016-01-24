#!/usr/bin/python
# -*- coding: UTF-8 -*-

from CCPlugin import CCPlugin
import time
import shelve


className = "Storage"

class Storage(CCPlugin):
	def perform(self):
		now = str(int(time.time()))

		print self._request.args

		if not 'a' in self._request.args:
			return "ERR Missing action!"
		if not 'k' in self._request.args:
			return "ERR Missing key!"

		key = self._request.args['k']

		if self._request.args['a'] == 'set':
			if not 'v' in self._request.args:
				return "ERR Missing value!"
			self.db[key] = self._request.args['v']
			self.db.sync()
			return "OK"
		elif self._request.args['a'] == 'get':
			if not key in self.db:
				return "OK"
			return "OK " + self.db[key]
			# Keeping it here for possible testing
			#output = ''
			#for k in self.db.keys():
			#	output += "@" + k + " : " + str(self.db[k]) + "<br>"
			#return output
		else:
			return "ERR Unknown command!"

	def shutdown(self):
		print "Storage: shutdown()"
		self.db.sync()
		self.db.close()

	def __init__(self):
		CCPlugin.__init__(self)
		self._path = "/storage"
		self.db = shelve.open("storage.db.shelve", writeback=True)

