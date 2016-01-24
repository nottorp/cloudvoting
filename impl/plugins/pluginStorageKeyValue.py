#!/usr/bin/python
# -*- coding: UTF-8 -*-

from CCPlugin import CCPlugin
import pickledb
import time


className = "StorageKeyValue"

class StorageKeyValue(CCPlugin):
	def perform(self):
		now = int(time.time())
		self.db.set(now, 'perform()')
		keys = self.db.getall()
		output = ""
		for k in keys:
			output += "@" + str(k) + " : " + self.db.get(k) + "<br>"

		return output

	def shutdown(self):
		print "Storage Key Value: shutdown()"
		self.db.dump()

	def __init__(self):
		CCPlugin.__init__(self)
		self._path = "/storagekv"
		self.db = pickledb.load('storage.db', True)

