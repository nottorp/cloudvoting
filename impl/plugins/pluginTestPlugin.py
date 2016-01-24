#!/usr/bin/python
# -*- coding: UTF-8 -*-

from CCPlugin import CCPlugin

className = "TestPlugin"

class TestPlugin(CCPlugin):
	def perform(self):
		print self._request.args
		return "Test Plugin: perform(): " + repr(self._request.__dict__)

	def __init__(self):
		CCPlugin.__init__(self)
		self._path = "/test"

if __name__ == "__main__":
	p = TestPlugin()
	p.perform()

