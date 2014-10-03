#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sync_my_calendars.services import bluemind
from sync_my_calendars.backends import ftp

bluemind.get_events()
ftp.send_events()
