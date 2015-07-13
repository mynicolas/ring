#!/usr/bin/env python
#-*- coding: utf-8 -*-

class RingTypeError(Exception):
	def __init__(self):
		self.message = "type of ring element should be alike"


class StepTypeError(Exception):
	def __init__(self):
		self.message = "the variable 'step' should be >= 0"
		