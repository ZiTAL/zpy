#!/usr/bin/python2
# -*- coding: utf-8 -*-

import json, web

from lib.log import Log

class Env(object):

	@staticmethod
	def get(key):
		if key and key in web.ctx.env:
			return web.ctx.env[key]
		else:
			return web.ctx.env
	
	@staticmethod
	def set(key, value):
		web.ctx.env[key] = value

	@staticmethod
	def setFromFile(file):
		fenv = open(file)
		jenv = json.load(fenv)

		for key,value in jenv.items():
			web.ctx.env[key] = value