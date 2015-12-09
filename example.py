# -*- coding: utf-8 -*-

import ConfigParser
import datetime
import logging
import os

import arrow
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

    pid_by_name = {
        project.name().data: project.id().data
        for project in me.data.projects
    }
    logger.debug(pid_by_name)

    start = arrow.get(datetime.datetime(2015, 12, 1), toggl_tz)
    stop = arrow.get(datetime.datetime(2015, 12, 9), toggl_tz)

    workdays = [
        day for day in
        arrow.Arrow.range('day', start, stop)
        if day.isoweekday() not in [6, 7]
    ]

    time_entries = api.time_entries()

    for workday in workdays:
        a = workday.replace(hours=9, minutes=15)
        b = workday.replace(hours=9, minutes=30)

        time_entries.post(data={
            'time_entry': {
                'description': 'COFFEEE! :D',
                'pid': pid_by_name['misc'],
                'start': a.to('utc').isoformat(),
                'stop': b.to('utc').isoformat(),
                'duration': (b - a).seconds,
                'created_with': 'tapioca-toggl',
                'tags': ["Yum!", "Let's go!"]
            }
        })


if __name__ == '__main__':
    main()
