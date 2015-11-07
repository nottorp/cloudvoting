#!/usr/bin/python
# -*- coding: UTF-8 -*-
from cloudclient import CCConnectionData

class CCResponse(CCConnectionData):
	def __init__(self):
		self.___requestUID = None
		"""@AttributeType string"""

