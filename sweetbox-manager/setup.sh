#! /usr/local/bin/bash

pip install virtualenv

PYTHON='/usr/local/bin/python2.7'
virtualenv -p $PYTHON virtual

source virtual/bin/activate

pip install -r requirements.txt

# Tool for automatically activating virtual environment
brew install autoenv
echo 'source /usr/local/opt/autoenv/activate.sh' >> ~/.bash_profile