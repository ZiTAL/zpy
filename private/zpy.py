#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, web
from lib.route import Route

sys.dont_write_bytecode = True

urls = ("/.*", "Zpy")
app = web.application(urls, globals())

# sessions in sqlite
db = web.database(dbn='sqlite', db='config/session.db')
store = web.session.DBStore(db, 'sessions')
#session = web.session.Session(app, store, initializer={'count': 0})
session = web.session.Session(app, store)

def session_hook():
    web.ctx.session = session

app.add_processor(web.loadhook(session_hook))

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
	# for cgi
	#web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
	app.run()
