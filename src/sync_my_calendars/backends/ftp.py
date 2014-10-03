#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ftplib

from sync_my_calendars.config import BLUEMIND
from sync_my_calendars.config import FTP


def send_events():

    if not FTP['ACTIVE']:
        return

    ftp = ftplib.FTP()
    ftp.connect(FTP['HOST'], FTP['PORT'])
    ftp.login(FTP['USERNAME'], FTP['PASSWORD'])
    ftp.cwd(FTP['DIRECTORY'])

    if BLUEMIND['ACTIVE']:
        file_path = os.path.join(
            BLUEMIND['LOCAL_DIRECTORY'],
            BLUEMIND['ICS_FILENAME']
        )
        upload_file = open(file_path, 'r')
        ftp.storlines(
            'STOR {}'.format(BLUEMIND['ICS_FILENAME']),
            upload_file
        )
        #ftp.storbinary(
        #    'STOR {}'.format(BLUEMIND['ICS_FILENAME']),
        #    upload_file
        #)
        upload_file.close()

    ftp.quit()
