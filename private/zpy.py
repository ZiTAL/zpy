#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys, web
from lib.route import Route

web.config.debug = True

urls = ("/.*", "Zpy")
app = web.application(urls, globals())

# sessions in db
db = web.database(dbn='sqlite', db='config/session.db')
store = web.session.DBStore(db, 'sessions')
session = web.session.Session(app, store)

# put session object in web.py's ctx namespace
def session_hook():
    web.ctx.session = session
app.add_processor(web.loadhook(session_hook))

# for each http request method redirect to Route
class Zpy(object):
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
		#return web.input(_method=web.ctx.method)

if __name__ == "__main__":
	# for cgi
	#web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
	app.run()