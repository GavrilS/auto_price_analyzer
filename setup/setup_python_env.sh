#!/bin/bash

PYVERSION=$(python --version)
# echo "python version = $PYVERSION"

if [[ "$PYVERSION" == *"Python 3"* ]]; then
    echo "Python 3 is installed, python version - $PYVERSION"
else
    echo "Python 3 is not installed!!!"
    exit 1
fi
