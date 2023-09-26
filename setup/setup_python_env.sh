#!/bin/bash

PYVERSION=$(python3 --version)
# echo "python version = $PYVERSION"

if [[ "$PYVERSION" == *"Python 3"* ]]; then
    echo "Python 3 is installed, python version - $PYVERSION"
else
    echo "Python 3 is not installed!!!"
    exit 1
fi

echo "Python version found and script is continuing"

python3 -m pip install virtualenv && python3 -m venv env && source env/bin/activate \
    && pip install scrapy && pip install django
