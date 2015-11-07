#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod

class CCCommand(object):
	"""@Interface"""
	__metaclass__ = ABCMeta
	@abstractmethod
	def wait(self):
		pass

	@abstractmethod
	def finished(self):
		pass

	@abstractmethod
	def __init__(self):
		self._args = None
		self._commands = None
		self._name = None

