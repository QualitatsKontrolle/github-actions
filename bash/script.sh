#!/usr/bin/bash -x

read -p "Enter number: " number

if [ "$number" = "1" ]; then
    echo "Number equals 1"
else
    echo "Number is not equal"
fi
