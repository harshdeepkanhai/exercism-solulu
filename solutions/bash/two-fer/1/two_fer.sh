#!/usr/bin/env bash

main (name) {
    if [[ $name = ''  ]]
    then
        echo "One for you, one for me"
    else
        echo "One for $name, one for me"
}

main "$name"

