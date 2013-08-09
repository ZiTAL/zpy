#!/usr/bin/env python
# -*- coding: utf-8 -*-

from web import ctx

class Session(object):

	@staticmethod
	def set(key, value):
		if 'session' in ctx:		
			ctx.session[key] = value
		return None

	@staticmethod
	def get(key):
		if key in ctx.session:
			return ctx.session[key]
		return  False
