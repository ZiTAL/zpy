#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web, json, re

from core.error import Error
from lib.log import Log
from lib.url import Url

class Route(object):

	def main(self):
		routes = self._load()
		return routes
		#return "method: "+web.ctx.method + " path:"+web.ctx.path

	def _load(self):
		# get routes
		f = open('config/route.json')
		r = json.load(f)

		# get uri
		path = Url.getUri()

		# if url doesn't end with /, redirect to / ended url
		if path.endswith('/') == False:
			path = path + "/"
			raise web.redirect(path, '301 ')

		# check url in routes json
		for key,value in r.items():

			if self._regex(path, key):

				# controller dynamic load
				module_name = "controller.{}".format(value['controller'])

				# uppercase first char
				class_name = value['controller'].title()

				#default method name
				method_name = 'main'
				if 'method' in value:
					method_name = value['method']

				# from path import module
				try:
					module = __import__(module_name, fromlist=[class_name])
				except Exception as e:
					Log.error(e)
					raise Error('500')

				# get class from module
				try:
					class_object = getattr(module, class_name)
				except Exception as e:
					return Log.error(e)

				# instance module
				try:
					controller_instance = class_object()
				except Exception as e:
					return Log.error(e)

				# exec method from class instance
				try:				
					func = getattr(controller_instance, method_name)
				except Exception as e:
					return Log.error(e)

				# method instance
				try:
					func_instance = func()
					return func_instance
				except Exception as e:
					m = re.match("[0-9]{3}", str(e))
					if m:
						http_code = m.group(0)
						if re.match("(4|5)", http_code):
							Error(http_code)

		# redirect to 404 page
		raise Error('404')

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
