#!/usr/bin/python
# -*- coding: UTF-8 -*-

from CCPlugin import CCPlugin

className = "Failing"

class Failing(CCPlugin):
	def perform(self):
		pass

	def __init__(self):
		CCPlugin.__init__(self)
		self._path = "/fail"

if __name__ == "__main__":
	p = Failing()
	p.perform()

