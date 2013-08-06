#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web, json, re, sys

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
		if not path.endswith('/'):
			path = path + "/"
			web.redirect(path, '301 ')

		# check url in routes json
		for key,value in r.items():

			if self._regex(path, key):

				# controller dynamic load
				#module_name = "controller."+value['controller']
				module_name = "controller.{}".format(value['controller'])

				# uppercase first char
				#class_name = value['controller'][0].upper() + value['controller'][1:]
				class_name = value['controller'].title()

				#default method name
				method_name = 'main'
				if 'method' in value:
					method_name = value['method']

				# from path import module
				module = __import__(module_name, fromlist=[class_name])

				# get class from module
				class_object = getattr(module, class_name)

				# instance module
				controller_instance = class_object()

				# exec method from class instance
				func = getattr(controller_instance, method_name)
				return func()

		# redirect to 404 page
		return None;


	def _getPath(self):
		if 'path' in web.ctx:
			return web.ctx.path
		else:
			return "/"

	def _regex(self, url, to_match):
		# allowed pattern
		allow = "[A-Za-z\-\_\%]+"

		# replace * to allow
		to_match = re.sub("\*", allow, to_match)

		# replace ? to allow - or nothing
		to_match = re.sub("/\?", "(|/"+allow+")", to_match)

		# start and end
		if re.match(r'^'+to_match+'$', url):
			return True
		return None
