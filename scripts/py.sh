#!/usr/bin/env bash

set -euo pipefail

INTERACTIVETTY=""

if [ -t 0 ] ; then
  INTERACTIVETTY="--interactive --tty"
fi

docker run \
  $INTERACTIVETTY \
  --volume $(pwd):/src \
  --workdir /src \
  practical_vim:latest \
  ${@:-python}

