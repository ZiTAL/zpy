#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

from core.Controller import Controller
from core.View import View

from lib.session import Session

class Sessions(Controller):

	def set(self):
		Session.set('count', 1)
		return View.load('/session/set.tpl')

	def get(self):
		params = {}
		params['key'] = 'count'
		params['value'] = Session.get('count')

		return View.load('/session/get.tpl', params)

	def add(self):
		count = Session.get('count')
		count = count + 1
		Session.set('count', count)
		raise web.seeother('/session/get/')

	def remove(self):
		count = Session.get('count')
		if count > 0:
			count = count - 1
		else:
			count = 0

		Session.set('count', count)
		raise web.seeother('/session/get/')


	def destroy(self):
		Session.destroy()
		raise web.seeother('/session/get/')