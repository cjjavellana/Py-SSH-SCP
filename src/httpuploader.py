import requests, logging

class Upload(object):

  def __init__(self, files):
    self.logger = logging.getLogger(__name__)
    self.files = files

  def to(self, url):
    self.url = url
    return self

  def with_options(self, options_dict):
    self.options_dict = options_dict
    return self

  def doit(self):
    self.logger.info('Uploading {} to {}'.format(self.files, self.url))
    return requests.post(url=self.url, files=self.files)

