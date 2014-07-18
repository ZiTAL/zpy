#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.Controller import Controller
from core.View import View

class Default(Controller):

	def main(self):
		tpl = View.load('default.tpl', {'title': 'zpy'})
		return tpl