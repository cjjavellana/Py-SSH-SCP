import unittest, os, sys, mock, logging

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, '{}/../src'.format(dir_path))

from scpcopy import ScpCopy
from httpuploader import HttpUploader

logging.basicConfig(level=logging.DEBUG)

class RemoteFileCopyTestCase(unittest.TestCase):

  def setUp(self):
    self.log = logging.getLogger(__name__)
    self.connection = mock.Mock()
    self.connection.get = mock.Mock()
    self.scpcopy = ScpCopy(self.connection)

  def test_copy_file_to_current_workdir(self):
    self.scpcopy.get('/tmp/remote_to_current_workdir.txt')
    self.connection.get.assert_called_once_with('/tmp/remote_to_current_workdir.txt', None)

  def test_copy_file_with_local_dest(self):
    self.scpcopy.get('/tmp/remote_to_tmp.txt', '/tmp')
    self.connection.get.assert_called_once_with('/tmp/remote_to_tmp.txt', '/tmp')

  def test_copy_matching_files(self):
    self.connection.run = mock.Mock()
    self.scpcopy._listfiles = mock.MagicMock(return_value=['/tmp/test1', '/tmp/test2'])
    self.scpcopy.get = mock.Mock()
    r = self.scpcopy.get_matches('/tmp', 'tes*', '/tmp/workdir')
    self.assertEqual(r, ['/tmp/workdir/test1', '/tmp/workdir/test2'])
    self.assertEqual(self.scpcopy.get.call_count, 2)

class HttpFileUploaderTestCase(unittest.TestCase):

  def setUp(self):
    self.log = logging.getLogger(__name__)

  @mock.patch('httpuploader.requests')
  def test_upload_single_file(self, mock_request):
    open_name = '%s.open' % __name__
    mock_request.post = mock.Mock()

    self.httpuploader = HttpUploader()
    with mock.patch(open_name, create=True) as mock_open:
      mock_open.return_value = mock.MagicMock(spec=file)
      self.httpuploader.upload(url='/api/v1/upload', files={'file': open('report.xls', 'rb')})
      mock_request.post.assert_called_once_with(url='/api/v1/upload', files={'file': open('report.xls', 'rb')})