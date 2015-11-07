#!/usr/bin/python
# -*- coding: UTF-8 -*-
from cloudclient import CCDatabase
from cloudclient import CCCommand

class CCDBCommand(object):
	def setUnnamed_CCDatabase_(self, aUnnamed_CCDatabase_):
		"""@ParamType aUnnamed_CCDatabase_ cloudclient.CCDatabase
		@ReturnType void"""
		self._unnamed_CCDatabase_ = aUnnamed_CCDatabase_

	def getUnnamed_CCDatabase_(self):
		"""@ReturnType cloudclient.CCDatabase"""
		return self._unnamed_CCDatabase_

	def setUnnamed_CCCommand_(self, aUnnamed_CCCommand_):
		"""@ParamType aUnnamed_CCCommand_ cloudclient.CCCommand
		@ReturnType void"""
		self._unnamed_CCCommand_ = aUnnamed_CCCommand_

	def getUnnamed_CCCommand_(self):
		"""@ReturnType cloudclient.CCCommand"""
		return self._unnamed_CCCommand_

	def __init__(self):
		self._unnamed_CCDatabase_ = None
		# @AssociationType cloudclient.CCDatabase
		self._unnamed_CCCommand_ = None
		# @AssociationType cloudclient.CCCommand
		# @AssociationKind Composition

