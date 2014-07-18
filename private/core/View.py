#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os, sys
from jinja2 import Environment, FileSystemLoader

project_folder = os.path.dirname(os.path.realpath(sys.argv[0]))
env = Environment(loader=FileSystemLoader(project_folder+"/view"))

class View(object):

	@staticmethod
	def load(file, params={}):
		tpl = env.get_template(file)
		return tpl.render(params)