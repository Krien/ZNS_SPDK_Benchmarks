#!/bin/bash
set -e

if [[ $# -lt 1 ]]; then
    echo ""
    echo "Please provide an argument containing a path to a file to process"
    echo ""
    exit 1
fi

if [[ ! -f $1 ]]; then
    echo ""
    echo "file not found, please provide a valid path"
    echo ""
    exit 1
fi

if [[ $2 = "tropodb" ]]; then
    awk  'BEGIN{RS=","} {print}' $1     \
        | head -n -1                    \
        | tail -n +2                    \
        | awk '{print $1,NR-1}' FS=" "  \
        | awk -f resets_to_json.awk
else
    awk  '$1 == "R" {print $2}' $1 \
        | sort -n                  \
        | uniq -c                  \
        | awk -f resets_to_json.awk
fi
