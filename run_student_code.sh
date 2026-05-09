#!/bin/bash

EXECUTABLE=./JackCompiler

pushd /autograder/source/ >/dev/null

# remove old files
rm -rf ./${1} 1>/dev/null

# copy test files over
mkdir -p ./${1} 1>/dev/null
chmod -R ugo+rw ./${1} 1>/dev/null
cp /autograder/grader/tests/${1}/* ./${1} 1>/dev/null

# run student-submitted code (untrusted)
runuser -u student -- ${EXECUTABLE} ${1}

cp /autograder/grader/tests/expected-outputs/${1}/Main.tst ${1} 1>/dev/null
cp /nand2tetris/tools/OS/*.vm ./${1} 1>/dev/null

popd >/dev/null
