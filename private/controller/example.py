#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.session import Session

class Example(object):

	def main(self):		
		count = Session.get('count')
		count = count + 1
		Session.set('count', count)
		return count
