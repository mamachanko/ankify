#!/usr/bin/env bash

set -euxo pipefail

cd "$(dirname "$0")"/..

main() {
  unit_tests
  e2e_tests
}

unit_tests() {
  pytest -vv
}

e2e_tests() {
  rm -rf notes.apkg
  ./ankify.py fixtures/notes.md
  file notes.apkg

  rm -rf notes2.apkg
  ./ankify.py < fixtures/notes.md > notes2.apkg
  # cat notes.md | ./ankify.py > notes2.apkg
  file notes2.apkg
}

main

