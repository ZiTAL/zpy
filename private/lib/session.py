#!/usr/bin/env python
# -*- coding: utf-8 -*-

from web import ctx

session = ctx.session

class Session(object):

	@staticmethod
	def set(key, value):
		session[key] = value
		return True

	@staticmethod
	def get(key):
		if key in session:
			return session[key]
		return  False

	@staticmethod
	def delete(key):
		session.pop(key, None)
		return None

	@staticmethod
	def getAll():
		result = {}
		for key in session.keys():
			result[key] = session[key]
		return result

	@staticmethod
	def getId():
		return Session.get('session_id')

	@staticmethod
	def destroy():
		session.kill()
