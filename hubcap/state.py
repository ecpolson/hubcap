#!/usr/bin/python
import time

class State(object):
  def __init__(self):
    pass
  def sync(self):
    pass
  def transition(self):
    pass
  def wait(self):
    pass


class Armed(State):
  def getState(self):
    return 'Armed'
  def sync(self):
    print('ARMED')
  def transition(self):
    return True
  def wait(self):
    time.sleep(2)
  def next(self):
    return Disarmed()

class Disarmed(State):
  def getState(self):
    return 'Disarmed'
  def sync(self):
    print('DISARMED')
  def transition(self):
    return True
  def wait(self):
    time.sleep(4)
  def next(self):
    return Armed()
