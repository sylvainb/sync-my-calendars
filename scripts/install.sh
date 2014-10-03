#!/bin/bash
#
# cd sync-my-calendars
# ./scripts/install.sh
# ===> create virtualenv, install the module
#
# cd sync-my-calendars
# ./scripts/install.sh clean
# ===> WARNING: remove virtualenv files, create virtualenv, and install the module

function print()
{
    echo ''
    echo '================================================'
    echo $1
    echo '================================================'
    echo ''
}

if [ $1 == clean ]; then
  if [ -f bin/python ]; then
      print "Remove virtualenv files"
      rm -rf bin include lib man .Python
      # rm -rf htmlcov .coverage
  fi
fi

if [ ! -f bin/python ]; then
    print "Install a virtual in the current directory"
    virtualenv .
    source bin/activate
    easy_install -U setuptools
    easy_install -U distribute
fi

print "Install the module"
source bin/activate
pip install -e .
# pip install coverage
# pip install nose

chmod +x ./scripts/sync.sh


