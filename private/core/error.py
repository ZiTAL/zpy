#!/usr/bin/python2
# -*- coding: utf-8 -*-

import web, json, time

from core.view import View
from lib.log import Log
from lib.env import Env

class Error(web.HTTPError):
	def __init__(self, status, headers={}, tpl=None):
		
		# get http status code's from json
		hsc = open('config/http_status_codes.json')
		jhsc = json.load(hsc)
		
		# view params
		params = {'key': status, 'value': ''}
		params['SERVER_NAME'] = Env.get('SERVER_NAME')
		params['CONTACT'] = Env.get('CONTACT')
		params['SERVER_SOFTWARE'] = Env.get('SERVER_SOFTWARE')

		# status exists in json
		if status in jhsc:
			params['value'] = jhsc[status]		
		
		# status tpl
		if(tpl==None):
			tpl = "error/"+status+".tpl"
		
		# Content type required header
		if('Content-Type' in headers):
			pass
		else:
			headers['Content-Type'] = 'text/html'
		
		# load view
		data = View.load(tpl, params)
		
		# view not exists, load default tpl
		if data==False:
			tpl = 'error/default.tpl'
			data = View.load(tpl, params)

		msg =	"\nzpy Error: \n"
		msg +=	"Status: "+status+"\n"
		msg +=	"Url: "+Env.get('REQUEST_URI')+"\n"
		msg +=	"Remote Address: "+Env.get('REMOTE_ADDR')+"\n"
		msg +=	"Date: "+time.strftime("%Y/%m/%d %H:%M:%S")+"\n"
		msg +=	"-------------------------------------------"
		
		Log.debug(msg)
		web.HTTPError.__init__(self, status, headers, data)