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
				continue
			plugin_name = modname[6:]
			plugin_class_name = getattr(mod, "className")
			plugin_class = getattr(mod, plugin_name)
			self.___pluginList.append({"name": plugin_class_name, "class": plugin_class, "instance": None})

	def load(self):
		for p in self.___pluginList:
			p["instance"] = p["class"]()

	def run(self):
		pass

	def registerPlugin(self, pluginName):
		for p in self.___pluginList:
			if p["name"] == pluginName:
				return p["class"]()

		return None

	def dispatch(self):
		pass

	def getResult(self):
		pass

	def operation(self):
		pass

	def listPlugins(self):
		for p in self.___pluginList:
			print(p)

	def getPlugins(self):
		return self.___pluginList

	def shutdown(self):
		for p in self.___pluginList:
			i = p.get("instance")
			if i is not None:
				i.shutdown()

	def __init__(self):
		self.___pluginList = []
		self.___resultsQueue = None
		"""@AttributeType Queue"""
		self._unnamed_CCPlugin_ = None
		# @AssociationType cloudclient.CCPlugin
		# @AssociationKind Aggregation


# UNIT Test
if __name__ == "__main__":
	PLUGIN_DIR = './plugins'
	sys.path.append(PLUGIN_DIR)

	pm = CCPluginManager()

	pm.locate(PLUGIN_DIR)
	pm.listPlugins()
	pm.load()
	pm.listPlugins()
	storagePlugin = pm.registerPlugin("Storage")
	print(storagePlugin.getPath())

