#!/bin/bash

[[ $# -ge 1 ]] || exit
[[ $# -ge 2 ]] || printf $1:

texfile="$1"
grep '\\includegraphics' "$texfile" | sed -E 's/\\includegraphics\{(.+)}/\1 /g' | tr -d '\n'

included=$(grep '\\input' "$texfile" | sed -E 's/\\input\{(.+)\}/\1/')
for f in $included; do
    printf "$f"
    ./texdeps.sh $f None
done
