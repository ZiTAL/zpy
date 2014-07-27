#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, inspect

class Log(object):

	@staticmethod
	def debug(e):
		print >> sys.stderr, str(e)
		
	@staticmethod
	def error(e):
		# get code traces
		stack = inspect.stack()

		#revert stack list
		stack = stack[::-1]
		# remove web.py's logs
		for i in range(0, 26):
			stack.pop(0)
		
		msg = ''
		for i in stack:
			# get code from the list and trim
			code = str(i[4][i[5]]).strip()

			msg2 =	"\tFrame:\t\t"+str(i[0])+"\n"
			msg2 += "\tFile:\t\t"+str(i[1])+"\n"
			msg2 += "\tLine:\t\t"+str(i[2])+"\n"
			msg2 += "\tFunc:\t\t"+str(i[3])+"\n"
			msg2 += "\tCode:\t\t"+code+"\n\n"

			msg = msg + msg2

		msg = "zpy error:\n"+msg

		if e!='':
			msg += "\tError:\t\t"+str(e)+"\n\n"
			Log.debug(msg)			