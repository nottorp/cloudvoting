#!/usr/bin/python
# -*- coding: UTF-8 -*-

from CCPlugin import CCPlugin
import requests
import json
className = "TestPlugin"

class TestPlugin(CCPlugin):
	def perform(self):
		testResults = {}
		try:
			r = requests.get("http://localhost:9000/")
			plugins = r.json()
			print plugins
			for p in plugins:
				print p
				if p["path"] == self._path:
					continue

				try:
					r = requests.get("http://localhost:9000" + str(p["path"]))
					if r.status_code != 200:
						testResults[p["name"]] = "fail"
					else:
						testResults[p["name"]] = "working"
				except ValueError:
					testResults[p["name"]] = "did not return a response"

				#testResults[p["name"]] = "working"
		except Exception, e:
			testResults["general"] = e

		return json.dumps(testResults)

	def __init__(self):
		CCPlugin.__init__(self)
		self._path = "/test"


if __name__ == "__main__":
	p = TestPlugin()
	p.perform()

