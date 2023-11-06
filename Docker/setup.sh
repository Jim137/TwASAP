#!/bin/bash

twid=($TWITTER_ID)
dccid=($DISCORD_CHANNEL_ID)

twid+=($TWITTER_ID1)
dccid+=($DISCORD_CHANNEL_ID1)

twid+=($TWITTER_ID2)
dccid+=($DISCORD_CHANNEL_ID2)

len=${#twid[@]}

for (( i=0; i<$len; i++ )); do
if [ ! -z "${twid[$i]}" ] ; then
  echo "${twid[$i]},${dccid[$i]}" >> ./id.csv
fi
done

exec /bin/bash exec.sh
