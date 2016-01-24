#!/usr/bin/python
# -*- coding: UTF-8 -*-
import CCConnectionData
import CCConnectionManager

class CCConnectionQueue(object):
	def put(self):
		pass

	def get(self):
		pass

	def __init__(self):
		self.___incoming = None
		"""@AttributeType cloudclient.CCConnectionData"""
		self.___outgoing = None
		"""@AttributeType cloudclient.CCConnectionData"""
		self._unnamed_CCConnectionManager_ = None
		# @AssociationType cloudclient.CCConnectionManager
		self = None
		# @AssociationType cloudclient.CCConnectionData
		# @AssociationKind Aggregation

