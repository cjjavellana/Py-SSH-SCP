import requests
import sys, os, logging.config, yaml
import logging
import argparse

from fabric import Connection

logger = None
dir_path = os.path.dirname(os.path.realpath(__file__))

def parse_args(argv):
  parser = argparse.ArgumentParser(description='Parse command line arguments')
  parser.add_argument('--host', metavar='hostname', help='The remote host', 
    dest='host')
  parser.add_argument('--user', metavar='user', help='The user to authenticate with on the remove host', 
    dest='user')
  parser.add_argument('--port', metavar='22', type=int, 
    default=22, help='The port on the remote host. (Default 22)', dest="port")
  parser.add_argument('--keyfile', metavar='id_rsa', 
    help='The private key file for authentication', dest="keyfile")
  parser.add_argument('--filename', metavar='file1|file*', 
    help='The filename or filename pattern to copy from the remote host', 
    dest="filename")
  parser.add_argument('--remotedir', metavar='/tmp', 
    help='The remote directory where to copy the files from', 
    dest="remotedir")
  parser.add_argument('--uploadendpoint', metavar='/api/v1/upload', 
    help='The API Server to upload the files to after copying it from the remote host', 
    dest="upload_endpoint")
  return parser.parse_args()

def copy(options):
  global logger
  from scpcopy import ScpCopy

  logger.info("{} {} {} {}".format(options.host, options.port, options.filename, options.upload_endpoint))
  connection = Connection(options.host, 
    user=options.user, 
    port=options.port,
    connect_timeout=10,
    connect_kwargs={"key_filename": options.keyfile})
  scpcopy = ScpCopy(connection)
  #scpcopy.get('{}/{}'.format(options.remotedir, options.filename), '/tmp/tes3.txt')
  scpcopy.get_matches(options.remotedir, options.filename)
  connection.close()

def setup_logging(
    default_path='logging.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'

):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

def main():
  global logger

  logger = logging.getLogger(__name__)
  options = parse_args(sys.argv[1:])
  copy(options)

setup_logging()
if __name__ == '__main__':
  main()
