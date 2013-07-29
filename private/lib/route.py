#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web, json, re

class Route(object):

	def main(self):
		routes = self._load()
		return routes
		#return "method: "+web.ctx.method + " path:"+web.ctx.path

	def _load(self):
		# get routes
		f = open('config/route.json')
		r = json.load(f)

		# get url
		path = self._getPath()

		# if url doesn't end with /, redirect to / ended url
		m = re.search(r'[^\/]$', path)
		if(m!=None):
			path = path + "/"
			web.redirect(path, '301 ')

		# check url in routes json
		for key,value in r.items():
			if self._regex(path, key):
				return value

		# redirect to 404 page
		return None;

	def _getPath(self):
		return web.ctx.path

	def _regex(self, url, to_match):
		# replace * -> a-z 0-9 -
		to_match = re.sub("\*", "[A-Za-z\-\_\%]+", to_match)

		# replace ? -> a-z 0-9 - or nothing
		to_match = re.sub("/\?", "(|/[A-Za-z\-\_\%]+)", to_match)

		if re.match(r'^'+to_match+'$', url):
			return True
		return None
