#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python suds documentation:
https://fedorahosted.org/suds/wiki/Documentation

BlueMind documentation
https://forge.blue-mind.net/confluence/display/LATEST/Documentation+BlueMind
"""

import os
from datetime import datetime
from suds.client import Client
from icalendar import Calendar, Event

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
    date_max = '{0}-12-31'.format(datetime.today().year + 1)
    icalendar = client.service.exportICS(
        accesstoken,
        datetime.strptime(date_max, '%Y-%m-%d')
    )
    #icalendar_ics = icalendar.encode('utf8')

    # Filter the calendar subcomponents with the icalendar python module
    pycal = Calendar.from_ical(icalendar)
    subcomponents = []

    for subcomponent in pycal.subcomponents:

        # Filter events
        if type(subcomponent) is Event \
           and BLUEMIND['EVENT_FILTER'] is not None \
           and BLUEMIND['EVENT_FILTER'](subcomponent) is False:
            continue

        subcomponents.append(subcomponent)

    pycal.subcomponents = subcomponents
    pyicalendar_ics = pycal.to_ical()

    # Save it to the filesystem
    file_path = os.path.join(
        BLUEMIND['LOCAL_DIRECTORY'],
        BLUEMIND['ICS_FILENAME']
    )
    with open(file_path, 'w') as f:
        f.write(pyicalendar_ics)

    # Logout from Bluemind
    client.service.logout(accesstoken)
