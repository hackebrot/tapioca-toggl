# -*- coding: utf-8 -*-

import ConfigParser
import logging
import os

import tapioca_toggl

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('TOGGL')

config = ConfigParser.RawConfigParser()
config.read(os.path.expanduser('~/.togglrc'))

logger.debug('Reading auth from user config')
api = tapioca_toggl.Toggl(access_token=config.get('Toggl', 'access_token'))


def main():
    pass

if __name__ == '__main__':
    main()
