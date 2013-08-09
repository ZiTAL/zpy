#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.session import Session

class Example(object):

	def main(self):		
		count = Session.get('count')
		if count == False:
			count = 0
		count = count + 1
		Session.set('count', count)
		return count
