#!/usr/bin/python
# -*- coding: UTF-8 -*-
from CCPlugin import CCPlugin

import glob
import importlib
import sys
import os

class CCPluginManager(object):
	def locate(self, pluginDir):
		possible_plugins = glob.glob(pluginDir + "/plugin*.py")
		for p in possible_plugins:
			try:
				modname = os.path.splitext(os.path.basename(p))[0]
				print "Importing", modname
				mod = importlib.import_module(modname)
			except Exception as e:
				# If I can't import it, i'm not interested in it
				print e
				pass
			plugin_class_name = getattr(mod, "className")
			plugin_class = getattr(mod, plugin_name)
				
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
		self.___pluginList = []
		self.___resultsQueue = None
		"""@AttributeType Queue"""
		self._unnamed_CCPlugin_ = None
		# @AssociationType cloudclient.CCPlugin
		# @AssociationKind Aggregation

sys.path.append('.')

pm = CCPluginManager()

pm.locate('.')
