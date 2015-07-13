#!/usr/bin/env python
#-*- coding: utf-8 -*-
from ringexception import *

class Distance(object):
  def __init__(self, distance):
    """
    距离类
    包含两个属性
    rdistance: cursor到portal的顺时针位置
    ldistance: cursor到portal的逆时针位置
    """
    self.rdistance = distance['rdistance']
    self.ldistance = distance['ldistance']


class Ring(object):
  def __init__(self, *args):
    """
    环容器类
    data:     环容器所有元素的列表形式
    size:     环容器的当前规模
    portal:   环容器的入口
    distance: 环容器的cursor到portal的位置对象，该对象为Distance类的实例
    """
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

    self.size = len(self.data)
    self.portal = self.cursor = 0
    self.distance = Distance({
      "ldistance": 0,
      "rdistance": len(self.data) - self.cursor
    })

  @self._updateAll
  def rspin(self, step):
    """
    cursor顺时针旋转
    @param step: 旋转步进
    """
    self._spin(step)
    self.cursor = step % len(self.data)
    return self

  @self._updateAll
  def lspin(self, step):
    """
    cursor逆时针旋转
    @param step: 旋转步进
    """
    self._spin(step)
    self.cursor = len(self.data) - step % len(self.data)
    return self

  def _spin(self, step):
    if step < 0:
      raise StepTypeError

  def _updateAll(self, func):
    def _deco(*args):
      return func(*args)
    return _deco

  def _updateSize(self):
    pass

  def _updateCursor(self):
    pass

  def _updateDistance(self):
    pass


  

