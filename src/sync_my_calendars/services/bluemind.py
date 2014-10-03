#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python suds documentation:
https://fedorahosted.org/suds/wiki/Documentation

BlueMind documentation
http://docs.blue-mind.net/2/index.jsp
"""

import os
from datetime import datetime
from suds.client import Client

from sync_my_calendars.config import BLUEMIND


def get_events():

    if not BLUEMIND['ACTIVE']:
        return

    # Connect to BlueMind SOAP API
    client = Client(BLUEMIND['SOAP_URL'])

    # Display the SOAP API
    # print client

    # Retrieve an access token
    accesstoken = client.service.login(
        BLUEMIND['USERNAME'],
        BLUEMIND['PASSWORD'],
        BLUEMIND['ORIGIN']
    )

    # Export the iCalendar (until the end of the next year)
    date_max = '{}-12-31'.format(datetime.today().year + 1)
    icalendar = client.service.exportICS(
        accesstoken,
        datetime.strptime(date_max, '%Y-%m-%d')
    )

    # Save it to the filesystem
    file_path = os.path.join(
        BLUEMIND['LOCAL_DIRECTORY'],
        BLUEMIND['ICS_FILENAME']
    )
    with open(file_path, 'w') as f:
        f.write(icalendar.encode('utf8'))

    # Logout from Bluemind
    client.service.logout(accesstoken)
