import requests, logging

class HttpUploader(object):

  def __init__(self):
    self.logger = logging.getLogger(__name__)

  def upload(self, url, files=None):
    self.logger.info('Uploading {} to {}'.format(files, url))
    requests.post(url=url, files=files)