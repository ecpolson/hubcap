#!/usr/bin/python
import time

from logger import Logger

class State(object):
  def __init__(self):
    self.log = Logger(filepath='/proj/hubcap/hubcap/logs/logger.log')


class Armed():
  def __init__(self, state=None):
    if state is None:
      state = State()
    self.log = state.log
    self.log.INFO('ARMED')
    self.state = state
  def getState(self):
    return 'Armed'
  def sync(self):
    print('ARMED')
  def transition(self):
    return True
  def wait(self):
    time.sleep(2)
  def next(self):
    self.log.INFO('disarming')
    return Disarmed(self.state)

class Disarmed(State):
  def __init__(self,state):
    self.log = state.log
    self.log.INFO('DISARMED')
    self.state = state
  def getState(self):
    return 'Disarmed'
  def sync(self):
    print('DISARMED')
  def transition(self):
    return True
  def wait(self):
    time.sleep(4)
  def next(self):
    self.log.INFO('arming')
    return Armed(self.state)
