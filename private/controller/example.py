#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from lib.session import Session
from lib.cookie import Cookie

class Example(object):

	def main(self):

		Session.delete('count')

		count = Session.get('count')
		if count == False:
			count = 0
		count = count + 1
		Session.set('count', count)
		return count

	def logout(self):
		Cookie.set('key', 'value', 3600)
		Session.destroy()
		return '<a href="/">go to main</a>'
		#web.redirect("/")
