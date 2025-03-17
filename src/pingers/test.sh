#!/bin/bash

TEST_HOST=$1
TEST_PORT=$2
SOCKS_HOST=`echo $3|awk -F":" '{print $1}'`
SOCKS_PORT=`echo $3|awk -F":" '{print $2}'`

#echo $TEST_HOST $TEST_PORT $SOCKS_HOST $SOCKS_PORT

s1=`adjtimex | grep -i tv|awk -F" " '{print $2}'|sed ':a;N;$!ba;s/\n//g'`
r=`echo "test"|\
socat -t 2 stdio SOCKS4A:"$SOCKS_HOST":"$TEST_HOST":"$TEST_PORT",socksport="$SOCKS_PORT",connect-timeout=2,shut-none \
> /allout.txt 2>&1;\
cat /allout.txt | grep fail|wc -l`
s2=`adjtimex | grep -i tv|awk -F" " '{print $2}'|sed ':a;N;$!ba;s/\n//g'`
[ "$r" == 1 ] && ping_test=10000 || ping_test=$(bc -l <<< $((s2-s1))/100000000)
ping_int=$(printf "%.0f" "$ping_test")

if [ "$ping_int" -lt 0 ] || [ "$ping_int" -gt 1000000 ]; then
  ping_tmp=0
else
  ping_tmp=$ping_int
fi

[ "$ping_tmp" -eq 10000 ] && ping_ret='-1' || ping_ret=$ping_tmp

echo -n $ping_ret
