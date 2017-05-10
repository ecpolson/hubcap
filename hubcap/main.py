#!/usr/bin/python
import shutil
import time

from state import *
from logger import Logger

class Main():
  def __init__(self):
    self.state = Armed()
    self.log = Logger()

  def main(self):
    try:
      while True:
        print self.state.getState()
        self.state.wait()
        self.state.sync()
        if self.state.transition():
          self.state = self.state.next()
          print self.state.getState()
          self.log.INFO('{0}'.format(self.state.getState()))
    except KeyboardInterrupt:
      shutil.copytree('/proj/hubcap/hubcap/logs','/proj/hubcap/hubcap/archives/{0}/'.format(
                time.strftime("%m-%d-%y-%H%M%S")))

if __name__ == '__main__':
  main = Main()
  main.main()
