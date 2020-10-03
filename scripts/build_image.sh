#!/usr/bin/env bash

set -euxo pipefail

docker \
  build . \
  --tag ankify:latest

