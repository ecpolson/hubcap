#!/usr/bin/python
import time

class Logger():
  
  def __init__(self,filepath=None):
    if filepath is not None:
      self.filepath = filepath
    else:
      self.filepath = '/proj/hubcap/hubcap/logs/logging.log'
    f = open(self.filepath, 'w')
    f.close()
    self.topic = {'INFO':'info',
                  'WARN':'warn',
                  'ERROR':'error',
                  'ALERT':'alert',
                  'FATAL':'fatal'}

  def INFO(self,message):
    '''Used to log informational messages'''
    self.sendLog(self.topic['INFO'],
            '[INFO ]:{0}'.format(message))

  def ALERT(self,message):
    '''Used to log security related messages'''
    self.sendLog(self.topic['ALERT'],
            '[ALERT]:{0}'.format(message))

  def WARN(self,message):
    '''Used to log errors that do not affect system function'''
    self.sendLog(self.topic['WARN'],
            '[WARN ]:{0}'.format(message))

  def ERROR(self,message):
    '''Used to log errors that impact non-critical function'''
    self.sendLog(self.topic['ERROR'],
            '[ERROR]:{0}'.format(message))

  def FATAL(self,message):
    '''Used to log errors and exceptions that impact critical function'''
    self.sendLog(self.topic['FATAL'],
            '[FATAL]:{0}'.format(message))
    
  def sendLog(self,topic,message):
    #not using topic currently
    with open(self.filepath, 'a') as f:
      f.write('{0}{1}\n'.format(
                  '{0}'.format(time.time()).split('.')[0],
                  message))
    
