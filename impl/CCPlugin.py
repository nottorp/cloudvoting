#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from abc import ABCMeta, abstractmethod
#import CCResponse

class CCPlugin(object):
	#"""@Interface"""
	#__metaclass__ = ABCMeta
	#@abstractmethod
	def perform(self):
		pass

	def getPath(self):
		return self._path

	#@abstractmethod
	def __init__(self):
		self._path = None
		self._request = None
		"""@AttributeType cloudclient.CCResponse"""

