from abc import ABC, abstractmethod
from random import random


class Notes():
  notes = "Do  re   mi   fa   sol   la   ti".split("  ")

class InterfaceKeys(ABC):

  notes = Notes()

  @abstractmethod
  def keyboard(self, pressed:list=None) -> None or str:
    """SOunds form pressing keys"""
    pass
  
class Piano(InterfaceKeys):

  def keyboard(self, pressed:list=None) -> None or str:
    """SOunds form piano keys"""
    if pressed is None:
      return
    return f"Sounds by hitting strings {pressed}, that is {self.__class__.notes}"

class Clavecin(InterfaceKeys):

  def keyboard(self, pressed:list=None) -> None  or str:
    """SOunds form clavecin keys"""
    if pressed is None:
      return
    return f"Sounds by picking strings {pressed}"


class Creator(type):
  """makes talanted people like Artist"""
  _master_pieces = {}

  def __init__(cls, *args, **kwargs):
    super(Creator, cls).__init__(cls)
    cls.STAR = hash(cls)
    print(cls, args, kwargs)
    
  #cls = artist
  def __call__(cls, name):
    _alias = cls.__class__._master_pieces
    key = cls.__name__+name
    if _alias.get(key, False):
      print('already exists, not repeat')
      return _alias[key]
    _alias[key] = super().__call__(name)
    return _alias[key]

class Master(metaclass=Creator):
  STAR = None
  YEAR = None
  #self = master_pieces
  def __init__(self, name, date='?'):
    self.name = name
    self.date = date


class DaVinci(Master):
  YEAR = 1452


class Composer(Master):

  def compose(self, notes:list):
    self.notes = notes

  @classmethod
  def play(cls, instument: InterfaceKeys, notes:list=None):
    return f"{cls} plays {instument} making {instument.keyboard(notes)}"

class Beethoven(Composer):
  YEAR = 1770


class Mozart(Composer):
  YEAR = 1756



