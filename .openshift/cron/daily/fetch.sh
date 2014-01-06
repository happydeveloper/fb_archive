#!/bin/bash
echo 'fetching data'
source ${OPENSHIFT_HOMEDIR}python/virtualenv/bin/activate
python ${OPENSHIFT_HOMEDIR}app-root/repo/fetch.py
echo 'end fetching'
