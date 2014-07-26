#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.controller import Controller
from core.view import View

class Default(Controller):

	def main(self):
		tpl = View.load('default.tpl', {'title': 'zpy'})
		return tpl