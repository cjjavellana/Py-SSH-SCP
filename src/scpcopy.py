import logging
import os
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
    self.logger.info('Copying (remote) {} from {} to (local) {}'.format(
      remotefile, self.connection.host, local))
    self.connection.get(remotefile, local)

  def get_matches(self, remotedir, filepattern, local=None):
    '''
    Copy multiple files that matches the remotedir/filepattern pattern from remote host
    '''
    files = self._listfiles(remotedir, filepattern)
    self.logger.info('Search Result for {}/{} => {}'.format(remotedir, filepattern, files))

    base = os.getcwd() if local is None else local
    if not base.endswith(os.sep):
      base = ''.join([base, '/'])

    copied_files = []
    for f in files:
      stagedfiled = ''.join([base, os.path.basename(f)])
      self.get(f, stagedfiled)
      copied_files.append(stagedfiled)

    return copied_files

  def _listfiles(self, remotedir, filepattern):
    r = self.connection.run('for f in `ls {}/{}`; do echo $f; done;'.format(remotedir, filepattern),
      hide='both')
    files = r.stdout.replace('\r', '').split('\n')
    return [f for f in files if f != '']