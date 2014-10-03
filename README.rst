===============================================
sync-my-calendars
===============================================

.. contents:: Table of Contents
   :depth: 2

Overview
--------

Goals :

    * Get events from Bluemind and Wunderlist and store them as ical calendar files.
    * Send ical files to an FTP server or Dropbox.

System requirements
-------------------

    * bash
    * wget
    * a working SMTP server

Installation
------------

Install in a virtualenv
~~~~~~~~~~~~~~~~~~~~~~~

Download ``sync-my-calendars`` and use ``virtualenv`` to install the module :
::
  sudo apt-get install python-virtualenv
  cd sync-my-calendars
  chmod +x ./scripts/install.sh
  ./scripts/install.sh

  source bin/activate
  (sync-my-calendars) python
  >>> import sync_my_calendars

Configuration
~~~~~~~~~~~~~~

Create an edit the configuration file :
::
  (sync-my-calendars) cd src/sync_my_calendars/
  (sync-my-calendars) cp config.py.sample config.py
  (sync-my-calendars) vi config.py

Add a cron JOB
~~~~~~~~~~~~~~~

Create a file <where-you-want>/sync_my_calendars.sh with the following content (don't forget to adapt <egg-directory>)..
::
    #!/bin/bash
    cd <egg-directory>
    scripts/sync.sh

Change permissions settings for the cron bash script :
::
    chmod +x <where-you-want>/sync_my_calendars.sh

Edit your personal crontab :
::
    crontab -e

And and adapt the following lines :
::
    # Launch sync_my_calendars script every 1 hour
    0 * * * * <where-you-want>/sync_my_calendars.sh >> /tmp/sync_my_calendars.cron.log

Credits
-------

    * Sylvain Boureliou [sylvainb] - `Github <https://github.com/sylvainb/>`_ - `Website <http://www.boureliou.com>`_

Source code
-----------

`Source code <https://github.com/sylvainb/sync-my-calendars>`_ is hosted on Github.

How to contribute and submit a patch ?
--------------------------------------

`Source code <https://github.com/sylvainb/sync-my-calendars>`_ and an `issue tracker <https://github.com/sylvainb/sync-my-calendars/issues>`_ is hosted on Github.


