#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from lib.route import Route

urls = ("/.*", "Zpy")
app = web.application(urls, globals())

class Zpy:
	def GET(self):
		return self.main()
	def POST(self):
		return self.main()
	def PUT(self):
		return self.main()
	def DELETE(self):
		return self.main() 

	def main(self):
		r = Route()       
		return r.main()
		#return "method: "+web.ctx.method + " path:"+web.ctx.path
		#return web.input(_method=web.ctx.method)

if __name__ == "__main__":
	web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
	app.run()
