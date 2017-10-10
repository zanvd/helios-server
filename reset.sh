#!/bin/bash

PYTHON=python3
SETTINGS=${1:-settings}

source <($PYTHON dumpvars.py $SETTINGS)

if [ -n "$HOST" ]; then
    HOST="-h $HOST"
else
    HOST=""
fi
if [ -n "$USER" ]; then
    SUDO="sudo -u $USER"
else
    SUDO=""
fi

$SUDO dropdb $HOST helios
$SUDO createdb $HOST helios
$PYTHON manage.py makemigrations --settings=$SETTINGS
$PYTHON manage.py migrate --settings=$SETTINGS
echo "$SHELLCMD" | $PYTHON manage.py shell --settings=$SETTINGS
