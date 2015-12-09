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
    logger.debug('Retrieving user data')
    me = api.me_with_related_data().get()

    toggl_tz = me.data.timezone().data
    logger.debug('Timezone set to "{}"'.format(toggl_tz))


if __name__ == '__main__':
    main()
