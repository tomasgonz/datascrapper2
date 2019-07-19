import time
import threading
import sys
import os
import countries
import console

# Import data sources
import sources

# to inspect methods of classes
import inspect

from colorama import init, Fore, Back, Style

import getpass
import cmd

class Shell(cmd.Cmd):

	menus = []

	header = ""

	name = "shell"
	
	prompt = "->"

	def __init__(self):
		cmd.Cmd.__init__(self)

		self.name = "Scrapper"
		# this should place sticky text on the top right side of the shell
		# you can change this text by calling sticker() from a commandthat appears in the top left of the shell
		self.header = """Welcome to Scrapper, a console application focused on data. Built by Tomas Gonzalez."""

		init()
		
		console.set_color(1,0,0)

		print(self.header)

	# Generic operation commands
	def help_quit(self):
		print ("Exit shell.")
	def do_quit(self, commandline):
		return True

	# Really cool command that allows for interaction with the operative system
	# This method should be upgraded to use the subprocess module instead of os

	def do_shell(self, s):
		os.system(s)

	def help_shell(self, s):
		print("Execute shell commands")

	def help_p(self, p):
		print("Utility command for testing purposes")

	def do_p(self, p):
		pass

	def help_p(self, p):
		print("Execute a python instruction")

	def help_sources(self, p):
		print("Interaction with data sources")

	def do_sources(self, p, *args):
		
		if p in sources.__all__:
			print(sources.get_properties(p))
			print(getattr(sources, p))
		
		if p == 'list':
			print(sources.__all__)
	
		if p.split(' ')[1] == "get":
			s = getattr(sources, p.split(' ')[0])
			d = getattr(s, p.split(' ')[2])
			print(d)
				
	# internal methods
	def _add_menus(self):
		pass


# Init interactive console
shell = Shell()
shell.cmdloop()

