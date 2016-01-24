#!/usr/bin/python
# -*- coding: UTF-8 -*-

from CCPlugin import CCPlugin

className = "TestPlugin"

class TestPlugin(CCPlugin):
	def perform(self):
		pass

	def __init__(self):
		self._path = None
		self._request = None
		"""@AttributeType cloudclient.CCResponse"""

