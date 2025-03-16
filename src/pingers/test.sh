#!/bin/bash

SOCKS_HOST="10.0.0.25"
SOCKS_PORT="9050"
TEST_HOST="iwojimagzktuisvveh6zjuv453wm6rnch6oefof66mt7nuoxn4nliwqd.onion"
TEST_PORT="80"

s1=`adjtimex | grep -i tv|awk -F" " '{print $2}'|sed ':a;N;$!ba;s/\n//g'`
r=`echo "test"|\
socat -t 10 stdio SOCKS4A:"$SOCKS_HOST":"$TEST_HOST":"$TEST_PORT",socksport="$SOCKS_PORT",connect-timeout=10,shut-none \
> /allout.txt 2>&1;\
cat /allout.txt | grep fail|wc -l`
s2=`adjtimex | grep -i tv|awk -F" " '{print $2}'|sed ':a;N;$!ba;s/\n//g'`
[ "$r" == 1 ] && exit 10000 || exit bc -l <<< $((s2-s1))/10000000