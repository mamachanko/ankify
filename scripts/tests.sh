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
  ./scripts/run.sh fixtures/notes.md
  file notes.apkg
}

main

