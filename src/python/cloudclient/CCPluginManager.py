#!/usr/bin/python
# -*- coding: UTF-8 -*-
from cloudclient import CCPlugin

class CCPluginManager(object):
	def locate(self):
		pass

	def load(self):
		pass

	def run(self):
		pass

	def registerPlugin(self):
		pass

	def dispatch(self):
		pass

	def getResult(self):
		pass

	def operation(self):
		pass

	def __init__(self):
		self.___pluginList = None
		self.___resultsQueue = None
		"""@AttributeType Queue"""
		self._unnamed_CCPlugin_ = None
		# @AssociationType cloudclient.CCPlugin
		# @AssociationKind Aggregation

