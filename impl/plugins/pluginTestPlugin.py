#!/usr/bin/python
# -*- coding: UTF-8 -*-

from CCPlugin import CCPlugin

className = "TestPlugin"

class TestPlugin(CCPlugin):
	def perform(self):
		return "Test Plugin: perform()"

	def __init__(self):
		self._path = "/test"
		self._request = None
		"""@AttributeType cloudclient.CCResponse"""

