#!/bin/bash
echo 'fetching data'
source ${OPENSHIFT_HOMEDIR}/python/bin/activate_virtenv
python ${OPENSHIFT_HOMEDIR}/fetch.py
echo 'end fetching'
