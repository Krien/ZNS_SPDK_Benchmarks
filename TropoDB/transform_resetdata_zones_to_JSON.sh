#!/bin/bash
set -e

if [[ $# -lt 1 ]]; then
    echo "Please provide a valid path"
    return 1
fi

if [[ ! -f $1 ]]; then
    echo ""
    echo "BPF result not found, please provide a valid path"
    echo ""
    exit 1
fi

if [[ $2 -eq "tropodb" ]]; then
    awk  'BEGIN{RS=","} {print}' $1     \
        | head -n -1                    \
        | tail -n +2                    \
        | awk '{print $1,NR-1}' FS=" "  \
        | awk -f resets_to_json.awk

else
    awk '{print $2}' $1 \
        | head -n -4    \
        | tail -n +5    \
        | sort -n       \
        | uniq -c       \
        | awk -f resets_to_json.awk
fi
