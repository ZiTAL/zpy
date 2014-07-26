#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.controller import Controller
from core.view import View

from lib.cookie import Cookie

class Cookies(Controller):

	def set(self):
		params = {}
		params['key'] = 'key'
		params['value'] = 'zpy is the law'

		Cookie.set(params['key'], params['value'], 3600)

		return View.load('/cookie/set.tpl', params)

	def get(self):
		params = {}
		params['key'] = 'key'
		params['value'] = Cookie.get('key')

		return View.load('/cookie/get.tpl', params)		

	def destroy(self):
		Cookie.delete('key')
		return View.load('/cookie/destroy.tpl')