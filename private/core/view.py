#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os, sys
from jinja2 import Environment, FileSystemLoader
from lib.log import Log

project_folder = os.path.dirname(os.path.realpath(sys.argv[0]))
view_folder = project_folder+"/view/"
env = Environment(loader=FileSystemLoader(view_folder))

class View(object):

	@staticmethod
	def load(file, params={}):
		tpl = view_folder+file
		if(os.path.isfile(tpl) and os.access(tpl, os.R_OK)):
			tpl = env.get_template(file)
			return tpl.render(params)
		else:
			Log.debug(tpl+": file not exists")
			return False