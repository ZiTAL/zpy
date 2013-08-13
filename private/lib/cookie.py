#!/usr/bin/env python
# -*- coding: utf-8 -*-

from web import webapi

class Cookie(object):

	@staticmethod
	def get(key):
		return webapi.cookies()

	@staticmethod
	def set(key, value, expire):
		#setcookie(key, value, expires='', domain=None, secure=False, httponly=False, path=None)
		webapi.setcookie(key, value, expire)
		return None

	@staticmethod
	def delete(key):
		webapi.setcookie(key, None, -1)
		return None
