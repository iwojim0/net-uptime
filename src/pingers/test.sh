#!/bin/bash

TEST_HOST=$1
TEST_PORT=$2
SOCKS_HOST=`echo $3|awk -F":" '{print $1}'`
SOCKS_PORT=`echo $3|awk -F":" '{print $2}'`

#echo $TEST_HOST $TEST_PORT $SOCKS_HOST $SOCKS_PORT

s1=`adjtimex | grep -i tv|awk -F" " '{print $2}'|sed ':a;N;$!ba;s/\n//g'`
r=`echo "test"|\
socat -t 10 stdio SOCKS4A:"$SOCKS_HOST":"$TEST_HOST":"$TEST_PORT",socksport="$SOCKS_PORT",connect-timeout=10,shut-none \
> /allout.txt 2>&1;\
cat /allout.txt | grep fail|wc -l`
s2=`adjtimex | grep -i tv|awk -F" " '{print $2}'|sed ':a;N;$!ba;s/\n//g'`
[ "$r" == 1 ] && ping='10000' || ping=`bc -l <<< $((s2-s1))/100000000`

echo -n $ping
