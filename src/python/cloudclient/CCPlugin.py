#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from cloudclient import CCResponse

class CCPlugin(object):
	"""@Interface"""
	__metaclass__ = ABCMeta
	@abstractmethod
	def perform(self):
		pass

	@abstractmethod
	def __init__(self):
		self._path = None
		self._request = None
		"""@AttributeType cloudclient.CCResponse"""

