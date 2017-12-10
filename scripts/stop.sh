#!/bin/sh

[[ -e /etc/init/talkmeup.conf ]] \
  && status talkmeup | \
    grep -q '^talkmeup start/running, process' \
  && [[ $? -eq 0 ]] \
  && stop talkmeup || echo "Application not started"
