#!/usr/bin/env bash

set -euo pipefail

cd "$(dirname "$0")"/..

./scripts/tests.sh

docker build . --tag mamachanko/ankify:latest

