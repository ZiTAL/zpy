#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from lib.session import Session

class Sessions(object):

	def set(self):
		Session.set('count', 1)

		html = """<!doctype html>
<html>
<head>
<title>Session set</title>
</head>
<body>
<p>Session set "count" => "1"
</body>
</html>"""
		return html


	def get(self):
		html = """<!doctype html>
<html>
<head>
<title>Session get</title>
</head>
<body>
<p>Session key: <strong>{key}</strong> and value: <strong>{value}</strong></p>
</body>
</html>"""

		html = html.format(key="count", value=Session.get('count'))
		return html

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
