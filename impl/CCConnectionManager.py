#!/usr/bin/python
# -*- coding: UTF-8 -*-
import CCConnectionQueue
import CCConnection
from CCPluginManager import CCPluginManager
from multiprocessing import Process

import sys, signal
from flask import Flask
from flask import request

PLUGIN_DIR = './plugins'
sys.path.append(PLUGIN_DIR)

class CCConnectionManager(object):
	def run(self):
		self.___app.debug = True
		self.___app.run(port=9000)

	def stop(self):
		pass

	def __CCConnectionManager(self):
		pass

	def getInstance(self):
		"""@ReturnType cloudclient.CCConnectionManager"""
		pass


	def index(self):
		return `self.paths`

	def __init__(self, app):
		self.___queue = None
		self.___connection = None
		self.___app = app
		self.___server = None


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
				self.___app.add_url_rule(pluginInstancePath, pluginInstancePath, pluginInstance.perform)

		self.___app.add_url_rule('/', 'index', self.index)
		self.___app.add_url_rule('/shutdown', 'shutdown', self.shutdown)

		self.___instance = None

	def shutdown(self):
		print "Shutting down"
		self.___pluginManager.shutdown()
		self._shutdown_app()
		return "Shutting down"


	def _shutdown_app(self):
		func = request.environ.get('werkzeug.server.shutdown')
		if func is None:
			raise RuntimeError('Not running with the Werkzeug Server')
		func()

if __name__ == "__main__":
	app = Flask(__name__)
	cm = CCConnectionManager(app)
	cm.run()

	def signalHandler(signal, frame):
		cm.shutdown()

	signal.signal(signal.SIGINT, signalHandler)






