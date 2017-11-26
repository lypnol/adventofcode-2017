#!/bin/bash
# set -ev
declare a CHANGED

for DAY_DIRECTORY in `git --no-pager diff --name-only ${TRAVIS_COMMIT_RANGE} | cut -d "/" -f1`
do
    if [[ $DAY_DIRECTORY == day-* ]]; then
        DAY=$(echo $DAY_DIRECTORY | cut -d'-' -f 2)
        if [[ " ${CHANGED[*]} " == *" ${DAY} "* ]]; then
            continue;
        else
            CHANGED=("${CHANGED[@]}" "${DAY}")
            python main.py -d $DAY;
        fi
    fi
done
