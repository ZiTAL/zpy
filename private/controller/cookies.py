#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from lib.cookie import Cookie

class Cookies(object):

	def set(self):
		Cookie.set('key', 'value', 3600)

		html = """<!doctype html>
<html>
<head>
<title>Cookie set</title>
</head>
<body>
<p>Cookie set "key" => "value"
</body>
</html>"""
		return html


	def get(self):
		html = """<!doctype html>
<html>
<head>
<title>Cookie get</title>
</head>
<body>
<p>Cookie key: <strong>{key}</strong> and value: <strong>{value}</strong></p>
</body>
</html>"""

		html = html.format(key="key", value=Cookie.get('key'))
		return html

	def destroy(self):
		Cookie.delete('key')

		html = """<!doctype html>
<html>
<head>
<title>Cookie get</title>
</head>
<body>
<p>Cookie "key" deleted</p>
</body>
</html>"""
		return html
