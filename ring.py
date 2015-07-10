#!/usr/bin/env python
#-*- utf-8 -*-

class Ring(object):
  def __init__(self, *args):
    _isValid = reduce(lambda x, y: type(x) == type(y), args)
    if not _isValid:
      raise TypeError

    self.data = list(args[0]) if len(args) == 1 and isinstance(args[0], (list, tuple)) else self.data = list(args)
    if len(args) >= 2:
      self.data = list(args)

    self.portal = self.cursor = 0
    self.instance = {
      "linstance": 0
    }

  def 
