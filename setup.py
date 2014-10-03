#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

version = '1.0dev'

description = \
    "Get events from Bluemind and Wunderlist and store them as ical " \
    "calendar files. Send ical files to an FTP server or Dropbox."
long_description = open("README.rst").read() + "\n" \
    + open(os.path.join("docs", "HISTORY.rst")).read()

setup(name='sync-my-calendars',
      version=version,
      description=description,
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='python calendar bluemind wunderlist',
      author='Sylvain Boureliou [sylvainb]',
      author_email='sylvain.boureliou@gmail.com',
      url='https://github.com/sylvainb/sync-my-calendars',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'suds',
      ],
      entry_points={
      }
      )
