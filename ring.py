#!/usr/bin/env python
#-*- utf-8 -*-

class Distance(object):
  def __init__(self, distance):
    self.rdistance = distance['rdistance']
    self.ldistance = distance['ldistance']

class Ring(object):
  def __init__(self, *args):
    _isValid = reduce(lambda x, y: type(x) == type(y), args)
    if not _isValid:
      raise RingTypeError

    # self.data = list(args[0]) if len(args) == 1 and isinstance(args[0], (list, tuple)) else self.data = list(args)
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
      self.data = list(args[0])
    else:
      self.data = list(args)  
      
    if len(args) >= 2:
      self.data = list(args)

    self.portal = self.cursor = 0
    self.distance = Distance({
      "ldistance": 0,
      "rdistance": len(self.data) - self.cursor
    })

  def rspin(self, step):
    self._spin(step)
    
    self.cursor = step % len(self.data)
    return self

  def lspin(self, step):
    self._spin(step)

    self.cursor = len(self.data) - step % len(self.data)
    return self

  def _spin(self, step):
    if step < 0:
      raise StepTypeError


  

