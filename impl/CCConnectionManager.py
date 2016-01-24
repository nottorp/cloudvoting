#!/usr/bin/python
# -*- coding: UTF-8 -*-
import CCConnectionQueue
import CCConnection
from CCPluginManager import CCPluginManager

import sys
from flask import Flask
app = Flask(__name__)

PLUGIN_DIR = './plugins'
sys.path.append(PLUGIN_DIR)

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


	def index(self):
		return `self.paths`

	def __init__(self):
		self.___queue = None
		"""@AttributeType cloudclient.CCConnectionQueue"""
		self.___connection = None
		self.___pluginManager = CCPluginManager()
		self.___pluginManager.locate(PLUGIN_DIR)
		self.___pluginManager.load()
		pl = self.___pluginManager.getPlugins()
		self.paths = []
		for p in pl:
			pluginInstance = p.get("instance")
			pluginInstancePath = pluginInstance.getPath()
			if pluginInstance is not None and pluginInstancePath is not None:
				self.paths.append(pluginInstancePath)
				print("Plugin: %s REST Path: %s" % (p["name"], pluginInstancePath))
				app.add_url_rule(pluginInstancePath, pluginInstancePath, pluginInstance.perform)

		app.add_url_rule('/', 'index', self.index)

		"""@AttributeType cloudclient.CCPluginManager"""
		self.___instance = None
		self._unnamed_CCConnectionQueue_ = None
		# @AssociationType cloudclient.CCConnectionQueue
		# @AssociationKind Aggregation
		self._unnamed_CCConnection_ = None
		# @AssociationType cloudclient.CCConnection
		# @AssociationKind Aggregation

if __name__ == "__main__":
	cm = CCConnectionManager()
	app.debug = True
	app.run(port=9000)


