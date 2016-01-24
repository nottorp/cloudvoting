#!/usr/bin/python
# -*- coding: UTF-8 -*-

from CCPlugin import CCPlugin
import time
import shelve


className = "Storage"

class Storage(CCPlugin):
	def perform(self):
		now = str(int(time.time()))
		self.db[now] = " storage perform()"
		keys = self.db.keys()
		output = ""
		for k in keys:
			output += "@" + k + " : " + str(self.db[k]) + "<br>"

		return output

	def shutdown(self):
		print "Storage: shutdown()"
		self.db.sync()
		self.db.close()

	def __init__(self):
		CCPlugin.__init__(self)
		self._path = "/storage"
		self.db = shelve.open("storage.db.shelve", writeback=True)

