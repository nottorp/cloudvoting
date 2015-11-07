#!/usr/bin/python
# -*- coding: UTF-8 -*-
from cloudclient import CCConnectionQueue
from cloudclient import CCConnection
from cloudclient import CCPluginManager

class CCConnectionManager(object):
	def run(self):
		pass

	def stop(self):
		pass

	def __CCConnectionManager(self):
		pass

	def getInstance(self):
		"""@ReturnType cloudclient.CCConnectionManager"""
		pass

	def __init__(self):
		self.___queue = None
		"""@AttributeType cloudclient.CCConnectionQueue"""
		self.___connection = None
		"""@AttributeType cloudclient.CCConnection*"""
		self.___pluginManager = None
		"""@AttributeType cloudclient.CCPluginManager"""
		self.___instance = None
		self._unnamed_CCConnectionQueue_ = None
		# @AssociationType cloudclient.CCConnectionQueue
		# @AssociationKind Aggregation
		self._unnamed_CCConnection_ = None
		# @AssociationType cloudclient.CCConnection
		# @AssociationKind Aggregation

