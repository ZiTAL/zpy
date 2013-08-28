#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

class Default(object):

	def main(self):

		html = """<!doctype html>
<html>
<head>
</head>
<body>
	<ul>
		<li><h1>Cookie</h1></li>
		<li><a href="/cookie/set/">cookie set</li>
		<li><a href="/cookie/get/">cookie get</li>
		<li><a href="/cookie/destroy/">cookie destroy</li>
		<li><h1>Session</h1></li>
		<li><a href="/session/set/">session set</li>
		<li><a href="/session/get/">session get</li>
		<li><a href="/session/add/">session +1 var</li>
		<li><a href="/session/remove/">session -1 var</li>
		<li><a href="/session/destroy/">session destroy</li>
	</ul>
</body>
</html>"""
		return html
