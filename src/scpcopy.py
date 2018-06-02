import logging
from fabric import Connection

class ScpCopy(object):

  def __init__(self, connection):
    self.logger = logging.getLogger(__name__)
    self.connection = connection

  def get(self, remotefile, local=None):
    '''
    Copies a file from a remote host
    
    remotefile - The file to copy.
    local - The local destination to copy the file to. If None, resolves 
     os.getcwd()
    '''
    self.logger.info('Copying file {} from {}'.format(remotefile, self.connection.host))
    self.connection.get(remotefile, local)