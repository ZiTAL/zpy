#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, inspect, re

class Error(object):

	@staticmethod
	def log(e):
		"""
		stack = inspect.stack()
		
		msg = ''
		for i in stack:
			# get code from the list and trim
			code = str(i[4][i[5]]).strip()

			msg2 =	"\tFrame:\t\t"+str(i[0])+"\n"
			msg2 += "\tFile:\t\t"+str(i[1])+"\n"
			msg2 += "\tLine:\t\t"+str(i[2])+"\n"
			msg2 += "\tFunc:\t\t"+str(i[3])+"\n"
			msg2 += "\tCode:\t\t"+code+"\n\n"

			msg = msg2 + msg


		msg = "zpy error:\n"+msg

		if(e!=''):
			msg += "\tError:\t\t"+str(e)+"\n\n"
		"""
		print >> sys.stderr, ":"+str(e)+":"