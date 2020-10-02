#!/usr/bin/env bash

set -euxo pipefail

main() {
  docker run \
    --interactive \
    --tty \
    --volume $(pwd):/src \
    --workdir /src \
    practical_vim:latest \
    ./make-deck.py $@
}

main $@

