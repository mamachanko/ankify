#!/usr/bin/env bash

set -euxo pipefail

docker run -it -v $(pwd):/src -w /src practical_vim:latest ./make-deck.py

