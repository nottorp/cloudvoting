#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from abc import ABCMeta, abstractmethod
#import CCResponse

from flask import request

class CCPlugin(object):
	def perform(self):
		print("Path: %s doesn't implement perform() method !" % self._path)

	def shutdown(self):
		print("Path: %s doesn't implement shutdown() method !" % self._path)

	def getPath(self):
		return self._path

	#@abstractmethod
	def __init__(self):
		self._path = None
		self._request = request

