#!/usr/bin/python
# -*- coding: UTF-8 -*-

from CCPlugin import CCPlugin
import pickledb
import time


className = "Storage"

class Storage(CCPlugin):
	def perform(self):
		now = int(time.time())
		self.db.set(now, 'perform()')
		keys = self.db.getall()
		output = ""
		for k in keys:
			output += "@" + str(k) + " : " + self.db.get(k) + "<br>"

		return output

	def __init__(self):
		self._path = "/storage"
		self._request = None
		self.db = pickledb.load('storage.db', False)
		"""@AttributeType cloudclient.CCResponse"""

