#!/usr/bin/python
import sys
sys.path.append('/proj/hubcap/hubcap')
import unittest
from logger import Logger

class TestLoggingFunctions(unittest.TestCase):

  def __init__(self, *args, **kwargs):
    super(TestLoggingFunctions, self).__init__(*args, **kwargs)
    self.log = Logger()
  
  def test_INFO(self):
    self.log.INFO('test')
    self.checkLog('INFO')

  def test_WARN(self):
    self.log.WARN('test')
    self.checkLog('WARN')

  def test_ALERT(self):
    self.log.ALERT('test')
    self.checkLog('ALERT')

  def test_ERROR(self):
    self.log.ERROR('test')
    self.checkLog('ERROR')

  def test_FATAL(self):
    self.log.FATAL('test')
    self.checkLog('FATAL')

  def checkLog(self,level):
    with open(self.log.filepath, 'r') as f:
      line = f.readlines()[-1]
      self.assertTrue(level in line)

if __name__ == '__main__':
  unittest.main()  
