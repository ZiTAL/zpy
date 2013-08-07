#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

class Url(object):

	_params = []

	@staticmethod
        def getUri():
                if 'path' in web.ctx:
                        return web.ctx.path
                else:
                        return "/bat/"

	@staticmethod
	def getParamsFromUri(uri):
		parts = uri.split('/')
		
		# remove empty parts
		params = filter(None, parts)
		return params

	@staticmethod
	def setParams():
		uri = Url.getUri()
		Url._params = Url.getParamsFromUri(uri)

	@staticmethod
	def getParams():
		return Url._params

Url.setParams()
